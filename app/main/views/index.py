from flask import render_template, request, Response, json
import os
from app.main import main
from werkzeug.utils import secure_filename
from app.models import Book


@main.route("/", methods=['GET'])
def index():
    return render_template('main/index.html')


@main.route("/upload_image", methods=['POST', 'OPTIONS'])
def upload():
    if request.method == 'POST':
        image = request.files['analysis_image']
        if image:
            filename = secure_filename(image.filename)
            image.save(os.path.join('app/static/upload/', filename))
        print filename
        tmp = [
            {
                "description": "white",
                "score": 0.9355741
            },
            {
                "description": "black and white",
                "score": 0.9302869
            },
            {
                "description": "photograph",
                "score": 0.9293675
            },
            {
                "description": "black",
                "score": 0.92929024
            },
            {
                "description": "monochrome photography",
                "score": 0.7750446
            },
            {
                "description": "monochrome",
                "score": 0.7387478
            },
            {
                "description": "silhouette",
                "score": 0.6257669
            },
            {
                "mid": "/m/01cd9",
                "description": "brand",
                "score": 0.5969167
            },
            {
                "description": "illustration",
                "score": 0.5436892
            }]
        print request.method
        response = Response(json.dumps(tmp), status=200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Methods'] = '*'
        return response
    else:
        response = Response(status=200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Methods'] = '*'
        return response


@main.route("/upload_images", methods=['POST', 'OPTIONS'])
def upload_multiple():
    if request.method == 'POST':
        print type(request.files)
        image = request.files['analysis_image']
        if image:
            filename = secure_filename(image.filename)
            image.save(os.path.join('app/static/upload/', filename))
        print filename
        tmp = [{
            "description": "brand",
            "score": 0.5969167
        },
            {
                "description": "illustration",
                "score": 0.5436892
            }]
        print request.method
        response = Response(json.dumps(tmp), status=200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Methods'] = '*'
        return response
    else:
        response = Response(status=200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Methods'] = '*'
        return response
