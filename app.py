from flask import Flask, jsonify, render_template, request
import json
import unicodedata
from brain import best_move
import os

app = Flask(__name__)


def helper(arr):
    return map(lambda x : unicodedata.normalize('NFKD', x).encode('ascii','ignore'), arr)

def transform(arr):
    return map(lambda x : 1 if x == 'X' else (None if len(x) == 0 else 0), arr)

def convert(tup):
    return str((tup[0] * 3) + 1 + tup[1])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ["POST"])
def process():
    data =  json.loads(request.form.keys()[0])['x']
    data = map(helper , data)
    data = map(transform, data)

    ans = convert(best_move(data))
    return ans
