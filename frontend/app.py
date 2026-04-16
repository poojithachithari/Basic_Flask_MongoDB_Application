from flask import Flask,render_template,request
import requests

BACKEND_URL = 'http://0.0.0.0:9000'
app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
