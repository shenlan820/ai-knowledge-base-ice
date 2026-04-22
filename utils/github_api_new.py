import requests

def get_repo_info(owner, repo_name):
    url = f'https://api.github.com/repos/{owner}/{repo_name}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'star_count': data['stargazers_count'],
            'forks_count': data['forks_count'],
            'description': data['description']
        }
    else:
        return None

# Example usage:
# repo_info = get_repo_info('octocat', 'Hello-World')
# print(repo_info)