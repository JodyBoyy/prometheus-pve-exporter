from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify, Response
import requests
from flask_httpauth import HTTPTokenAuth
import threading



    
def main():
    app = Flask(__name__)

    auth = HTTPTokenAuth(scheme='Bearer')

    tokens = {
        "secret-token-1": "john",
        "secret-token-2": "susan"
    }

    @auth.verify_token
    def verify_token(token):
        if token in tokens:
            return tokens[token]


    @app.route('/<path:path>', methods=['GET'])
    @auth.login_required
    def proxy(path):
        if auth.current_user():
            resp = requests.get(f'http://127.0.0.1:9221/{path}')
            excluded_headers = []
            headers = [(name, value) for (name, value) in     resp.raw.headers.items() if name.lower() not in excluded_headers]
            response = Response(resp.content, resp.status_code, headers)
            return response
            # requests.get("https://127.0.0.1:9221/metrics")
        else:
            None

    app.run(host="0.0.0.0", port=9222)
