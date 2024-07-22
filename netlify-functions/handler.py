from flask import Flask, jsonify, send_from_directory
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/api/data')
def api_data():
    return jsonify({"message": "Hello from Flask on Netlify!"})

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

def handler(event, context):
    def application(environ, start_response):
        environ['flask.request'] = request
        return DispatcherMiddleware(app, { '/': app })(environ, start_response)

    return Response(application(event, context))
