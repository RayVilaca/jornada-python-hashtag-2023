from flask import Flask, render_template
from flask_socketio import SocketIO, send

# cria o site
app = Flask(__name__)
# chave de seguranca
app.config["SECRET"] = "ajuiahfa78fh9f78shfs768fgs7f6"
# para testarmos o código, no final tiramos
app.config["DEBUG"] = True
# cria a conexão entre diferentes máquinas que estão no mesmo site
socketio = SocketIO(app, cors_allowed_origins="*")

# define que a função abaixo vai ser acionada quando o evento de "message" acontecer
@socketio.on("message")
def gerenciar_mensagens(mensagem):
    print(f"Mensagem: {mensagem}")
    # envia a mensagem para todo mundo conectado no site
    send(mensagem, broadcast=True)

# cria a página do site
@app.route("/")
def home():
    # essa página vai carregar esse arquivo html que está aqui
    return render_template("index.html")

if __name__ == "__main__":
    # define que o app vai rodar no seu servidor local, ou seja, na internet em que o seu computador tá conectado
    socketio.run(app, host='localhost')