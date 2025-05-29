from flask import Flask
from app.api.receipt_api import process_bp
from app.api.receipt_api import points_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(process_bp)
    app.register_blueprint(points_bp)
    return app


