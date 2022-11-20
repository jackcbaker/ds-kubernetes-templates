# Data Science Kubernetes Templates

This repo has a collection of kubernetes templates, tutorials and patterns for deploying data science solutions.

## Setup

To run the templates you will need to have docker and kubernetes installed. 

You will also need a working unix shell (e.g. bash, zsh). These come as standard on Mac OS and Linux, but if you're using Windows I recommend installing [Windows Subsystem Linux](https://learn.microsoft.com/en-us/windows/wsl/install).

### Setup using docker desktop

To setup kubernetes on docker desktop:

1. Install docker desktop using [these instructions](https://docs.docker.com/get-docker/).
2. Enable kubernetes on docker desktop by following [these instructions](https://docs.docker.com/desktop/kubernetes/).

Docker desktop requires a [license](https://www.docker.com/pricing/) in a large commercial setting. But docker is standard when creating data science tools so in most companies this should not be a problem.

### Linux alternative setup

For those who use Linux, I find just installing the docker engine and then `minikube` to work well for me, and is a lighter weight, open source alternative. This is not possible in MacOS though. If you go down this route don't forget to get docker to use the [`minikube` cluster when building](https://minikube.sigs.k8s.io/docs/handbook/pushing/#1-pushing-directly-to-the-in-cluster-docker-daemon-docker-env). Else `minikube` won't find any of your docker images.


## The templates

1. **[Job template](https://github.com/jackcbaker/ds-kubernetes-templates/tree/main/1-job)**

Jobs are the basic building plot of most of these templates. This template gets you building and debugging a data science job.

2. **[CronJob template](https://github.com/jackcbaker/ds-kubernetes-templates/tree/main/2-cronJob)**

CronJobs in kubernetes allow you to create batch jobs which run at a regular time.

3. **(Coming Soon) API trigger job**

Trigger a data science pipeline from an API.

4. **(Coming Soon) Deploying an API in Kubernetes**

Deploying an API in Kubernetes that is able to trigger a job.