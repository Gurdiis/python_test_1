#*************************************
#PY19_No06    PW-51A221(02) Zhang
#Cookie利用
#=====================================
#2023-09-07  NEW Zhang
#=====================================
#
#*************************************

from flask import Flask, render_template, request,make_response
import json
import datetime


app = Flask(__name__)

@app.route('/')
def index():
    data = {}
    errors = {}
    return render_template('index.html',data=data,errors=errors)


@app.route('/setcookie', methods=['POST'])
def setcookie():
    data = {}
    errors = {}

#入力項目名TBL*********************
    fields = {
        'name': '名前',
        'address': '住所',
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
    
#set cookie
    # 设置Cookie的有效期限（以秒为单位）
    limit = 5
    expires = int(datetime.datetime.now().timestamp()) + limit

    # 创建一个包含数据的字典，用于存储在Cookie中
    cookie_data = {'name': data['name'], 'address': data['address']}

    # 将字典数据转换为JSON格式
    json_data = json.dumps(cookie_data)

    # 创建响应对象
    resp = make_response(render_template('setcookie.html', data=data,fields=fields))

    # 设置Cookie，包括数据和过期时间
    resp.set_cookie('my_cookie', value=json_data, expires=expires)

    return resp


@app.route('/getcookie', methods=['POST'])
def getcookie():
    # 获取名为 'my_cookie' 的Cookie的值
    cookie_data = request.cookies.get('my_cookie')

    if cookie_data is not None:
        # 如果Cookie存在，将其解析为JSON格式（假设它是JSON数据）
        result = json.loads(cookie_data)
        # 在这里可以对 'result' 进行进一步处理
        return render_template('getcookie.html', result=result)

    return "Cookie data not found"

if __name__ == '__main__':
    app.run()
