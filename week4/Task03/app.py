from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session

app=Flask(__name__,static_folder="public",static_url_path="/")#代表目前執行的目錄
# 設置密鑰
app.secret_key="i am very secret"
# 測試用帳號密碼
My_count = "test"
My_password = "test"

# 首頁
@app.route("/")
def home():
    return render_template("public.html")

# 登入用表單，並且驗證
@app.route("/signin" ,methods=["POST"])
def signin():
    count=request.form["count"]
    password=request.form["password"]
    if count!=My_count or password!=My_password:
        return redirect("/error?message=帳號、或密碼錯誤")
    elif len(count)>0:
        session["username"]="test"
        return redirect("/member")
    else:
        return redirect("/error?message=請輸入使用者名稱和密碼")

#先驗證是否有先登入才導至會員頁面
@app.route("/member")
def member():
    if "username" in session:
        return render_template("member.html")
    else:
        return redirect("/")

# 錯誤頁面導向
@app.route("/error")
def error():
    message=request.args.get("message","發生意外的錯誤")
    return render_template("error.html",message=message)

#登出
@app.route("/signout")
def signout():
    #移除密鑰
    del session["username"]
    #導回首頁
    return redirect("/")

app.run(port=3000, debug=True)