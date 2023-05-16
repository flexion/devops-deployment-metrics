from github import Github


def connect_to_github(username: str, token: str) -> any:
    return Github(login_or_token=username, token=token, verify=True)
