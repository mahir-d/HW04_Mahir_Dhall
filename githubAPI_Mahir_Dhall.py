"""
Author: Mahir Dhall 
"""
import requests
import json as js


def get_repo_info(user_id: str) -> int:
    """ This function takes in a Github user_id as input to print 
        name of each repositories and their total number of commits in each 
        Attribute:
            user_id: str
        Returns:
            status_code: int
    """
    if type(user_id) != str:
        raise TypeError('Error: user_iduser_id should be of type str')
    if(len(user_id) == 0):
        raise ValueError('Error: user_id should not be an empty string')
    output = requests.get(f"https://api.github.com/users/{user_id}/repos")
    if output.status_code != 200:
        raise ValueError(
            f"{user_id} is not a valid github user id, please check")
    else:
        repo_list = output.json()
        for repo in repo_list:
            repo_name: str = repo['name']
            no_of_commit: int = get_commits(user_id, repo_name)
            print(f"Repo: {repo_name} Number of commits: {no_of_commit}")

        return output.status_code


def get_commits(user_id: str, repo: str) -> int:
    """ This function requests the github API for the information 
        on repositories 
        Attributes:
            user_id: str
            repo: str
        Returns: 
            no_of_commits: int    
    """
    output = requests.get(
        f"https://api.github.com/repos/{user_id}/{repo}/commits")
    commit = output.json()
    return (len(commit))


def get_input() -> None:
    """ This funciton get the input from the user of their github user_id """
    while True:
        try:
            user_id: str = input("Please enter a Github user-ID -> ")
            get_repo_info(user_id)
            break
        except Exception as e:
            print(e)


def main() -> None:
    get_input()


if __name__ == "__main__":
    main()
