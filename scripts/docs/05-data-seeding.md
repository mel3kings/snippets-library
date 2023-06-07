# Feature Name: Automated Data Seeding
Start Date: TBD
RFC PR: TBD

## Problem to Solve
How do we minimize manual intervention on each VM? How do we manage multiple environments? What are the multiple environments?
- 2 x different classification levels (protected, secret)
- 2 x desployments (staging, uat)

## Hypothesis
The best way to automate is to disable Hasura Console. All DB schema, Hasura API metadata, and initial seed data is codified for automated initial deployment. Maintenance of environments - all changes will need a PR on the Hasura codebase after running console locally. A Pgadmin page will still exist to manage DB data insertions (i.e., to physically get data into secret). Single user access only. As a debugging tool, it's super useful.

## Solution Overview
- Seed data pipeline engine - how does that fit into the picture?
- All DB schema, Hasura API metadata and initial seed data is codified for automated initial deployment.
- A Pgadmin page will still exist to manage DB data insertions (i.e., to physically get data into secret). Single user access only.

## Shared Responsibility
Data seeding is a shared responsibility between the SE and DS/DE Team.
- Whenever a server is rebuilt after a failure, the database is empty and needs to be re-applied.

## Data Seeding Best Practices
- Get metrics out of the model automatically.
- Data versioning?
- Model repository / versioning / roll back.
- Tag your images?
- Deployment Pipeline should fail if the model doesn't operate correctly.

## Unresolved Questions
None at this time.

## Acknowledgments
None at this time.