from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
import mysql.connector


app = Flask(__name__, static_folder="public", static_url_path="/")  # 代表目前執行的目錄
# 設置密鑰
app.secret_key = "WGXaTKE7JR9MzzykHVp1O8ix7cnkx5eOb400I5gPxXJI3I8saAUWZjDLxs6056M"
# 測試用帳號密碼
My_count = "test"
My_password = "test"


# 首頁
@app.route("/")
def home():
    return render_template("public.html")


# 註冊帳號
@app.route("/signup", methods=["POST"])
def signup():
    # 連線到資料庫
    con = mysql.connector.connect(
        user="root", 
        password="root123", 
        host="localhost", 
        database="website"
    )
    print("資料庫連線成功")

    count_name = request.form["count_name"]
    user_count = request.form["user_count"]
    password = request.form["password"]
    username = (user_count,)  # 將資料轉為tuple才可被SQL語法操作
    cursor = con.cursor()
    cursor.execute("select username from member where username = %s", (username))
    data = cursor.fetchone()
    if data:
        con.close()
        return redirect("/error?message=帳號已經被註冊")
    else:
        cursor.execute("insert into member(name, username, password) values(%s, %s, %s )",(count_name, user_count, password))
        con.commit()
        cursor.execute("select * from member where username=%s",(username))
        data=cursor.fetchone()
        session["username"] = count_name
        session["id"] = data[0]
        con.close()
        return redirect("/member")


# 登入用表單，並且驗證
@app.route("/signin", methods=["POST"])
def signin():
    con = mysql.connector.connect(user="root", password="root123", host="localhost", database="website")


    count = request.form["count"]
    password = request.form["password"]
    # username=(count,) #將資料轉為tuple才可被SQL語法操作
    cursor = con.cursor()
    cursor.execute("select id,name,username,password from member where username = %s and password = %s ",(count, password),)
    data = cursor.fetchone()
    con.close()
    if data:
        session["id"] = data[0]
        session["username"] = data[1]
        session["name"] = data[2]
        return redirect("/member")
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤")

@app.route("/createMessage", methods=["POST"])
def createMessage():
    message = request.form["message"]
    if "username" in session:
        input_message=message
        id=session["id"]
        con = mysql.connector.connect(
            user="root", 
            password="root123", 
            host="localhost", 
            database="website"
            )
        cursor = con.cursor()
        cursor.execute("insert into message(member_id, content) values(%s, %s )",(id, input_message))
        con.commit()
        con.close()
        return redirect("/member")
    else:
        return redirect("/")

# 先驗證是否有先登入才導至會員頁面
@app.route("/member")
def member():
    if "username" in session:
        con = mysql.connector.connect(
        user="root", 
        password="root123", 
        host="localhost", 
        database="website"
        )
        cursor = con.cursor()
        cursor.execute("select name,content,message.time from member inner join message on member.id=message.member_id order by message.time desc")
        data=cursor.fetchall()
        username = session["username"]
        con.close()
        return render_template("member.html", username=username,data = data)
    else:
        con.close()
        return redirect("/")

# 錯誤頁面導向
@app.route("/error")
def error():
    message = request.args.get("message", "發生意外的錯誤")
    return render_template("error.html", message=message)

# 登出
@app.route("/signout")
def signout():
    # 移除密鑰
    session.clear()
    return redirect("/")


app.run(port=3000, debug=True)
