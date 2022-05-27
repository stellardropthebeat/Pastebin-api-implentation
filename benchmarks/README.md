# Run benchmark via Locust.io

## Make sure all kubernetes pods are running

### Change current working directory to benchmarks 
```
cd benchmarks
```

### Run the Locust 1 /api per run
```
locust -H http://127.0.0.1 -f benchmarking.py -u 100 -r 10 benchmarking
```
This benchmark at localhost. Inside the benchmark file will have each /api test.

When benchmarking, comment out others /api and test it once for best efficiency.

-u 100 : Test 100 users (Peak Concurrency)

-r 10: At the increasing rate of 10

-benchmarking is the class of benchmarking.py file

### Check benchmark at
```
localhost:8089
```

Criteria: 

- Reach 500 rps (500 requests per second). This mean the backend can handle 

a bunch of request in a period of time

- No failure is detected (0% failure)

