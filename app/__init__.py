from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.routes.frases import frases_bp
    app.register_blueprint(frases_bp, url_prefix="/api/frases")
    
    return app
