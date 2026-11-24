
from flask import Flask, render_template, abort

app = Flask(__name__)

SAMPLE_ITEMS = [
    {"id": 1, "name": "Cafe con Leche", "category": "Drinks", "price_cents": 350},
    {"id": 2, "name": "Cuban Coffee", "category": "Drinks", "price_cents": 250},
    {"id": 3, "name": "Cortadito", "category": "Drinks", "price_cents": 300},
    {"id": 4, "name": "Cuban Sandwich", "category": "Food", "price_cents": 950},
    {"id": 5, "name": "Croqueta", "category": "Food", "price_cents": 200},
    {"id": 6, "name": "Guava Pastry", "category": "Dessert", "price_cents": 325},
]

SAMPLE_ORDERS = [
    {"id": 101, "customer": "Maria", "item": "Cafe con Leche", "status": "Pending", "total_cents": 350},
    {"id": 102, "customer": "Carlos", "item": "Cuban Sandwich", "status": "Preparing", "total_cents": 950},
    {"id": 103, "customer": "Ana", "item": "Guava Pastry", "status": "Completed", "total_cents": 325},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html", items=SAMPLE_ITEMS)


@app.route("/menu/<int:item_id>")
def item_detail(item_id):
    if item_id < 1:
        abort(404)

    item = next(
        (i for i in SAMPLE_ITEMS if i["id"] == item_id),
        None
    )

    if item is None:
        abort(404)

    return render_template("item.html", item=item)

@app.route("/order/new")
def new_order():
    return render_template("order.html", items=SAMPLE_ITEMS)

@app.route("/kitchen")
def kitchen():
    return render_template("kitchen.html", orders=SAMPLE_ORDERS)

@app.route("/orders")
def orders():
    return render_template("orders.html", orders=SAMPLE_ORDERS)

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
