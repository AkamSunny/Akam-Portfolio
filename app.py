from flask import Flask, render_template, jsonify
import os
from datetime import datetime



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/health')
def health_check():
    return jsonify({
        'status': 'OK', 
        'timestamp': datetime.utcnow().isoformat(),
        'message': 'Portfolio is running'
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)