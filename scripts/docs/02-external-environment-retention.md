# Feature Name: McKinsey Environment Retention
Start Date: 2023-02-09
RFC PR:
## Summary
This RFC explores the options for retaining or fully migrating from the McKinsey Environment in light of the need for 2-way communications to the database.

## Motivation
During the initial stages of development, the frontend was developed using static data outside the client network.
As the application matures, it is necessary to have 2-way communications with the database but given client sensitivities prevented us from just building outside client network.
This has raised questions about the viability of retaining or fully migrating from the McKinsey Environment.

## Basic example
Solution Option 1: Remove McKinsey environment.
This solution would result in a loss of a staging environment, which would slow down response times for issue fixes and prevent demoing to potential new clients.

Solution Option 2: Deploy DB to platform McKinsey.
This solution would allow an automation-first approach for new deployments, reduce complexity of code base, and provide a full-featured demo system to clients. However, it would require effort to implement and maintain.

Solution Option 3: Retain and mock out 2-way communications with DB.
This solution would require development time to create and maintain mocks and separate code paths, which may be greater than just deploying the backend.

## Detailed design and Considerations
The team has opted to completely remove the ability to develop outside of client infrastructure due to several reasons:
- There is no easy way to sync code from mck/public network into client network. The current process was to request sync from a DevSecOps contact person with the client, which was becoming a bottleneck due to deployment speed and availability of contact person.
- It constituted double work for bug fixes only found inside the client network, meaning work inside the network had to be manually transcribed outside.
- The sensitivities of client data prevent simulation of web with close-to-production data.
- These problems compounded each other and became more of a bottleneck.

## Alternatives considered
None.

## Prior art
None.

## Unresolved questions
How do we enable non-cleared engineers to develop now?