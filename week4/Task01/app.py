from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__,static_folder="public",static_url_path="/")#代表目前執行的目錄

@app.route("/")
def home():
    return render_template("public.html")

app.run(port=3000, debug=True)