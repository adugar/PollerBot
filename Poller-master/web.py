from flask import Flask, render_template
import utils

app = Flask(__name__)

@app.route('/poll/<id>')
def home(id):
    info = utils.get_info(id)
    choices1 = info[1].split("##")
    return render_template("poll.html", sname=info[3], creator=info[2], choices=choices1)

if __name__ == '__main__':
    app.run(port=5002)