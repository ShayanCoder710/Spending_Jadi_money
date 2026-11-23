from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for('jadi'))

@app.route("/jadi")
def jadi():
    return render_template("jadi.html")

@app.route("/ElonMusk")
def elonmusk():
    return render_template("ElonMusk.html")

@app.route("/BillGates")
def billgates():
    return render_template("BillGates.html")

@app.route("/MarkZuckerberg")
def markzuckerberg():
    return render_template("MarkZuckerberg.html")

@app.route("/JeffBezos")
def jeffbezos():
    return render_template("JeffBezos.html")

@app.route("/LarryPage")
def larrypage():
    return render_template("LarryPage.html")

if __name__ == "__main__":
    app.run(debug=True)
