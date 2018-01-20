from flask import Flask, render_template
import meow
app = Flask(__name__)

@app.route("/")
def show_data():
	data = meow.main()
	return render_template('index.html', data=data)
