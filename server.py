from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome"

@app.route("/play")
def play():
    return render_template("index.html", amount = 3, box_color = "#9fc5f8")

@app.route("/play/<int:boxes>")
def play1(boxes):
    return render_template("index.html", amount = boxes, box_color = "#9fc5f8")

@app.route("/play/<int:boxes>/<box_color>")
def play2(boxes,box_color):
    return render_template("index.html", amount = boxes, box_color = box_color)



if __name__=="__main__":
    app.run(debug=True)