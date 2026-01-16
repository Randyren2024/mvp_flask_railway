from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        "status": "success",
        "message": "Hello, Flask MVP is running!",
        "deployment": "Railway"
    })

if __name__ == '__main__':
    # Railway sets the PORT environment variable
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
