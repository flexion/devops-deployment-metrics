# devops-deployment-metrics

An application that generates DevOps deployment metrics from GitHub repositories using a GitHub Action workflow to deploy a product.

## Three deployment metrics

This application reads historical data for workflows from GitHub. The application looks at records for the deployment workflow
and generates Deployment Frequency, Change Fail Percentage and a Mean Time to Recover metrics for fixed-width reporting periods.

Metrics will be reported from a configured starting time to the present, with results reported in fixed-width periods.
The reporting period width is configurable from 1 day on up.

### Deployment Frequency

Deployment Frequency is a simple calculation of the number of deployments per day in the reporting period. For example,
if there is a 14-day reporting period, and there are 28 deployments by the workflow during that period, the deployment
frequency would be 2.0.

### Change Fail Rate

Change Fail Rate is a simple ratio of the number of failed deployments over the total number of deployments in a given
reporting period. If all the deployments fail, the change fail rate will be 1.0. If all the deployments succeed,
the change fail rate will be 0.0.

### Mean Time to Recover

The deployment Mean Time to Recover (MTTR) mean of the deployment time-to-recover in a given reporting period.
The deployment time-to-recover is the time between a failed deployment and the next successful deployment. The
metric is reported in hours.
