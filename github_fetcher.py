import requests

def get_repo_files(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents"
    response = requests.get(url)

    files = []

    if response.status_code == 200:
        data = response.json()

        for item in data:
            if item["name"].endswith(".py"):
                files.append(item["download_url"])

    return files