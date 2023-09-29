import git

# remote repo and local repo
repo_url = 'https://github.com/sky2626/automation.git'
repo_path = '/mnt/c/Users/Ma Guy/Desktop/git-repos/automation'

# intialize the git repo object
repo = git.Repo(repo_path)

try:
    # ad all changes to the index
    repo.index.add('*')

    # commit changes
    commit_massage = 'update'
    repo.index.commit(commit_massage)

    # push changes
    origin = repo.remote(name='origin')
    origin.push()
    print(f'Code successfully push to {repo_url}')

except Exception as e:
    print(f'an error occurred: {str(e)}')
