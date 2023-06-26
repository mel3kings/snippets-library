# What
- Precommit are commands that run before you commit to git, they can prevent you to commit code that fails unit-tests or are automatically lint.


# How
- run the command below to set where the hooks are located
`git config core.hooksPath hooks`
- ensure that the hooks are executable:
`chmod +x hooks/pre-commit`


# Notes
- the files need a specific naming convention depending on what the stage you want them to run. e.g (`pre-commit`, `pre-push`, see: for all the stages: https://git-scm.com/docs/githooks)

