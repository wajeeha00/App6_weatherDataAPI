from flask import Flask, request, jsonify,render_template

app =Flask("website")
@app.route("/home")
def home():
    return render_template("home.html")

# @app.route("/about/")
# def about():
#     return render_template("about.html" )

# @app.route("/contact-us/")
# def contact():
#     return render_template("contact.html")

# @app.route("/store/")
# def store():
#     return render_template("store.html")

app.run(debug=True)