# What?
- Prettier fixes code formatting and standardizes code standard

# How?
- install prettier in your project:
`npm install --save-dev --save-exact prettier`
- create empty config
`echo {}> .prettierrc.json`
-  create prettier ignore to ignore some folders on your project
```shell
echo '# Ignore artifacts:
build
coverage' > .prettierignore
```