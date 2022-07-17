# Hasura
## Hasura-CLI
install hasuri-cli to automatically manage migrations/scripts
```shell
brew install hasura-cli
```

## Scripts
Prerequisites:
- assuming you have the correct `config.yaml file` (change admin secret)
- assuming you are in `hasura-server` folder (`cd hasura-server`)
- Change to the correct values

## Create migration script from existing Schema (will generate `up.sql`)
``` shell
hasura migrate create init --from-server --schema <SCHEMA_NAME>
```

## Create Seed scirpt from existing Tables (This will generate insert scripts for existing data)
``` shell
hasura seeds create initial_data --from-table <TABLE_NAME>

```

## Export DB Metadata
``` shell
hasura metadata export
```


## Apply migrations and seeds (Run this if you have migrations/seeds that are pending)
- To see if you have pending migration run `hasura migrate status`

``` shell
 hasura migrate apply --skip-execution --database-name default 
 hasura seeds apply
```