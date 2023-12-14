from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def hello():
	return """<h1>Hello People</h1>
			  <br>
			  <body> your lucky number is """ + str(luckynumber()) + """</body>"""

@app.route("/moi")
def moi():
	return "<h2>Moi!</h2>"

def luckynumber():
	return random.randint(0,100)

if __name__ == "__main__":
	app.run(host='0.0.0.0')