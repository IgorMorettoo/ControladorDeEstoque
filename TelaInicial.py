from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget

class MinhaJanela(QWidget):
    def __init__(self):
        super().__init__()

        # Configuração da janela
        self.setWindowTitle("Gerenciamento de estoque")
        self.setGeometry(100, 100, 640, 480)  

        # Rótulo
        self.label = QLabel("Clique no botão abaixo!", self)
        self.label.setGeometry(50, 50, 200, 30)  # Posição (x=50, y=50) e tamanho (200x30)

        # Botão
        self.botao = QPushButton("Clique aqui", self)
        self.botao.setGeometry(50, 100, 120, 40)  # Posição (x=50, y=100) e tamanho (120x40)
        self.botao.clicked.connect(self.ao_clicar)

        # Botão
        self.botao2 = QPushButton("Clique aqui 2", self)
        self.botao2.setGeometry(50, 20, 120, 40)  # Posição (x=50, y=100) e tamanho (120x40)
        self.botao2.clicked.connect(self.ao_clicar)
        self.botao.setStyleSheet("background-color: lightblue;")


    def ao_clicar(self):
        self.label.setText("Botão clicado!")  # Altera o texto do rótulo

# Inicialização do aplicativo
if __name__ == "__main__":
    app = QApplication([])
    janela = MinhaJanela()
    janela.show()
    app.exec_()
