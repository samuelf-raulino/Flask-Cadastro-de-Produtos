from flask import Flask,render_template,redirect,request
from func_connect import inserir_camiseta,retornar_camiseta,editar_camiseta,deletar_camiseta
app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html",retornar_camiseta=retornar_camiseta)
@app.route("/camiseta-insert",methods=["GET","POST"])
def camiseta_insert():
    if request.method=="POST":
        nome = request.form["nome"]
        tamanho = request.form["tamanho"]
        cor = request.form["cor"]
        modelo = request.form["modelo"]
        inserir_camiseta(nome,tamanho,cor,modelo)
        return redirect("/home")
    return render_template("camiseta.html")
@app.route("/camiseta-edit/<int:id>",methods=["GET","POST"])#declara a variavel inteira "id" como sendo o valor dado na url
def camiseta_edit(id):#pega a variavel da url e passa para a aba de atributos da função
    if request.method == "POST":
        nome = request.form["nome"]
        tamanho = request.form["tamanho"]
        cor = request.form["cor"]
        modelo = request.form["modelo"]
        editar_camiseta(nome,tamanho,cor,modelo,id)
        return redirect("/home")
    valores = retornar_camiseta(id)[0]#pega o valor id e retorna como a camiseta
    return render_template("camiseta_edit.html",valores = valores)
@app.route("/camiseta-delete/<int:id>")
def camiseta_delete(id):
    deletar_camiseta(id)
    return redirect("/home")
if __name__ == "__main__":
    app.run(debug=True)