# app.py

from flask_cors import CORS
from flask import Flask
from youtube_api.youtube import Yt
from scrap.webscrap import Scrap

app = Flask(__name__)
CORS(app)


@app.route('/ytb/<id>')
def youtube_search(id):
    string = Yt.youtube_search(Yt(), query=id)
    return "{}".format(string)


@app.route('/scrap/<name>')
def scrap_item(name):
    spotfid = Scrap.startBroser(Scrap(), name)
    return '{}'.format(spotfid)


@app.route('/')
def index():
    return "<h1>Flask API</h1></br>" \
           "<h2>A Flask API that converts Youtube music to a Spotify item :)</h2>" \
           "<h3>A simple project made by Paulo Henrique</h3>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=False, threaded=True, port=5000)
