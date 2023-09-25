#*************************************
#PY19_No05    PW-51A221(02) Zhang
#Session演習
#=====================================
#2023-07-13  NEW Zhang
#=====================================
#
#*************************************

from flask import Flask, render_template, request,session,redirect
from datetime import timedelta


app = Flask(__name__)

# session初期設定
app.secret_key = 'your_secret_key'  
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route('/')
def index():
    data = {}
    errors = {}
    return render_template('index.html',data=data,errors=errors)


@app.route('/login', methods=['POST'])
def login():
    data = {}
    errors = {}

#入力項目名TBL*********************
    fields = {
        'username': 'ユーザーID',
        'password': 'パスワード',
    }

# 空白チェック*********************
    for field, label in fields.items():
        value = request.form.get(field)
        if value:
            data[field] = value
        else:
            errors[field] = f"{label}が入力されていません。"

    if errors:
        return render_template('index.html', data=data,errors=errors)
# 認証成功,ID PW を　sessionに格納
    if data['username'] == 'IH12' and data['password'] == '999':
        session['username'] = data['username']
        session['password'] = data['password']
        return render_template('login.html', data=data,fields=fields)
# 認証失敗
    else:
        errors['login_error'] = 'IDまたはパスワードが違います。'
        return render_template('index.html', data=data,errors=errors)



@app.route('/user', methods=['GET'])
def user():
    user_data = {}
# sessionチェック、存在するsessionを取り出す
    if session:
        user_data['username'] = session['username']
        user_data['password'] = session['password']
        return render_template('user.html', user_data=user_data)
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run()
