from flask import Flask
app=Flask("FastQA")

@app.route("/")
def index():
	return "Welcome to FastQA!"

@app.route("/api/")
def newSheet():
	return "Welcome to FastQA API!"


