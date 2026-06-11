from flask import Flask, render_template, request

app = Flask(__name__)

menu_items = [
    {"name": "Cheese Pizza", "price": 199},
    {"name": "Veg Burger", "price": 99},
    {"name": "Masala Dosa", "price": 129},
    {"name": "Chocolate Shake", "price": 89}
]

@app.route("/")
def home():
    return render_template("index.html", menu_items=menu_items)

@app.route("/order", methods=["POST"])
def order():
    customer_name = request.form.get("customer_name")
    address = request.form.get("address")
    selected_food = request.form.get("selected_food")

    return render_template(
        "success.html",
        customer_name=customer_name,
        address=address,
        selected_food=selected_food
    )

if __name__ == "__main__":
    app.run(debug=True)