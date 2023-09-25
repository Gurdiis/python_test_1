from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    # 设置 session 数据
    session['username'] = 'John'
    session['age'] = 25

    # 创建 session 的副本
    session2 = session.copy()

    # 修改 session2 的值
    session2['age'] = 30

    return f"session: {session}, session2: {session2}"

if __name__ == '__main__':
    app.run()



    if 'ganumber' not in session:  
        session.clear() 
    if 'name' not in session:  
        session.clear() 
    if 'klass' not in session:  
        session.clear() 
    if 'shnumber' not in session:  
        session.clear() 
    if 'yunumber' not in session:  
        session.clear() 
    if 'address' not in session:  
        session.clear() 
    if 'tel' not in session:  
        session.clear() 
    if 'mail' not in session:  
        session.clear() 
