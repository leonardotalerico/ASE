import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2) # 1-2 seconds between simulated events

    @task # defines a user task, asssociated to a microthread by locust
    def index_page(self):
        self.client.get("/") # get home page

    @task(3) # this task is 3 times likelier than the previous!
    def view_item(self):
        for item_id in range(10):
            self.client.get(f"/calc/sum?m={item_id}&n={42}", name="/calc/sum")
            time.sleep(1)

    def on_start(self): # init for each virtual user
         pass