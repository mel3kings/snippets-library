
# Feature Name: Migrating to Flask from Hasura
Start Date: 2023-05-01

## Summary
This RFC proposes migrating from Hasura to Flask for small scale web queries that require minimal data manipulations while keeping separation of concerns between the web app and Kedro.

## Motivation
Hasura was the quickest way to handle CRUD operations during POC phase given the current timeline, it was a quick and easy way to spin up queries and database. However, as time progressed, more complex queries (multiple joins on different schemas and complex SQL and data manipulation) were not easily accommodated by Hasura. Putting complex data logic in the FE wasn't an option to keep the FE modularized and "dumb". Therefore, migrating to Flask would allow for python-based REST queries that can manipulate DB data without costly subscriptions via Hasura.

## Basic example
Flask is normally used alongside Kedro for small-scale queries. It can be inserted into a new hardened container using established processes.

## Detailed design and Considerations
The migration will involve separating concerns between the web app and Kedro. Flask will be used for small scale web queries that require minimal data manipulations while long running operations will still use Kedro. This will reduce latency since Flask is quicker than Hasura for such tasks.

Hasura currently handles automated database migrations via up and down sql scripts, GraphQL queries for CRUD operators, and subscriptions for listening into Kedro pipeline updates (via listening to table mutations). These features will need to be implemented in Flask as well.

Pros of migrating include reducing latency, reducing complexity of code by separating concerns between web app and Kedro, relatively low risk, and quicker development time.

## Alternatives considered
NoSQL databases like MongoDB were considered but were deemed unsuitable

## Unresolved questions
The extent to which Flask should be used for data manipulation and whether it can handle more complex queries in the future remains an open question. It is also unclear whether Flask can handle automated database migrations via up and down sql scripts, GraphQL queries for CRUD operators, and subscriptions for listening into Kedro pipeline updates as well as Hasura currently does.

## Acknowledgments