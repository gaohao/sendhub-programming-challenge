import unittest
import json
import server

class ServerTest(unittest.TestCase):
    def setUp(self):
        self.app = server.app.test_client()

    def tearDown(self):
        pass

    def routing_service_1_recipient(self, p):
        input_data = {"message": "SendHub Rocks", "recipients": ["412-427-8881"]}
        response = self.app.post(path=p, data=json.dumps(input_data), content_type="application/json")
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert response_data is not None
        assert len(response_data['routes']) == 1
        assert response_data['routes'][0]['ip'] == "10.0.1.1"
        assert len(response_data['routes'][0]['recipients']) == 1
        assert response_data['routes'][0]['recipients'][0] == "412-427-8881"
    
    def routing_service_2_recipient(self, p):
        input_data = {"message": "SendHub Rocks", 
                    "recipients": ["412-427-8881", "412-427-8882"]}
        response = self.app.post(path=p, data=json.dumps(input_data), content_type="application/json")
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert response_data is not None
        assert len(response_data['routes']) == 2
        assert response_data['routes'][0]['ip'] == "10.0.1.1"
        assert len(response_data['routes'][0]['recipients']) == 1
        assert response_data['routes'][1]['ip'] == "10.0.1.2"
        assert len(response_data['routes'][1]['recipients']) == 1

    def routing_service_4_recipient(self, p):
        input_data = {"message": "SendHub Rocks", 
                    "recipients": ["412-427-8881", "412-427-8882", 
                                    "412-427-8883", "412-427-8884"]}
        response = self.app.post(path=p, data=json.dumps(input_data), content_type="application/json")
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert response_data is not None
        assert len(response_data['routes']) == 4
        assert response_data['routes'][0]['ip'] == "10.0.1.1"
        assert len(response_data['routes'][0]['recipients']) == 1
        assert response_data['routes'][1]['ip'] == "10.0.1.2"
        assert len(response_data['routes'][1]['recipients']) == 1
        assert response_data['routes'][2]['ip'] == "10.0.1.3"
        assert len(response_data['routes'][2]['recipients']) == 1
        assert response_data['routes'][3]['ip'] == "10.0.1.4"
        assert len(response_data['routes'][3]['recipients']) == 1

    def routing_service_5_recipient(self, p):
        input_data = {"message": "SendHub Rocks", 
                    "recipients": ["412-427-8881", "412-427-8882", 
                                    "412-427-8883", "412-427-8884",
                                    "412-427-8885"]}
        response = self.app.post(path=p, data=json.dumps(input_data), content_type="application/json")
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert response_data is not None
        assert len(response_data['routes']) == 1
        assert response_data['routes'][0]['ip'] == "10.0.2.1"
        assert len(response_data['routes'][0]['recipients']) == 5

    def routing_service_10_recipient(self, p):
        input_data = {"message": "SendHub Rocks", 
                    "recipients": ["412-427-8881", "412-427-8882", 
                                    "412-427-8883", "412-427-8884",
                                    "412-427-8885", "412-427-8886",
                                    "412-427-8887", "412-427-8888",
                                    "412-427-8889", "412-427-8890"]}
        response = self.app.post(path=p, data=json.dumps(input_data), content_type="application/json")
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert response_data is not None
        assert len(response_data['routes']) == 1
        assert response_data['routes'][0]['ip'] == "10.0.3.1"
        assert len(response_data['routes'][0]['recipients']) == 10

    def routing_service_17_recipient(self, p):
        input_data = {"message": "SendHub Rocks", 
                    "recipients": ["412-427-8881", "412-427-8882", 
                                    "412-427-8883", "412-427-8884",
                                    "412-427-8885", "412-427-8886",
                                    "412-427-8887", "412-427-8888",
                                    "412-427-8889", "412-427-8890",
                                    "412-427-8891", "412-427-8892",
                                    "412-427-8893", "412-427-8894",
                                    "412-427-8895", "412-427-8896",
                                    "412-427-8897"]}
        response = self.app.post(path=p, data=json.dumps(input_data), content_type="application/json")
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert response_data is not None
        assert len(response_data['routes']) == 4
        assert response_data['routes'][0]['ip'] == "10.0.3.1"
        assert len(response_data['routes'][0]['recipients']) == 10
        assert response_data['routes'][1]['ip'] == "10.0.2.1"
        assert len(response_data['routes'][1]['recipients']) == 5
        assert response_data['routes'][2]['ip'] == "10.0.1.1"
        assert len(response_data['routes'][2]['recipients']) == 1
        assert response_data['routes'][3]['ip'] == "10.0.1.2"
        assert len(response_data['routes'][3]['recipients']) == 1

    def routing_service_25_recipient(self, p):
        input_data = {"message": "SendHub Rocks", 
                    "recipients": ["412-427-8881", "412-427-8882", 
                                    "412-427-8883", "412-427-8884",
                                    "412-427-8885", "412-427-8886",
                                    "412-427-8887", "412-427-8888",
                                    "412-427-8889", "412-427-8890",
                                    "412-427-8891", "412-427-8892", 
                                    "412-427-8893", "412-427-8894",
                                    "412-427-8895", "412-427-8896",
                                    "412-427-8897", "412-427-8898",
                                    "412-427-8899", "412-427-8900",
                                    "412-427-8901", "412-427-8902", 
                                    "412-427-8903", "412-427-8904",
                                    "412-427-8905"]}
        response = self.app.post(path=p, data=json.dumps(input_data), content_type="application/json")
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert response_data is not None
        assert len(response_data['routes']) == 1
        assert response_data['routes'][0]['ip'] == "10.0.4.1"
        assert len(response_data['routes'][0]['recipients']) == 25

    def test_greedy_routing_service_1_recipient(self):
        self.routing_service_1_recipient('/v1.0/greedy_routes')

    def test_greedy_routing_service_2_recipient(self):
        self.routing_service_2_recipient('/v1.0/greedy_routes')

    def test_greedy_routing_service_4_recipient(self):
        self.routing_service_4_recipient('/v1.0/greedy_routes')

    def test_greedy_routing_service_5_recipient(self):
        self.routing_service_5_recipient('/v1.0/greedy_routes')

    def test_greedy_routing_service_10_recipient(self):
        self.routing_service_10_recipient('/v1.0/greedy_routes')

    def test_greedy_routing_service_17_recipient(self):
        self.routing_service_17_recipient('/v1.0/greedy_routes')

    def test_greedy_routing_service_25_recipient(self):
        self.routing_service_25_recipient('/v1.0/greedy_routes')

    def test_dynamic_routing_service_1_recipient(self):
        self.routing_service_1_recipient('/v1.0/dynamic_routes')

    def test_dynamic_routing_service_2_recipient(self):
        self.routing_service_2_recipient('/v1.0/dynamic_routes')

    def test_dynamic_routing_service_4_recipient(self):
        self.routing_service_4_recipient('/v1.0/dynamic_routes')

    def test_dynamic_routing_service_5_recipient(self):
        self.routing_service_5_recipient('/v1.0/dynamic_routes')

    def test_dynamic_routing_service_10_recipient(self):
        self.routing_service_10_recipient('/v1.0/dynamic_routes')

    def test_dynamic_routing_service_17_recipient(self):
        self.routing_service_17_recipient('/v1.0/dynamic_routes')

    def test_dynamic_routing_service_25_recipient(self):
        self.routing_service_25_recipient('/v1.0/dynamic_routes')

    def test_routing_service_duplicated_recipient(self):
        input_data = {"message": "SendHub Rocks", "recipients": ["412-427-8881", "412-427-8881"]}
        response = self.app.post(path='/v1.0/greedy_routes', data=json.dumps(input_data), content_type="application/json")
        assert response.status_code == 400

    def test_routing_service_invalid_url(self):
        invalid_url = '/v1.0/route'
        input_data = {"message": "SendHub Rocks", "recipients": ["412-427-8881"]}
        response = self.app.post(path=invalid_url, data=json.dumps(input_data), content_type="application/json")
        assert response.status_code == 404

    def test_routing_service_bad_json_schema(self):
        input_data = {"messages": "SendHub Rocks", "recipients": ["412-427-8881"]}
        response = self.app.post(path='/v1.0/greedy_routes', data=json.dumps(input_data), content_type="application/json")
        assert response.status_code == 400

if __name__ == '__main__':
    unittest.main()