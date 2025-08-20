import requests

username = "octocat"  # replace with any GitHub username
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()

for repo in repos:
    print(f"- {repo['name']}: {repo['html_url']}")
#This script will list each repository's name and its URL.

#Fetching Jokes from a Joke API
def fetch_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    resp = requests.get(url)
    joke = resp.json()
    print("\nHere's a joke for you:")
    print(f"{joke['setup']} — {joke['punchline']}")

if __name__ == "__main__":
    fetch_github_repos("octocat")  # replace with any GitHub username
    fetch_random_joke()