from flask import Flask
import logging

app = Flask(__name__)

# Логирование
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Запрос на главную страницу")
    return "Hello, DevOps!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)