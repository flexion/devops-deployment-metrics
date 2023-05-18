from github import Github


def connect_to_github(username: str, password: str) -> any:
    return Github(login_or_token=username, password=password, verify=True)
