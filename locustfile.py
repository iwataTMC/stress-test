from locust import HttpUser, TaskSet, task, between, constant

class UserBehavior(TaskSet):

    @task(1)
    def search(self):
        self.client.get("/api/t******-bo***", verify=False)

class WebsiteUser(HttpUser):

    tasks = {UserBehavior:1}
    wait_time = constant(0)
    
