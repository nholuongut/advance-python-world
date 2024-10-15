from flask import Flask, jsonify, abort
from db import fetch_blog, fetch_blogs, NotFoundError, NotAutherizedError, DbEmptyError

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/blogs")
def get_blogs():
    try:
        return fetch_blogs()
    except DbEmptyError:
        abort(404, "Resouce not found.")
    except NotFoundError:
        abort(404, "Resource not found.")


@app.route("/blogs/<id>")
def get_blog(id):
    try:
        return fetch_blog(id=id)
    except NotFoundError:
        abort(404, "Resource not found.")
    except NotAutherizedError:
        abort(403, "Not Authorized.")


if __name__ == "__main__":
    app.run(debug=True)
