# Feature Name: Buy or Build Custom UI Components for Complex Gantt Charts
Start Date: N/A
RFC PR: N/A

## Summary
This RFC proposes the development of custom UI components for complex Gantt charts to replace the current Frappe Gantt chart that is causing performance issues.

## Motivation
The current Frappe Gantt chart is causing performance issues, and we need to choose a new Gantt Chart. We want to develop custom UI components for complex Gantt charts because it will allow us to have better control over the design and functionality of the chart, and we can tailor it specifically to our needs.

## Basic example
We will choose between building the chart manually using CSS or by using a commercial off-the-shelf (COTS) chart solution like HighCharts. We will analyze what is possible with the chosen solution, including checkboxes, Christmas tree display, "Units-delivered-projectioner" slider button alignment with years in chart, and other requirements.

QB Components: We have access to Gantt styling resources from QB resources like Laleh Omolaki, Joseph Perkins, and Dan Dumitriu. Dan and Joseph have been approached regarding Javascript/React resources, and we are awaiting their response.

## Detailed design and Considerations
We will consider whether to build or buy a solution. If we decide to build a custom solution, developers will need to manually insert and align every single line, rectangle, and text element. Provision for happy path and all the edge cases that arise will also need to be provided along with hover support. Additionally, we will need to provide lifetime support for our custom solution.

If we decide to use a COTS solution like HighCharts, we can get something working quickly with high performance and no bugs. However, there may be limitations in replicating high fidelity designs.

## Alternatives considered
Other COTS solutions were considered but ultimately HighCharts was chosen due to its reputation for performance and broad feature set.

## Prior art
N/A

## Unresolved questions
None at this time.

Acknowledgments: N/A