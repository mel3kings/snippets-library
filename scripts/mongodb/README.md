## Mongo

### Local
- after running docker compose you can access:
`http://localhost:8081`

- URL String:
`mongodb://localhost:27017/<db_name>`

### CRUD
- Insert:
```
db.<db_name>.insertOne({

})
```

- delete all:
```
db.<name>.deleteMany({})
```

- select:
```
db.<name>.find().pretty();
```