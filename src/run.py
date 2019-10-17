from src.app.controller import app
from src.config import Config


if __name__ == "__main__":
    app.run(debug=Config.FLASK_DEBUG)
