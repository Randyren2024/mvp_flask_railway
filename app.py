from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', 
                           title="Home", 
                           message="Hello, Flask MVP is running!", 
                           platform="Railway (Docker)")

@app.route('/api')
def api_status():
    return jsonify({
        "status": "success",
        "message": "API is working",
        "deployment": "Railway"
    })

if __name__ == '__main__':
    # Railway sets the PORT environment variable
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
