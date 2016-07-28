from flask import Blueprint, request
from martin.utils.controllers import render_html

IndexBlueprint = Blueprint('Index', __name__, url_prefix='')

class IndexView(object):
    @staticmethod
    @IndexBlueprint.route('/')
    @render_html('index.html')
    def index():
        return
