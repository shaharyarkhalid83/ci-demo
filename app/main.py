# app/main.py

import os
from flask import Flask, render_template_string, send_from_directory
from version import APP_VERSION, APP_MESSAGE

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html>
  <head>
    <title>CI/CD Demo – {{ version }}</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 2rem; }
      .card {
        border: 1px solid #ddd;
        padding: 1.5rem;
        border-radius: 8px;
        max-width: 600px;
      }
      img {
        margin-top: 1rem;
        border-radius: 6px;
        width: 200px;
      }
      .version {
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
      }
    </style>
  </head>
  <body>
    <h1>CI/CD Demo</h1>
    <div class="card">
      <p class="version"><b>Version:</b> {{ version }}</p>
      <p>{{ message }}</p>
    </div>
  </body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(
        TEMPLATE,
        version=APP_VERSION,
        message=APP_MESSAGE,
    )


@app.route("/static/<path:filename>")
def static_files(filename):
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    return send_from_directory(static_dir, filename)


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
