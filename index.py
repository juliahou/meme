import os
from flask import Flask, render_template, request, redirect, url_for
#import meow
app = Flask(__name__)

'''@app.route("/")
def show_data():
	data = meow.main(10)
	return render_template('index.html', data=data)'''
@app.route("/")
def hello():
    return "Hello world!"

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)