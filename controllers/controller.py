from flask import render_template
from app import app
from models.game_shop import orders

@app.route("/")
def index():
    return render_template("index.html", orders = orders)

@app.route("/orders/<index>")
def show_order(index):
    index = int(index)
    order = orders[index]
    return render_template("orders.html", order = order)