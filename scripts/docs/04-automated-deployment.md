
# Feature Name: Automated Deployment to PRN/SRN
Start Date:
## Summary
This RFC proposes the automation of the deployment process to Production Ready Network (PRN) and Secure Ready Network (SRN) environments, with the goal of minimizing downtime and reducing errors from manual steps. The current deployment process involves multiple manual steps and takes 10-20 minutes, resulting in application downtime.

## Motivation
The current deployment process is reliant on one engineer and involves multiple manual steps, resulting in longer release cycles and increased risk of errors. By automating the deployment process, we can enable anyone to deploy, reduce downtime, increase release frequency, and allow more time for developing software.

## Basic example
The current interim solution is a cronjob that pulls a certain tag into deployment environments. However, we aim to fully automate the deployment process in PRN/SRN if possible. We will need to minimize manual steps in the deployment process by adjusting image tags for each service automatically based on Bamboo build numbers. 

## Detailed design and Considerations
- We will need to use tools that do not require orchestration tooling such as k8s or docker swarm due to client intervention constraints. We are also unsure if the environment can handle such tools due to hardened containers and client scanning requirements.
- Deployment to PRN and SRN is the same, except for the data.

## Alternatives considered
N/A

## Prior art
N/A

## Unresolved questions
- We are unsure yet how to rollback if the team wants to rollback to a certain version of the application due to the automation proposal.
- Currently only setup in PRN