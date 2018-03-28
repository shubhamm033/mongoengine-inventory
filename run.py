from flask import Flask

def create_app(config_filename):
    app=Flask(__name__)
    

    app.config.from_object(config_filename)
    
    from app import api_bp
    # app.register_blueprint(api_bp,url_prefix="/inventory")
    app.register_blueprint(api_bp,url_prefix="/inventory")
    from model import db
    db.__init__(app)
    
    return app

if __name__== "__main__":
    app=create_app("config")
    print(app)
    app.run(host="0.0.0.0",debug=True)
    
    p