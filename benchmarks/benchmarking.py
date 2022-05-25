from locust import FastHttpUser, task, SequentialTaskSet
import json
import time
import random


class benchmarking(FastHttpUser):

    # @task
    # def test_home(self):
    #    self.client.get('')

    # @task
    # def test_api_paste(self):
    #    payload = {
    #        "title": "My New paste",
    #        "content": "GGWP"
    #    }
    #    headers = {'content-type': 'application/json'}
    #
    #    self.client.post("/api/paste", data=json.dumps(payload), headers=headers)

    #@task
    #def test_id(self):
    #    self.client.get('/api/1')


    @task
    def test_api_recents(self):
        self.client.post('/api/recents', "")
