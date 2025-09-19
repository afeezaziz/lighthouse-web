from flask import render_template
from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/assets')
def assets():
    return render_template('assets.html')


# Restore Ark Nodes page
@bp.route('/ark-nodes')
def ark_nodes():
    return render_template('ark_nodes.html')


# Asset detail
@bp.route('/assets/<asset_id>')
def asset_detail(asset_id):
    return render_template('asset_detail.html', asset_id=asset_id)


# Lifts
@bp.route('/lifts')
def lifts():
    return render_template('lifts.html')


@bp.route('/lifts/<lift_id>')
def lift_detail(lift_id):
    return render_template('lift_detail.html', lift_id=lift_id)


# Lands
@bp.route('/lands')
def lands():
    return render_template('lands.html')


@bp.route('/lands/<land_id>')
def land_detail(land_id):
    return render_template('land_detail.html', land_id=land_id)


# VUTXOs
@bp.route('/vutxos')
def vutxos():
    return render_template('vutxos.html')


@bp.route('/vutxos/<vutxo_id>')
def vutxo_detail(vutxo_id):
    return render_template('vutxo_detail.html', vutxo_id=vutxo_id)


# Transactions
@bp.route('/txs')
def txs():
    return render_template('txs.html')


@bp.route('/txs/<tx_id>')
def tx_detail(tx_id):
    return render_template('tx_detail.html', tx_id=tx_id)


# Public key details
@bp.route('/pubs/<pubkey>')
def pub_detail(pubkey):
    return render_template('pub_detail.html', pubkey=pubkey)
