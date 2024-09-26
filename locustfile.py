from locust import HttpUser, task


# このテストシナリオのユーザーは、`/hello`にHTTPリクエストし、次に`/world`にHTTPリクエストし、それを繰り返します。
class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")
