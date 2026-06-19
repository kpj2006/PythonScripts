# This script stars all repositories of given github organizations.

import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN") # Go to your github account's developer settings, generate a classic token and add it to your ".env" file.
ORGS = ["AOSSIE-Org", "StabilityNexus", "DjedAlliance"]

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

for org in ORGS:
    page = 1 # Get all repositories

    while True:
        response = requests.get(
            f"https://api.github.com/orgs/{org}/repos",
            headers=headers,
            params={"per_page": 100, "page": page}
        )

        repos = response.json()

        if not repos:
            break

        for repo in repos:
            repo_name = repo["name"]

            star_response = requests.put(
                f"https://api.github.com/user/starred/{org}/{repo_name}",
                headers=headers
            )

            if star_response.status_code == 204:
                print(f"⭐ Starred {repo_name}")
            else:
                print(f"❌ Failed {repo_name}: {star_response.status_code}")
                print(star_response.status_code)
                print(star_response.text)

        page += 1

print("Done!")