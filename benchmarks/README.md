# Run benchmark via Locust.io

## Make sure all kubernetes pods are running

### Change current working directory to benchmarks 
```
cd benchmarks
```

### Run the Locust
```
locust -H http://127.0.0.1 -f benchmarking.py -u 20 -r 1 benchmarking
```

### Check benchmark at
```
localhost:8089
```

