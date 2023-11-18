# find_good_first_issues.py
import requests
import csv
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise ValueError("GitHub token not found. Set GITHUB_TOKEN environment variable.")

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}"
}

def search_good_first_issues():
    query = 'label:"good first issue" language:python'
    url = f'https://api.github.com/search/issues?q={query}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        print(f"Error: {response.status_code}")
        return []

def save_to_csv(issues):
    with open('/app/repositories.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Repository', 'Issue Title', 'Issue URL'])
        for issue in issues:
            writer.writerow([
                issue['repository']['full_name'],
                issue['title'],
                issue['html_url']
            ])

if __name__ == "__main__":
    issues = search_good_first_issues()
    save_to_csv(issues)
