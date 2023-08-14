from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import jsonify
import mysql.connector


app = Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key = "WGXaTKE7JR9MzzykHVp1O8ix7cnkx5eOb400I5gPxXJI3I8saAUWZjDLxs6056M"

cnxpool = mysql.connector.pooling.MySQLConnectionPool(user="root", password="root123", host="localhost", database="website",pool_name="mypool",pool_size=5)

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
    try:
        con=cnxpool.get_connection()
        cursor = con.cursor(dictionary=True)
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
            session["username"] = data["username"]
            session["id"] = data["id"]
            session["name"] = data["name"]
            return redirect("/member")
    finally:
        cursor.close()
        con.close()



# 登入用表單，並且驗證
@app.route("/signin", methods=["POST"])
def signin():
    con=cnxpool.get_connection()
    cursor = con.cursor(dictionary=True)
    try:
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
    finally:
        cursor.close()
        con.close()

@app.route("/createMessage", methods=["POST"])
def createMessage():
    if "username" in session:
        message = request.form["message"]
        con=cnxpool.get_connection()
        cursor = con.cursor(dictionary=True)
        try:
            input_message = message
            id = session["id"]
            cursor.execute(
                "insert into message(member_id, content) values(%s, %s )",
                (id, input_message),
            )
            con.commit()
            return redirect("/member")
        finally:
            cursor.close()
            con.close()
    else:
        return redirect("/")


# 先驗證是否有先登入才導至會員頁面
@app.route("/member")
def member():
    if "username" in session:
        con=cnxpool.get_connection()
        cursor = con.cursor(dictionary=True)
        try:
            cursor.execute("select message.id,name,content,message.time from member inner join message on member.id=message.member_id order by message.time desc")
            data = cursor.fetchall()
            usernames = session["name"]
            return render_template("member.html", username=usernames, data=data)
        finally:
            cursor.close()
            con.close()
    else:
        return redirect("/")


@app.route("/deleteMessage", methods=["POST"])
def deleteMessage():
    con=cnxpool.get_connection()
    cursor = con.cursor(dictionary=True)
    try:
        data=request.get_json()
        text=data.get("text")
        text=(text,)
        cursor.execute("delete from message where id=%s",(text))
        con.commit()
        return jsonify({"message": "資料刪除成功"})
    finally:
        cursor.close()
        con.close()

@app.route("/api/member/<username>")
def search(username):
    con=cnxpool.get_connection()
    cursor = con.cursor(dictionary=True)
    try:
        cursor.execute("select id,name,username from member where username=%s",(username,))
        data=cursor.fetchone()
        print(data)
        if data is not None:
            return {"data": data}
        else:
            return {"data" : None}
    finally:
        cursor.close()
        con.close()

@app.route("/api/member", methods=["PATCH"])
def update():
    con=cnxpool.get_connection()
    cursor = con.cursor(dictionary=True)
    username=session["username"]
    try:
        data=request.get_json()
        text=data.get("name")
        cursor.execute("update member set name=%s where username=%s",(text,username,))
        con.commit()
        session["name"]=text
        return jsonify({"ok": True})
    except:
        return jsonify({"error": True})
    finally:
        cursor.close()
        con.close()

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
