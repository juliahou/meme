from flask import Flask, render_template, request, redirect, url_for
import meow
app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

@app.route("/")
def show_data():
	data = meow.main(6)
	return render_template('index.html', data=data)