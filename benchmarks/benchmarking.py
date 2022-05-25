from locust import FastHttpUser, task, constant
import json
import time
import random


class benchmarking(FastHttpUser):
    wait_time = constant(1)

    def __init__(self, *args, **kwargs):
        time.sleep(random.randint(0, 5))
        super().__init__(*args, **kwargs)

    @task
    def test_home(self):
        self.client.get('')

    @task
    def test_api_paste(self):
        payload = {
            "title": "My New paste",
            "content": "GGWP"
        }
        headers = {'content-type': 'application/json'}

        self.client.post("/api/paste", data=json.dumps(payload), headers=headers)

    # @task
    # def test_id(self):
    #    for user_id in range(500):
    #        self.client.get(f'/api/?userId={user_id}', name='/api')

    @task
    def test_api_recents(self):
        self.client.post('/api/recents', "")
