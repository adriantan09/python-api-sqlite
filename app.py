from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# essential to register other routes
from routes import game_routes

@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory(path)

swaggerui_blueprint = get_swaggerui_blueprint(
    "/docs", # SWAGGER_URL
    "/static/swagger.json", # API_URL
    config={ 'app_name': "Test application" }
)
app.register_blueprint(swaggerui_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
