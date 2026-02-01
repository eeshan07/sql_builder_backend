from flask import Flask
from flask_cors import CORS
from app.routes.metadata import metadata_bp
from app.routes.query import query_bp
from app.routes.saved_query import saved_query_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(metadata_bp, url_prefix="/api/metadata")
    app.register_blueprint(query_bp, url_prefix="/api/query")
    app.register_blueprint(saved_query_bp, url_prefix="/api/saved-query")

    return app
