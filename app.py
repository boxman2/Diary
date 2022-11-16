from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.zhmj7xm.mongodb.net/AtlasCluster?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/post", methods=["POST"])
def diary_post():
    num_receive = request.form['num_give']
    date_receive = request.form['date_give']
    id_receive = request.form['id_give']
    title_receive = request.form['title_give']
    state_receive = request.form['state_give']
    isSecret_receive = request.form['isSecret_give']
    write_receive = request.form['write_give']
    like_receive = request.form['like_give']
    img_receive = request.form['img_give']

    doc = {
        'num': num_receive,
        'date': date_receive,
        'id': id_receive,
        'state': state_receive,
        'title': title_receive,
        'write': write_receive,
        'isSecret': isSecret_receive,
        'like': like_receive,
        'img': img_receive
    }
    db.user.insert_one(doc)
    return jsonify({'msg': '일기 끝!'})

@app.route("/post", methods=["GET"])
def diary_get():
    diary_list = list(db.user.find({}, {'_id': False}))
    return jsonify({'diary':diary_list, 'msg': 'Hi'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)