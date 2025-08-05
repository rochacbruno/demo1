from flask import Flask, render_template, request
import os
import re

app = Flask(__name__)


@app.route("/")
def photos():
    image_folder = os.path.join(app.static_folder, "imgs")
    filter_pattern = request.args.get("filter", "")
    
    images = []
    filter_error = None
    
    for img in os.listdir(image_folder):
        if filter_pattern:
            try:
                if re.search(filter_pattern, img):
                    images.append(os.path.join("imgs", img))
            except re.error as e:
                # Invalid regex pattern, show all images
                filter_error = f"Invalid regex pattern: {str(e)}"
                images.append(os.path.join("imgs", img))
        else:
            images.append(os.path.join("imgs", img))
    
    return render_template("photos.html", 
                         images=images, 
                         filter_pattern=filter_pattern,
                         filter_error=filter_error)


if __name__ == "__main__":
    app.run(debug=True)
