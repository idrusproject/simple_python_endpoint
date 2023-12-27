from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route for the root URL
@app.route('/')
def home():
    return 'Hello, this is the home page!'

# Route for handling HTTP POST requests
@app.route('/api/post_example', methods=['POST'])
def post_example():
    # Get data from the request
    data = request.json  # Assuming the data is sent as JSON in the request body

    # Process the data (you can perform any operations here)
    result = {"message": "Received data successfully", "data": data}

    # Return a JSON response
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='192.168.100.21', port=5000, debug=True)