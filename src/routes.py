from flask import render_template
from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/assets')
def assets():
    return render_template('assets.html')

@bp.route('/ark-nodes')
def ark_nodes():
    return render_template('ark_nodes.html')