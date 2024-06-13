from flask import Flask, render_template, send_file, url_for, redirect

app = Flask("Fahime Personal website")

@app.route("/")
def my_root():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    
    return render_template("login.html")


@app.route("/contact")
def contact():
    
    return render_template("contact.html")

@app.route("/register")
def register():
    
    return render_template("register.html")


@app.route("/blog")
def blog():
    
    return render_template("blog.html")

@app.route("/download")
def download():
    return send_file('static/fahimecv.pdf', as_attachment=True)