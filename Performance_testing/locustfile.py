import random
from locust import HttpUser, task, between

class BrowserUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def login(self):
        with self.client.get("https://petstore.swagger.io/v2/user/login?username=mbalentle&password=mbali", catch_response=True) as response:
            if response.status_code != 200:
                print
                response.failure("Login failed")
            else:
                response.success()
                

    @task
    def browser_category(self):
        category = ["available", "pending", "sold"]
        selected = random.choice(category)
        # Simulate browsing a category
        with self.client.get(f"https;//petstore.swagger.io/v2/pet/findByStatus?status={selected}", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Failed to browse category {category}")
            else:
                response.success()
       

    