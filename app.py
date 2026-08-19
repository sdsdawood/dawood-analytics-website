from flask import Flask, render_template
import os


# ==========================================================
# APPLICATION CONFIGURATION
# ==========================================================

app = Flask(__name__)


app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "development-secret-key"
)



# ==========================================================
# ROUTES
# ==========================================================

@app.route("/")
def home():

    return render_template("index.html")



# ==========================================================
# APPLICATION START
# ==========================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )