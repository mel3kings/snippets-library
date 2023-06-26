
# What
- Heroku is a IaaS that enables quick deployment for simple containers called 'dynos'
- The two files are examples of what are needed in your repository for heroku. 
    - Procfile - command for heroku to execute
    - runtime.txt - what your application runtime looks like

# Installations
- install heroku-cli
```brew tap heroku/brew && brew install heroku```
- login
```heroku login```


# Create dyno
- run this in a git repository:
```heroku create```
- this will create heroku app url and heroku git url for automated CiCD.


# Ops
`heroku logs --tail`
# Update
```git push heroku main```



# Tutorials:

https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true

