from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "siwarha"
password = "123"
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]


@app.route('/', methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	elif username == request.form['username'] and password == request.form['password']:
		return redirect(url_for('home'))
	else:
		return render_template('login.html')

@app.route('/home')
def home():
	return render_template('home.html', friends = facebook_friends)

@app.route('/friend_exists/<name>')
def friend_exists(name):
	if name in facebook_friends:
		friend_exists = True
	else:
		friend_exists = False
	return render_template('friend_exists.html', friend_exists = friend_exists, friends = facebook_friends)
def home():
	return render_template('home.html', friends = facebook_friends)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
