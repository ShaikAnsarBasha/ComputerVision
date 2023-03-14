import os
from flask import Flask, render_template, request
import utils

app = Flask(__name__)
image_uploads_folder = "./static/image_uploads"

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            image_file_path = os.path.join(image_uploads_folder, image_file.filename)
            image_file.save(image_file_path)
            image = utils.get_rgb_image(image_file_path)
            prediction = utils.predict(model, image)
            return render_template("index.html", image_file_path=image_file_path, prediction=prediction)
    return render_template("index.html", image_file_path=None)


if __name__ == "__main__":
    model = utils.load_saved_model()
    app.run(port=5000)
