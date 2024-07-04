from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while n > 0:
        digit = n % 10
        sum += digit ** order
        n = n // 10

    if sum == copy_n:
        result = {
            "number": copy_n,
            "Armstrong": True,
            "server IP": "122.234.213.53"
        }
    else:
        result = {
            "number": copy_n,
            "Armstrong": False,
            "server IP": "122.234.213.53"
        }
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
#Run the Flask application by executing python main.py in your terminal.
#Open your web browser and navigate to http://127.0.0.1:8000/armstrong/<number>
# (replace <number> with the actual number you want to check).