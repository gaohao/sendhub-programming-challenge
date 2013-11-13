from flask import Flask, request, jsonify
from jsonschema import validate

app = Flask(__name__)

schema = {
    "title": "SendHub Challenge Schema",
    "type": "object",
    "properties": {
        "message": {
            "type": "string"
        },
        "recipients": {
            "type": "array",
            "minItems": 1,
            "items": {"type": "string"},
            "uniqueItems": True
        }
    },
    "required": ["message", "recipients"]
}

table = {
    'small': {'category_name': 'Small', 'ip_subnets': '10.0.1.', 'throughput': 1, 'cost': 0.01},
    'medium': {'category_name': 'Medium', 'ip_subnets': '10.0.2.', 'throughput': 5, 'cost': 0.05},
    'large': {'category_name': 'Large', 'ip_subnets': '10.0.3.', 'throughput': 10, 'cost': 0.1},
    'super': {'category_name': 'Super', 'ip_subnets': '10.0.4.', 'throughput': 25, 'cost': 0.25},
}

categories = ['super', 'large', 'medium', 'small']

@app.route('/')
def hello():
    return 'Demo for sendhub coding challenge!'

@app.route('/api/sendhub/v1.0/routes', methods=['POST'])
def routing_service():
    data = request.json
    validate(data, schema)
    recipients = data['recipients']
    recipients_num = len(recipients)
    routes = []
    start = 0
    for i in range(len(categories)):
        requests_needed = recipients_num / table[categories[i]]['throughput']
        if requests_needed > 0:
            for j in range(1, requests_needed + 1):
                ip = table[categories[i]]['ip_subnets'] + str(j)
                end = start + table[categories[i]]['throughput']
                routes.append({'ip': ip, 'recipients': recipients[start : end]})
                start = end
        recipients_num = recipients_num % table[categories[i]]['throughput']
    return jsonify({'message': 'SendHubRocks', 'routes': routes})

if __name__ == '__main__':
    #app.run(debug=True)
    pass