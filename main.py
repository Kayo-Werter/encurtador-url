from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

links = {}

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        link_original = request.form["link-original"]
        caminho = request.form["caminho-do-link"]
        links[caminho] = link_original
        return f"Seu link é: {request.url_root}{caminho}"


    else:
        return render_template("homepage.html")


@app.route("/<caminho>")
def redirecionar(caminho):
    link_original = links.get(caminho)
    if link_original:
        return redirect(link_original)
    else:
        return "página não encontrada", 404

if __name__ == "__main__":
    app.run(debug=True)