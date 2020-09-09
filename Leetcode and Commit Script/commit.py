from git import Repo

path = "D:\\Personal\\Leetcode"
repo = Repo(path)

untrackedFiles = repo.untracked_files
commitMessage = untrackedFiles[0].split("/")[0]
print(commitMessage)
repo.index.add(untrackedFiles)
repo.index.commit(commitMessage)
repo.remotes.origin.push()