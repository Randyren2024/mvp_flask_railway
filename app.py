import os
import logging
from flask import Flask, jsonify

# 配置基础日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def hello_world():
    logger.info("Index route accessed")
    return jsonify({
        "status": "success",
        "message": "Hello, Flask MVP is running!",
        "deployment": "Railway (Docker)",
        "env": {
            "PORT": os.environ.get('PORT', 'Not Set'),
            "NODE_NAME": os.environ.get('RAILWAY_NODE_NAME', 'Unknown')
        }
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"Starting app on port {port}")
    app.run(host='0.0.0.0', port=port)
