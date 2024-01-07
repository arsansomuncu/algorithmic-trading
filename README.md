# algorithmic-trading


INSTALLATION GUIDE -> 

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




CONTRIBUTE AND REPORT

# Getting Involved

Thanks for your interest in the project, we'd love to have you involved! Check out the sections below to find out more about what to do next...

## Opening an Issue

We always welcome issues, if you've seen something that isn't quite right or you have a suggestion for a new feature, please go ahead and open an issue in this project. Include as much information as you have, it really helps.

## Making a Code Change

We're always open to pull requests, but these should be small and clearly described so that we can understand what you're trying to do. Feel free to open an issue first and get some discussion going.

When you're ready to start coding, fork this repository to your own GitHub account and make your changes in a new branch. Once you're happy (see below for information on how to run the tests), open a pull request and explain what the change is and why you think we should include it in our project.




