from flask import Flask

app = Flask(__name__)

@app.route("/")
def yeet():
	return 'yeeeeet'

if __name__ == '__main__':
	app.run(debug=True)