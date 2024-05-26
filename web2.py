import os
from flask import Flask, render_template

app = Flask(__name__)

def list_html_files(directory):
    html_files = []
    if os.path.exists(directory):
        for file in os.listdir(directory):
            if file.endswith(".html"):
                html_files.append(file)
    return html_files
web_directory_input = input("Type the file path: ")
@app.route('/')
def index():
    web_directory = (web_directory_input)
    html_files = list_html_files(web_directory)
    return render_template("index.html", html_files=html_files)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)
