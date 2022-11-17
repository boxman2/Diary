from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca=certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.zhmj7xm.mongodb.net/AtlasCluster?retryWrites=true&w=majority')
db = client.dbsparta

SECRET_KEY = 'HANGHAE1'

import jwt

import datetime

import hashlib

@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.register.find_one({"id": payload['id']})

        return render_template('list.html', id=user_info["id"])
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

@app.route('/write')
def write():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.register.find_one({"id": payload['id']})

        return render_template('write.html', id=user_info["id"])
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

@app.route('/secret')
def secret():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.register.find_one({"id": payload['id']})

        return render_template('secret.html', id=user_info["id"])
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))
@app.route('/comment', methods=['POST'])
def web_comment_post():
    comment_receive = request.form['commentContent_give']
    ID_receive = request.form['ID_give']
    num_receive = request.form['num_give']

    doc = {"comment":comment_receive, "id":ID_receive, "num":num_receive}
    db.comment.insert_one(doc)
    return jsonify({'msg':'코멘트 완료!'})

@app.route("/comment", methods=["GET"])
def web_comment_get():
    num_receive = request.args.get('num_give')
    comment_list = list(db.comment.find({"num":num_receive}, {'_id': False}))
    return jsonify({'comments': comment_list})

@app.route("/user", methods=["GET"])
def web_users_get():
    user_list = list(db.user.find({"isSecret":"true"}, {'_id': False}))
    return jsonify({'user': user_list})
@app.route('/like', methods=['POST'])
def web_users_post():
    id_receive=request.form['id_give']
    like_receive = request.form['like_give']
    num_receive = request.form['num_give']

    if db.like.find_one({'num': num_receive,'id':id_receive},{'_id': False}) is None :
        print('성공')
        doc = {"id":id_receive, "num":num_receive}
        db.like.insert_one(doc)
        db.user.update_one({'num': num_receive}, {'$set': {'like': int(like_receive)+1}})
        return jsonify({'msg':'완료'})
    else :
        print('실패')
        print(db.like.find_one({'num': num_receive,'id':id_receive}))
        return jsonify({'msg':'이미 누르셨습니다!'})



# 여기서부터는 로그인이랑 연동하기 ####################################
@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/api/register', methods=['POST'])
def api_register():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    nickname_receive = request.form['nickname_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    db.register.insert_one({'id': id_receive, 'pw': pw_hash, 'nick': nickname_receive})

    return jsonify({'result': 'success'})

@app.route('/api/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    # 회원가입 때와 같은 방법으로 pw를 암호화합니다.
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    # id, 암호화된pw을 가지고 해당 유저를 찾습니다.
    result = db.register.find_one({'id': id_receive, 'pw': pw_hash})

    # 찾으면 JWT 토큰을 만들어 발급합니다.
    if result is not None:
        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=5)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        # token을 줍니다.
        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

    #####애경님 코드#########################################

@app.route('/post', methods=['POST'])
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

@app.route("/api/post", methods=["GET"])
def Diary_get():
    diary_list = list(db.user.find({}, {'_id':False}))
    return jsonify({'Diary':diary_list})



# @app.route("/comment", methods=["GET"])
# def web_comment_get():
#     num_receive = request.args.get('num_give')
#     comment_list = list(db.comment.find({"num":num_receive}, {'_id': False}))
#     return jsonify({'comments': comment_list})

#####################################정득님코드

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)

