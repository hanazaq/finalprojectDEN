from flask import Flask ,render_template ,request
app = Flask(__name__)

@app.route("/")
def website():
	return render_template('home.html')
@app.route("/diary")
def about():
	return render_template('Diary.html')
@app.route("/advices")
def form():
	return render_template('advices.html')
@app.route("/about")
def us():
	return render_template('aboutUs.html')


if __name__== "__main__":
	app.run(port=8000,debug=True)
