import os
from flask import Flask, render_template, request, redirect, url_for
import meow
app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

@app.route("/")
def show_data():
	print "meow"
	data = meow.main(10)
	return render_template('index.html', data=data)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)