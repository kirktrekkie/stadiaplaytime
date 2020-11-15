import os
from flask import Flask
from flask import request, render_template
from stadiaplaytime.stadia_playtime import list_game_time
from stadiaplaytime.plot_graphs import make_graph_total_time
app = Flask(__name__)

FILE_PATH = 'uploads/uploaded_file.json'


@app.route('/hello')
def hello_world():
    return render_template("upload_file.html")


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            os.mkdir('uploads')
        except FileExistsError:
            pass
        f = request.files['filename']
        f.save(FILE_PATH)

        game_list = list_game_time(FILE_PATH)
        os.remove(FILE_PATH)
        make_graph_total_time(game_list)
        return render_template("result_table.html", result=game_list)

    return render_template("upload_file.html")


if __name__ == '__main__':
   app.run(debug=True, host='localhost')