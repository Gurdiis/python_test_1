#*************************************
#PY19_前記評定課題    PW-51A221(02) Zhang
#=====================================
#2023-09-19  NEW Zhang
#=====================================
#
#*************************************

from flask import Flask, render_template, request,session,redirect
from datetime import timedelta
import csv


app = Flask(__name__)

# session初期設定
app.secret_key = 'your_secret_key'  
app.permanent_session_lifetime = timedelta(minutes=1)



@app.route('/',methods=['GET'])
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
    if data['password'] == '111':
        return render_template('login.html', data=data,fields=fields)
# 認証失敗
    else:
        errors['login_error'] = 'パスワードが一致しません。'
        return render_template('index.html', data=data,errors=errors)



@app.route('/menu',methods=['GET'])
def menu():
    return render_template('menu.html')



@app.route('/input', methods=['POST'])
def handle_root():
    data={}
    errors={}
    # 一つのsessionでもなかったら、全てのsessionを消す
    keys = ['ganumber', 'name', 'klass']
    for key in keys:
        if key not in session:
            session.clear()
            break
    # check修正　及び　alldisp登録画面へ　から戻す
    # if request.method == 'POST':
    #     return redirect('/input') 

    return render_template('input.html',data=data,errors=errors)



@app.route('/check', methods=['POST'])
def check():
    data = {}
    errors = {}

    #入力項目名TBL*********************
    fields = {
        'ganumber': '商品コード',
        'name': '商品名',
        'klass': '商品価格',
    }

    #空白チェックする前に、sessionを消す
    for field in fields:
        session.pop(field, None)

    # 空白チェック*********************
    for field, label in fields.items():
        value = request.form.get(field)
        if value:
            data[field] = value
        else:
            errors[field] = f"{label}が入力されていません。"

    if errors:
        return render_template('input.html', data=data,errors=errors)
    # 入力した情報をsessionに格納
    else:
        for key, value in data.items():
            session[key] = value
    return render_template('check.html', data=data,fields=fields)



@app.route('/csvout', methods=['POST'])
def csvout():
    fields = {
        'ganumber': '商品コード',
        'name': '商品名',
        'klass': '商品価格',
    }
    #sessionから取った情報を、CSVに追加
    csvdata = []
    file_path = 'data.csv'
    csvdata.append([session.get(key, '') for key in fields])

    with open(file_path, 'a', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(csvdata)
    #session key　学籍番号　削除
    session.pop('ganumber', None)
    #直近一回目入力した情報を、CSVから取得
    last_data = csvdata[-1] if csvdata else []

    return render_template('csvout.html',last_data=last_data)




@app.route('/alldisp', methods=['POST'])
def alldisp():
    fields = {
        'ganumber': '学籍番号',
        'name': '氏名',
        'klass': 'クラス',
    }
    #csv全件表示
    all_data = []
    file_path = 'data.csv'

    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            all_data.append(row)
    
    return render_template('alldisp.html', all_data=all_data,fields=fields)


if __name__ == '__main__':
    app.run()
