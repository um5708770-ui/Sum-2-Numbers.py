from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.json
    a = data.get("a", 0)
    b = data.get("b", 0)
    result = a + b
    return jsonify({"sum": result})

@app.get("/")
def home():
    return "Sum API is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
