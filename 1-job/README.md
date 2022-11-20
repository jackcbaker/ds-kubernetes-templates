# Kubernetes Jobs

## Introduction

Jobs are the main tool to use for 'batch processing jobs'. In other words, anything that is expected to require a considerable amount of compute to run should be run in a job. 

They will form the base for most of the other examples in this repo.

Examples include: a data science `fit` pipeline; a data science batch `predict` pipeline; an operational research/combinatorial optimisation pipeline.

Jobs normally take a while to spin up, so a common example where you wouldn't want to use a job is a simple data science `predict` function (commonly referred to as model serving). This would normally be put directly into an API for easy access and quick response.

### Advantages

The advantages of jobs is that, while they take a little while to spin-up, they do not use any resources until they are required to be used. Therefore rather than having to keep a big server alive to complete your `fit` jobs, which typically don't get run very often; you can just spin it up as and when needed.

## Running example


First build the docker image from your terminal using:

```shell
docker build -t ds-job .
```

`manifest.yml` is a file in the standard YAML format that tells kubernetes how to run a given image. The output for our example is below:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: ds-job
spec:
  template:
    spec:
      containers:
      - name: ds-job
        image: ds-job
        imagePullPolicy: Never
      restartPolicy: Never
```

Manifest files look a bit confusing at first, and most of the time I find myself looking at examples on the kubernetes documentation, copying and pasting it, and then changing the salient points for my usecase.

To explain this file a bit we've defined that kubernetes should run the image `ds-job` as a kubernetes job. It specifies to run the `ds-job` image in the `containers` part. The `imagePullPolicy` ensures that kubernetes will always take the image from our local machine.

To run this job we simply run from our terminal:

```shell
kubectl apply -f manifest.yml
```

This will run the `CMD` part of our docker container. To view your currently running jobs run

```shell
kubectl get jobs
```

The output should look something like this:

```shell
NAME     COMPLETIONS   DURATION   AGE
ds-job   0/1           3s         3s
```

You should see a `ds-job` here, which is what we defined as the job name in `manifest.yml`.

To view the output of our job, we run

```shell
kubectl logs jobs/ds-job
```

This should show the print statements as `main.py` is executed in the docker container. E.g.

```shell
Fitting model...
Training finished with confusion matrix:
[[13  0  0]
 [ 0 15  0]
 [ 0  1  9]]
```

The job runs in a kubernetes concept known as a `pod`. This is similar to the concept of a container in `docker`. It is essentially the smallest component of kubernetes, and is where all the compute actually happens. To view the pod being booted up run

```shell
kubectl get pods
```

Output:
```shell
NAME           READY   STATUS      RESTARTS   AGE
ds-job-zzxbn   0/1     Completed   0          76s
```

This job will not disappear when it has finished. Which is useful for us while we're learning. To delete it when you're finished run:

```shell
kubectl delete jobs/ds-job
```

In practice, you often do want your jobs to disappear after some time. To do this set the 'time-to-live' using `ttl:` in the manifest. Read more [here](https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished/).


# Further reading

* Once you get used to it, the kubernetes documentation is excellent. This is the [page on jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/).