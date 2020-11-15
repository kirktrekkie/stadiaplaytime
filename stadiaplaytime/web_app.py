from flask import Flask
from flask import request, render_template
from stadiaplaytime.stadia_playtime import list_game_time
app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return render_template("upload_file.html")


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['filename']
        f.save('uploads\\uploaded_file.json')

        game_list = list_game_time()
        return render_template("result_table.html", result=game_list)

    return render_template("upload_file.html")


if __name__ == '__main__':
   app.run(debug=True, host='localhost')