import requests
from github_fetcher import get_repo_files
from complexity_checker import analyze_code
from security_checker import check_security

repo = input("Enter repository (owner/repo): ")

owner, repo_name = repo.split("/")

files = get_repo_files(owner, repo_name)

print("\nRepository Analysis")
print("-------------------")

for file_url in files:
    response = requests.get(file_url)
    code = response.text

    lines, functions, classes = analyze_code(code)
    warnings = check_security(code)

    print("\nFile:", file_url.split("/")[-1])
    print("Lines:", lines)
    print("Functions:", functions)
    print("Classes:", classes)

    for w in warnings:
        print("Warning:", w)