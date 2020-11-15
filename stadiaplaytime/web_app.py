import os
from flask import Flask
from flask import request, render_template
from stadiaplaytime.stadia_playtime import list_game_time
app = Flask(__name__)

FILE_PATH = 'uploads\\uploaded_file.json'


@app.route('/hello')
def hello_world():
    return render_template("upload_file.html")


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['filename']
        f.save(FILE_PATH)

        game_list = list_game_time()
        os.remove(FILE_PATH)
        return render_template("result_table.html", result=game_list)

    return render_template("upload_file.html")


if __name__ == '__main__':
   app.run(debug=True, host='localhost')