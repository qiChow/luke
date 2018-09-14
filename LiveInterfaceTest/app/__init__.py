from .rank import rank
from .blackword import blackword
from flask import Flask

app = Flask(__name__)
app.register_blueprint(rank, url_prefix='/gamehq/guest/api/v1/rank')
app.register_blueprint(blackword, url_prefix='/api/v1/blacklist_words')