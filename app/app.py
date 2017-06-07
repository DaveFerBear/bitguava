from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Bobit</h1>'

@app.route('/yahoo')
def yahoo_test():
	from extractors.yahoo import yahoo
	return str(yahoo.getData('YHOO', '2014-04-25', '2014-04-29'))

#MUST BE AT END OF FILE
if __name__ == "__main__":
	app.run()