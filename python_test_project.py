import requests


ENDPOINT="http://16.171.58.216:5000"

# def test_home():
#     res = requests.get(ENDPOINT+'/')
#     assert res.status_code == 200
#     pass

def test_get_github_commits_count_main():
    res = requests.get(ENDPOINT+'/get_github_commits_count_main?owner_username=IsuruVindula&repository_name=CloudComputing-CW&developer_username=IsuruVindula')
    assert res.status_code == 200
    pass

def test_get_github_pull_requests():
    res = requests.get(ENDPOINT+'/get_github_pull_requests?owner_username=IsuruVindula&repository=CloudComputing-CW&developer_username=IsuruVindula')
    assert res.status_code == 200
    pass

def test_get_github_issues():
    res = requests.get(ENDPOINT+'/get_github_issues?owner_username=IsuruVindula&repository=CloudComputing-CW&developer_username=IsuruVindula')
    assert res.status_code == 200
    pass

# def test_get_github_code_changes():
#     res = requests.get(ENDPOINT+'/get_github_code_changes?owner_username=IsuruVindula&repository=CloudComputing-CW&developer_username=IsuruVindula')
#     assert res.status_code == 200
#     pass
