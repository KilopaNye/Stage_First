from flask import Flask
from flask import request
from flask import render_template
from flask import redirect

app=Flask(__name__,static_folder="public",static_url_path="/")#代表目前執行的目錄


My_count = "test"
My_password = "test"


@app.route("/")
def home():
    return render_template("public.html")

# 登入用表單，並且驗證
@app.route("/signin" ,methods=["POST"])
def signin():
    count=request.form["count"]
    password=request.form["password"]
    if len(count)<1:
        return redirect("/error?message=請輸入使用者名稱和密碼")
    elif count!=My_count or password!=My_password:
        return redirect("/error?message=帳號、或密碼錯誤")
    elif len(count)>0:
        session["username"]="test"
        return redirect("/member")


@app.route("/error")
def error():
    message=request.args.get("message","發生意外的錯誤")
    return render_template("error.html",message=message)

app.run(port=3000, debug=True)