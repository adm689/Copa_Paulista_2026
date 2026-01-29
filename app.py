from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


# Página principal com formulário
@app.route('/')
def index():
    return render_template('index.html')

# Páginas extras
@app.route('/sorteio')
def sorteio():
    return render_template('sorteio.html')

@app.route("/times")
def times():
    return render_template("times.html")

@app.route("/campeonato")
def campeonato():
    return render_template("campeonato.html")

@app.route("/fases")
def fases():
    return render_template("fases.html")

@app.route("/selecao")
def selecao():
    return render_template("selecao.html")

@app.route("/selecao_sorteio")
def selecao_sorteio():
    return render_template("selecao_sorteio.html")

@app.route("/selecao_camp")
def selecao_camp():
    return render_template("selecao_camp.html")

@app.route("/selecao_fases")
def selecao_fases():
    return render_template("selecao_fases.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
