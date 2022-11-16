from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import random


from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.f0tzkg6.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)

db = client.dbsparta





@app.route('/')
def home():
    return render_template('index2.html')



@app.route("/api/post", methods=["GET"])
def Diary_get():
    diary_list = list(db.Diary.find({}, {'_id':False}))
    return jsonify({'Diary':diary_list})



@app.route("/comment", methods=["GET"])
def web_comment_get():
    num_receive = request.args.get('num_give')
    comment_list = list(db.comment.find({"num":num_receive}, {'_id': False}))
    return jsonify({'comments': comment_list})





if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)









