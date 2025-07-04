import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from password_checker import password_strength, check_pwned

from flask import Flask, render_template, request
from password_checker import password_strength, check_pwned

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    pwned = None
    if request.method == "POST":
        password = request.form["password"]
        strong, feedback = password_strength(password)
        result = "Strong password!" if strong else "Weak password: " + "; ".join(feedback)
        pwned = check_pwned(password)
    return render_template("index.html", result=result, pwned=pwned)

if __name__ == "__main__":
    app.run(debug=True)
