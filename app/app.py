from flask import Flask
from extractors import yahoo

app = Flask(__name__)
if __name__ == "__main__":
	app.run()

@app.route('/')
def index():
	return '<h1>Bobit</h1>'

@app.route('/yahoo')
def yahoo_test():
	return yahoo.getData('YHOO', '2014-04-25', '2014-04-29')
