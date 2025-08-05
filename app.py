from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def photos():
    image_folder = os.path.join(app.static_folder, "imgs")
    images = [os.path.join("imgs", img) for img in os.listdir(image_folder)]
    return render_template("photos.html", images=images)


if __name__ == "__main__":
    app.run(debug=True)
