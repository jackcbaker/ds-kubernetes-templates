# Batch Jobs with CronJob

## Introduction

A very common pattern for data science jobs is running a big job regularly at a set time. Some examples:

* A batch `fit` and `predict` algorithm which outputs to a file then picked up by a dashboard.
* An operations research algorithm that that outputs to a database then used by a dashboard.

In the last tutorial we described how jobs work, but we didn't describe how to *trigger* them, i.e. set the running in an automated way.

This tutorial shows how we can set jobs running at regular intervals using a CronJob


## Running example

Let's take a look at the `manifest.yml` for our new example:

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: ds-job
spec:
  schedule: 0 5 * * *
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: ds-job
            image: ds-job
            imagePullPolicy: Never
          restartPolicy: Never
```

Looks very similar to the last example!

The main new addition is the `schedule` field. This indicates how often the job should run in ['`cron`' format](https://www.ibm.com/docs/en/db2oc?topic=task-unix-cron-format).

For our example our job should run at 5am every day.

The other main difference is the definition of our job has been moved to `jobTemplate`.


Similar to before, first we build the image:

```shell
docker build -t ds-job .
```

Then we get this into kubernetes by running

```shell
kubectl apply -f manifest.yml
```

Now rather than the job running immediately, it gets set as a CronJob and is set to run at 5am each day. Let's list the cronjobs we have at the moment

```shell
kubectl get cronjob
```

Output:
```shell
NAME     SCHEDULE    SUSPEND   ACTIVE   LAST SCHEDULE   AGE
ds-job   0 5 * * *   False     0        <none>          7s
```

But I really don't want to get up at 5am to test this job out :(! Luckily to set the job running now you just have to run

```shell
kubectl create job --from=cronjob/ds-job ds-cronjob
```

We can now check the running job in a very similar way to the previous example, the only difference is the job will be called `ds-cronjob` rather than `ds-job`, because that's what we specified in our `kubectl create job` command. So using the commands from before

```shell
kubectl get jobs
```

Expected output:

```shell
NAME         COMPLETIONS   DURATION   AGE
ds-cronjob   0/1           3s         3s
```

```shell
kubectl logs jobs/ds-cronjob
```

Expected output:

```shell
Fitting model...
Training finished with confusion matrix:
[[13  0  0]
 [ 0 15  0]
 [ 0  1  9]]
```
