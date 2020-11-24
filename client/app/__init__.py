import os
from flask import Flask, render_template
from flask import send_from_directory


def create_app(script_info=None):

    app = Flask(__name__)
    
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    from app.blueprints.home import home_bp
    app.register_blueprint(home_bp)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
    
    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                            'favicon.ico',mimetype='image/vnd.microsoft.icon')

    return app