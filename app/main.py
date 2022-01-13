from flask import Flask, jsonify, request
from parser import parse

app=Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def hello():
    if request.method=='GET':
        return '<h5> Server Started </h5>'
    else:
        resume=request.files['resume']
        json=parse(resume)
        return jsonify(json)

