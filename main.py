from flask import Flask, send_from_directory
import lights

app = Flask(__name__)


@app.route('/')
def homepage():
    return send_from_directory('static', 'index.html')


@app.route('/off')
def off():
    lights.off()
    return "Done", 200


@app.route('/constant/dual')
def run_dual_constant():
    lights.constant_dual_color()
    return "Done", 200


@app.route('/constant/tri')
def run_tri_constant():
    lights.constant_tri_color()
    return "Done", 200


@app.route('/moving/dual')
def run_moving_dual():
    lights.moving_dual_color()
    return "Done", 200
