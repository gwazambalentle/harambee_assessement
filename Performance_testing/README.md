# E-Commerce performance testing
This project design and implement a basic performance test to simulate user behaviour for browsing product categories

## Test Scenarios
1. User login
2. Browse Products

## Running Tests
locust -f locustfile.py --headless -u {number of users} -r {ramp up} -t {Seconds}s --host https://petstore.swagger.io/ --csv performance_stats
