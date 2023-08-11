from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import jsonify
import mysql.connector


app = Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key = "WGXaTKE7JR9MzzykHVp1O8ix7cnkx5eOb400I5gPxXJI3I8saAUWZjDLxs6056M"

con = mysql.connector.connect(
    user="root", password="root123", host="localhost", database="website"
)
cursor = con.cursor(dictionary=True)
# 首頁
@app.route("/")
def home():
    return render_template("public.html")


# 註冊帳號
@app.route("/signup", methods=["POST"])
def signup():
    # 連線到資料庫
    count_name = request.form["count_name"]
    user_count = request.form["user_count"]
    password = request.form["password"]
    username = (user_count,) 
    cursor.execute("select username from member where username = %s", (username))
    data = cursor.fetchone()
    if data:
        return redirect("/error?message=帳號已經被註冊")
    else:
        cursor.execute(
            "insert into member(name, username, password) values(%s, %s, %s )",(count_name, user_count, password))
        con.commit()
        cursor.execute("select * from member where username=%s", (username))
        data = cursor.fetchone()
        session["username"] = count_name
        session["id"] = data["id"]
        session["name"] = data["name"]
        return redirect("/member")


# 登入用表單，並且驗證
@app.route("/signin", methods=["POST"])
def signin():
    count = request.form["count"]
    password = request.form["password"]
    # username=(count,) #將資料轉為tuple才可被SQL語法操作
    cursor.execute(
        "select id,name,username,password from member where username = %s and password = %s ",(count, password))
    data = cursor.fetchone()
    if data:
        print(data["id"])
        session["id"] = data["id"]
        session["username"] = data["username"]
        session["name"] = data["name"]
        return redirect("/member")
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤")


@app.route("/createMessage", methods=["POST"])
def createMessage():
    message = request.form["message"]
    if "username" in session:
        input_message = message
        id = session["id"]
        cursor.execute(
            "insert into message(member_id, content) values(%s, %s )",
            (id, input_message),
        )
        con.commit()
        return redirect("/member")
    else:
        return redirect("/")


# 先驗證是否有先登入才導至會員頁面
@app.route("/member")
def member():
    if "username" in session:
        cursor.execute("select message.id,name,content,message.time from member inner join message on member.id=message.member_id order by message.time desc")
        data = cursor.fetchall()
        print(data)
        username = session["name"]
        return render_template("member.html", username=username, data=data)
    else:
        return redirect("/")
    
@app.route("/deleteMessage", methods=["POST"])
def deleteMessage():
    data=request.get_json()
    text=data.get("text")
    text=(text,)
    cursor.execute("delete from message where id=%s",(text))
    con.commit()
    return jsonify({"message": "資料刪除成功"})

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
