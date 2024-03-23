import requests
from flask import Flask, jsonify, request
import mysql.connector
from werkzeug.urls import url_quote

app = Flask(__name__)

# Establish a connection to the database
#def create_connection():
    # connection = mysql.connector.connect(
    #     host="isuru-database-2.c1wakw0y4b18.eu-north-1.rds.amazonaws.com",
    #     user="admin",
    #     password="cde3CDE#",
    #     database="isuru_database_table_2"
    # )
    # return connection

# Call create_connection() function to establish a connection to the database
# db = create_connection()

# Endpoint for getting GitHub code changes
# Example URL: http://127.0.0.1:5000/get_github_code_changes?owner_username=SachiniTen&repository=Bootcamp&developer_username=SachiniTen
# Example URL: http://127.0.0.1:5000/get_github_code_changes?owner_username=IsuruVindula&repository=CloudComputing-CW&developer_username=IsuruVindula

@app.route('/get_github_code_changes', methods=['GET'])
def get_github_code_changes():
    # Get parameters from the request URL
    owner_username = request.args.get('owner_username')
    repository = request.args.get('repository')
    developer_username = request.args.get('developer_username')

    # Check if required parameters are missing
    if owner_username is None or repository is None or developer_username is None:
        return jsonify({'error': 'Missing required parameters'}), 400

    # GitHub API URL to retrieve contributor statistics
    contributor_stats_url = f"https://api.github.com/repos/{owner_username}/{repository}/stats/contributors"
    response = requests.get(contributor_stats_url)

    # GitHub API URL to retrieve repository details
    repo_details_url = f"https://api.github.com/repos/{owner_username}/{repository}"
    repo_details_response = requests.get(repo_details_url)

    # Check for successful API responses
    if response.status_code == 200: 
    # and repo_details_response.status_code == 200:
        contributors_data = response.json()
        repo_details_data = repo_details_response.json()

        # Filter contributions for the target user
        target_contributor = next(
            (contributor for contributor in contributors_data if contributor['author']['login'] == developer_username), None)

        if target_contributor:
            # Calculate added and deleted lines
            added_lines = sum(week['a'] for week in target_contributor['weeks'])
            deleted_lines = sum(week['d'] for week in target_contributor['weeks'])

            # Total file count in the repository
            total_files_count = repo_details_data.get('size', 0)

            # Insert data into the database
            cursor = db.cursor()
            insert_query = (
                "INSERT INTO isuru_database_table_2.github_code_changes(developer_username, repository, owner, "
                "added_lines_count, deleted_lines_count, total_files_count) VALUES (%s, %s, %s, %s, %s, %s)"
            )
            cursor.execute(insert_query, (developer_username, repository, owner_username, added_lines, deleted_lines, total_files_count))
            db.commit()

            # Return JSON response with code changes
            return jsonify({
                'added_lines': added_lines,
                'deleted_lines': deleted_lines,
                'total_files_count': total_files_count,
            })
        else:
            print(f"Contributions not found for user '{developer_username}'.")
            return jsonify({'error': f"Contributions not found for user '{developer_username}'"})
    else:
        print(f"Error: {response.status_code}")
        return jsonify({'error': f"Error: {response.status_code}"})


# Run the Flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
