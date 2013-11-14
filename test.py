import unittest
import json
import server

class ServerTest(unittest.TestCase):
    def setUp(self):
        self.app = server.app.test_client()

    def tearDown(self):
        pass

    def test_routing_service_1_recipient(self):
        input_data = {"message": "SendHub Rocks", "recipients": ["412-427-8881"]}
        response = self.app.post(path='/api/sendhub/v1.0/routes', data=json.dumps(input_data), content_type="application/json")
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert response_data is not None
        assert len(response_data['routes']) == 1
        assert response_data['routes'][0]['ip'] == "10.0.1.1"
        assert len(response_data['routes'][0]['recipients']) == 1
        assert response_data['routes'][0]['recipients'][0] == "412-427-8881"
    
if __name__ == '__main__':
    unittest.main()