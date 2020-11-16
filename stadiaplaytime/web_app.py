import os
from flask import Flask
from flask import request, render_template
from stadiaplaytime.stadia_playtime import list_game_time
from stadiaplaytime.plot_graphs import make_graph_total_time
from stadiaplaytime.remove_graphs import remove_old_graphs
app = Flask(__name__)

FILE_PATH = 'uploads/uploaded_file.json'
BAR_GRAPH_PATH = 'stadiaplaytime/static/total_time.png'
PIE_GRAPH_PATH = 'stadiaplaytime/static/pie_graph.png'

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
        remove_file_with_try(FILE_PATH)

        remove_old_graphs()
        file_number = make_graph_total_time(game_list)
        return render_template("result_table.html", result=game_list, file_number=file_number)

    return render_template("upload_file.html")


def remove_file_with_try(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass

if __name__ == '__main__':
   app.run(debug=True, host='localhost')