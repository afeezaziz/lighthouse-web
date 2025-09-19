from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.String(64), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    ticker = db.Column(db.String(10), nullable=True)
    supply = db.Column(db.BigInteger, nullable=False)
    decimals = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # Taproot Asset specific
    genesis_point = db.Column(db.String(128), unique=True, nullable=False)
    asset_type = db.Column(db.String(20), nullable=False)
    meta_data = db.Column(db.JSON)

class ArkNode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.String(64), unique=True, nullable=False)
    pub_key = db.Column(db.String(66), nullable=False)
    host = db.Column(db.String(255), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    last_seen = db.Column(db.DateTime, server_default=db.func.now())