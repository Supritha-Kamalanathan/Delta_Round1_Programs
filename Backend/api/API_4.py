# Blueprint is added in this API


from flask import Flask, jsonify, request, Blueprint
from googletrans import Translator
from langdetect import detect
from langcodes import *

app = Flask(__name__)

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/translate')
def translate():
    if request.method == 'GET':
        text = request.args.get("text")
        translator = Translator()
        transtring = translator.translate(text)
        response = {"translated-text": transtring.text}
    return jsonify(response)

@api_bp.route('/detect')
def detect_lang():
    if request.method == 'GET':
        text = request.args.get("text")
        lang = detect(text)
        response = {"detected language": lang, "language name": Language.make(language=lang).display_name()}
        return jsonify(response)

app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run()
