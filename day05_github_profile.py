import requests
import json


def github_profile(username):
    base = "https://api.github.com"

    print(f"Collecting public GitHub data for: {username}")

    # Get public user information
    user_response = requests.get(
        f"{base}/users/{username}",
        timeout=10
    )
    user_response.raise_for_status()
    user = user_response.json()

    # Get public repositories
    repos_response = requests.get(
        f"{base}/users/{username}/repos",
        params={"per_page": 10},
        timeout=10
    )
    repos_response.raise_for_status()
    repos = repos_response.json()

    # Count programming languages
    languages = {}

    for repo in repos:
        language = repo.get("language")

        if language:
            languages[language] = languages.get(language, 0) + 1

    # Build profile
    profile = {
        "username": username,
        "name": user.get("name"),
        "company": user.get("company"),
        "location": user.get("location"),
        "public_repos": user.get("public_repos"),
        "top_languages": languages,
        "bio": user.get("bio")
    }

    return profile


# Public practice account from the internship example
username = "torvalds"

try:
    profile = github_profile(username)

    print("\n" + "=" * 60)
    print("          GITHUB OSINT PROFILE")
    print("=" * 60)

    print(json.dumps(profile, indent=4))

    # Save profile to JSON
    with open("github_profile.json", "w", encoding="utf-8") as file:
        json.dump(profile, file, indent=4)

    print("\nProfile saved to: github_profile.json")
    print("=" * 60)

except requests.RequestException as error:
    print(f"\nError accessing GitHub API: {error}")