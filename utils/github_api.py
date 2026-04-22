import requests

def get_repo_info(owner: str, repo: str, token: str) -> dict:
    """获取GitHub仓库基本信息

    Args:
        owner (str): 仓库所有者
        repo (str): 仓库名称
        token (str): GitHub个人访问令牌

    Returns:
        dict: 包含star_count、fork_count、description的字典

    Raises:
        Exception: 当API请求失败时
    """
    url = f'https://api.github.com/repos/{owner}/{repo}'
    headers = {'Authorization': f'token {token}'}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            'star_count': data['stargazers_count'],
            'fork_count': data['forks_count'],
            'description': data['description']
        }
    except requests.exceptions.RequestException as e:
        raise Exception(f'GitHub API请求失败: {str(e)}')
