# def main():
#     print("Hello, World!")

# if __name__ == "__main__":
#     main()
from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template("file1.html")

if __name__ == "__main__":
    app.debug=True
    app.run()

