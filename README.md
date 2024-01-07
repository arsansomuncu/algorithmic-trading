# algorithmic-trading


Installation instructions -> 

Global setup:
  Download and install Git
  git config --global user.email EMAIL_ADDRESS
      
Next steps:
  mkdir PROJECT_NAME
  cd PROJECT_NAME
  git init
  touch README
  git add README
  git commit -m 'first commit'
  git remote add origin git@github.com:USER/PROJECT_NAME.git
  git push origin master
      
Existing Git Repo?
  cd existing_git_repo
  git remote add origin git@github.com:USER/PROJECT_NAME.git
  git push origin master

You may also want to track the master branch for easy pull/push
  git config branch.master.merge refs/heads/master
  git config branch.master.remote origin






