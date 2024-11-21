from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QStackedWidget, QLineEdit

# Tela de Fornecedor
class TelaFornecedor(QWidget):
    def __init__(self, mudar_tela_callback):
        super().__init__()
        layout = QVBoxLayout()
        
        self.botaoLayoutFornecedor = QPushButton("Fornecedor", self)
        self.botaoLayoutFornecedor.setGeometry(260, -5, 300, 30)  
        self.botaoLayoutFornecedor.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid black;          
            border-radius: 10px;
            font-size: 14px;
            font-weight: bold;               
        """) 

        self.botaoFornecedor = QPushButton("Adicionar Fornecedor", self)
        self.botaoFornecedor.setGeometry(90, 180, 150, 80)  
        self.botaoFornecedor.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid black;          
            border-radius: 10px;               
        """)

        self.botaoFornecedores = QPushButton("Listar Fornecedores", self)
        self.botaoFornecedores.setGeometry(350, 180, 150, 80)  
        self.botaoFornecedores.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid black;          
            border-radius: 10px;               
        """)

        # Gerenciador de Produtos
        self.botaoEFornecedor = QPushButton("Editar Fornecedor", self)
        self.botaoEFornecedor.setGeometry(600, 180, 150, 80)  
        self.botaoEFornecedor.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid black;          
            border-radius: 10px;               
        """)

        self.botao_voltar = QPushButton("Voltar para Tela Inicial", self)
        self.botao_voltar.setStyleSheet("""
            color: white;                     
            background-color: gray;      
            border: 2px solid black;          
            border-radius: 10px;               
            font-size: 14px;  
        """)
        self.botao_voltar.setFixedSize(180, 60)  

        layout.addStretch()  
        

        self.botao_voltar.clicked.connect(lambda: mudar_tela_callback("inicial"))
        layout.addWidget(self.botao_voltar)


        self.setLayout(layout)

class TelaCompras(QWidget):
    def __init__(self, mudar_tela_callback):
        super().__init__()
        layout = QVBoxLayout()
        
        self.botaoLayoutCompras = QPushButton("Compras", self)
        self.botaoLayoutCompras.setGeometry(260, -5, 300, 30)  
        self.botaoLayoutCompras.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid black;          
            border-radius: 10px;
            font-size: 14px;
            font-weight: bold;               
        """) 

        self.botaoNCompra = QPushButton("Nova Compra", self)
        self.botaoNCompra.setGeometry(90, 180, 150, 80)  
        self.botaoNCompra.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid black;          
            border-radius: 10px;               
        """)

        self.botaoLCompras = QPushButton("Listar Compras", self)
        self.botaoLCompras.setGeometry(350, 180, 150, 80)  
        self.botaoLCompras.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid black;          
            border-radius: 10px;               
        """)

        # Gerenciador de Produtos
        self.botaoECompra = QPushButton("Editar Compra", self)
        self.botaoECompra.setGeometry(600, 180, 150, 80)  
        self.botaoECompra.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid black;          
            border-radius: 10px;               
        """)

        self.botao_voltar = QPushButton("Voltar para Tela Inicial", self)
        self.botao_voltar.setStyleSheet("""
            color: white;                     
            background-color: gray;      
            border: 2px solid black;          
            border-radius: 10px;               
            font-size: 14px;  
        """)
        self.botao_voltar.setFixedSize(180, 60)  

        layout.addStretch()  
        

        self.botao_voltar.clicked.connect(lambda: mudar_tela_callback("inicial"))
        layout.addWidget(self.botao_voltar)


        self.setLayout(layout)

class TelaVendas(QWidget):
    def __init__(self, mudar_tela_callback):
        super().__init__()
        layout = QVBoxLayout()
        
        self.botaoLayoutVendas = QPushButton("Vendas", self)
        self.botaoLayoutVendas.setGeometry(260, -5, 300, 30)  
        self.botaoLayoutVendas.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid black;          
            border-radius: 10px;
            font-size: 14px;
            font-weight: bold;               
        """) 

        self.botaoNVenda = QPushButton("Nova Venda", self)
        self.botaoNVenda.setGeometry(90, 180, 150, 80)  
        self.botaoNVenda.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid black;          
            border-radius: 10px;               
        """)

        self.botaoLVendas = QPushButton("Listar Vendas", self)
        self.botaoLVendas.setGeometry(350, 180, 150, 80)  
        self.botaoLVendas.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid black;          
            border-radius: 10px;               
        """)

        # Gerenciador de Produtos
        self.botaoEVenda = QPushButton("Editar Vendas", self)
        self.botaoEVenda.setGeometry(600, 180, 150, 80)  
        self.botaoEVenda.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid black;          
            border-radius: 10px;               
        """)

        self.botao_voltar = QPushButton("Voltar para Tela Inicial", self)
        self.botao_voltar.setStyleSheet("""
            color: white;                     
            background-color: gray;      
            border: 2px solid black;          
            border-radius: 10px;               
            font-size: 14px;  
        """)
        self.botao_voltar.setFixedSize(180, 60)  

        layout.addStretch()  
        

        self.botao_voltar.clicked.connect(lambda: mudar_tela_callback("inicial"))
        layout.addWidget(self.botao_voltar)


        self.setLayout(layout)
# Tela de Cliente
class TelaCliente(QWidget):
    def __init__(self, mudar_tela_callback):
        super().__init__()
        layout = QVBoxLayout()
        
        self.botaoLayoutCliente = QPushButton("Cliente", self)
        self.botaoLayoutCliente.setGeometry(260, -5, 300, 30)  
        self.botaoLayoutCliente.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid black;          
            border-radius: 10px;
            font-size: 14px;
            font-weight: bold;               
        """) 

        self.botaoACliente = QPushButton("Adicionar Cliente", self)
        self.botaoACliente.setGeometry(90, 180, 150, 80)  
        self.botaoACliente.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid black;          
            border-radius: 10px;               
        """)

        self.botaoLCliente = QPushButton("Listar Cliente", self)
        self.botaoLCliente.setGeometry(350, 180, 150, 80)  
        self.botaoLCliente.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid black;          
            border-radius: 10px;               
        """)

        # Gerenciador de Produtos
        self.botaoECliente = QPushButton("Editar Cliente", self)
        self.botaoECliente.setGeometry(600, 180, 150, 80)  
        self.botaoECliente.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid black;          
            border-radius: 10px;               
        """)

        self.botao_voltar = QPushButton("Voltar para Tela Inicial", self)
        self.botao_voltar.setStyleSheet("""
            color: white;                     
            background-color: gray;      
            border: 2px solid black;          
            border-radius: 10px;               
            font-size: 14px;  
        """)
        self.botao_voltar.setFixedSize(180, 60)  

        layout.addStretch()  
        

        self.botao_voltar.clicked.connect(lambda: mudar_tela_callback("inicial"))
        layout.addWidget(self.botao_voltar)


        self.setLayout(layout)
# Tela de Produtos
class TelaProduto(QWidget):
    def __init__(self, mudar_tela_callback):
        super().__init__()
        layout = QVBoxLayout()
        
        self.botaoLayoutProdutos = QPushButton("Produtos", self)
        self.botaoLayoutProdutos.setGeometry(260, -5, 300, 30)  
        self.botaoLayoutProdutos.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid black;          
            border-radius: 10px;
            font-size: 14px;
            font-weight: bold;               
        """) 

        # Gerenciador de Produtos
        self.botaoAProdutos = QPushButton("Adicionar Produtos", self)
        self.botaoAProdutos.setGeometry(130, 140, 150, 80)  
        self.botaoAProdutos.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)
        self.botaoAProdutos.clicked.connect(lambda: mudar_tela_callback("CadastrarProduto"))
        # Gerenciador de Produtos
        self.botaoLProdutos = QPushButton("Listar Produtos", self)
        self.botaoLProdutos.setGeometry(340, 140, 150, 80)  
        self.botaoLProdutos.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)

        # Gerenciador de Produtos
        self.botaoEprodutos = QPushButton("Editar Produtos", self)
        self.botaoEprodutos.setGeometry(550, 140, 150, 80)  
        self.botaoEprodutos.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)


        # Gerenciador de Categoria
        self.botaoACategoria = QPushButton("Adicionar Categoria", self)
        self.botaoACategoria.setGeometry(130, 270, 150, 80)
        self.botaoACategoria.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)
    
        # Gerenciador de Categoria
        self.botaoLCategorias = QPushButton("Listar Categorias", self)
        self.botaoLCategorias.setGeometry(340, 270, 150, 80)  
        self.botaoLCategorias.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)
        
        # Gerenciador de Categorias
        self.botaoECategorias = QPushButton("Editar Categorias", self)
        self.botaoECategorias.setGeometry(550, 270, 150, 80)  
        self.botaoECategorias.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)

        self.botao_voltar = QPushButton("Voltar para Tela Inicial", self)
        self.botao_voltar.setStyleSheet("""
            color: white;                     
            background-color: gray;      
            border: 2px solid black;          
            border-radius: 10px;               
            font-size: 14px;  
        """)
        self.botao_voltar.setFixedSize(180, 60)  

        layout.addStretch()  
        

        self.botao_voltar.clicked.connect(lambda: mudar_tela_callback("inicial"))
        layout.addWidget(self.botao_voltar)


        self.setLayout(layout)

class TelaCadastrarProduto(QWidget):
    def __init__(self, mudar_tela_callback):
        super().__init__()
        layout = QVBoxLayout()
        
        
        self.botaoLayoutProdutos = QPushButton("Produtos", self)
        self.botaoLayoutProdutos.setGeometry(260, -5, 300, 30)  
        self.botaoLayoutProdutos.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid black;          
            border-radius: 10px;
            font-size: 14px;
            font-weight: bold;               
        """) 

        # Gerenciador de Produtos
        self.botaoAProdutos = QPushButton(self)
        self.botaoAProdutos.setGeometry(200, 50, 400, 400)  
        self.botaoAProdutos.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)
        
        # Botão
        self.botaoAProdutos = QPushButton(self)
        self.botaoAProdutos.setText("Adicionar Produto")  # Adiciona um texto ao botão
        self.botaoAProdutos.setGeometry(220, 80, 300, 20)  
        self.botaoAProdutos.setStyleSheet("""
            color: white;                     
            background-color: grey;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)

        # Campo de texto
        self.campo_texto = QLineEdit(self) 
        self.campo_texto.setGeometry(220, 110, 300, 30) 
        self.campo_texto.setPlaceholderText("Digite o nome do produto")  
        self.campo_texto.setStyleSheet("""
            border: 1px solid grey;
            border-radius: 5px;
            padding: 5px;
        """)
        

        self.botao_salvar = QPushButton("Salvar")
        

        self.botao_voltar = QPushButton("Voltar para \nTela de Produtos", self)
        self.botao_voltar.setStyleSheet("""
            color: white;                     
            background-color: gray;      
            border: 2px solid black;          
            border-radius: 10px;               
            font-size: 14px;  
        """)
        self.botao_voltar.setFixedSize(180, 60)  

        layout.addStretch()  
        

        self.botao_voltar.clicked.connect(lambda: mudar_tela_callback("VoltarInicialProdutos"))
        layout.addWidget(self.botao_voltar)


        self.setLayout(layout)
# Tela Inicial
class JanelaPrincipal(QWidget):
    def __init__(self, mudar_tela_callback):
        super().__init__()
       
        # Rótulo
        self.label = QLabel("TELA INICIAL", self)
        self.label.setGeometry(-1, 40, 200, 30) 
        self.label.setStyleSheet("""
        color: white; 
        font-size: 22px;
        font-weight: bold;
    """)

        self.botaoVendas = QPushButton("Vendas", self,)
        self.botaoVendas.setGeometry(-10, 110, 150, 80)  
        self.botaoVendas.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)
        self.botaoVendas.clicked.connect(lambda: mudar_tela_callback("vendas"))
        # Produto
        self.botaoProduto = QPushButton("Produto", self)
        self.botaoProduto.setGeometry(-10, 180, 150, 80)  
        self.botaoProduto.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)
        self.botaoProduto.clicked.connect(lambda: mudar_tela_callback("produto"))
        # Fornecedor 
        self.botaoFornecedor = QPushButton("Fornecedor", self)
        self.botaoFornecedor.setGeometry(-10, 250, 150, 80)  
        self.botaoFornecedor.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)
        self.botaoFornecedor.clicked.connect(lambda: mudar_tela_callback("fornecedor"))
        # Compras
        self.botaoCompras = QPushButton("Compras", self)
        self.botaoCompras.setGeometry(-10, 320, 150, 80)  
        self.botaoCompras.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)
        self.botaoCompras.clicked.connect(lambda: mudar_tela_callback("compras"))
        # Gerenciador de Vendas
        self.botaoGVendas = QPushButton("Gerenciador de Vendas", self)
        self.botaoGVendas.setGeometry(220, 180, 150, 80)  
        self.botaoGVendas.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)
        self.botaoGVendas.clicked.connect(lambda: mudar_tela_callback("vendas"))
        # Gerenciador de Compras
        self.botaoGcompras = QPushButton("Gerenciador de Compras", self)
        self.botaoGcompras.setGeometry(400, 180, 150, 80)  
        self.botaoGcompras.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)
        self.botaoGcompras.clicked.connect(lambda: mudar_tela_callback("compras"))

        # Gerenciador de Produtos
        self.botaoGprodutos = QPushButton("Gerenciador de Produtos", self)
        self.botaoGprodutos.setGeometry(580, 180, 150, 80)  
        self.botaoGprodutos.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)
        self.botaoGprodutos.clicked.connect(lambda: mudar_tela_callback("produto"))

        # Gerenciador de Fornecedores
        self.botaoGFornecedores = QPushButton("Gerenciador de Fornecedores", self)
        self.botaoGFornecedores.setGeometry(300, 280, 150, 80)
        self.botaoGFornecedores.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)
        self.botaoGFornecedores.clicked.connect(lambda: mudar_tela_callback("fornecedor"))
        
        # Gerenciador de Clientes
        self.botaoGClientes = QPushButton("Gerenciador de Clientes", self)
        self.botaoGClientes.setGeometry(480, 280, 150, 80)  
        self.botaoGClientes.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)
        self.botaoGClientes.clicked.connect(lambda: mudar_tela_callback("cliente"))
       


# Gerenciador de Telas (StackedWidget)
class GerenciadorDeTelas(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()
        self.setWindowTitle("Gerenciamento de estoque")
        self.setGeometry(100, 100, 820, 520) 
        self.setStyleSheet("""                    
            background-color: lightblue; 
            font-family:Arial 
        """)

        # Criar as telas
        self.tela_inicial = JanelaPrincipal(self.mudar_tela)
        self.tela_inicial_fornecedor = TelaFornecedor(self.mudar_tela)
        self.tela_inicial_produto = TelaProduto(self.mudar_tela)
        self.tela_inicial_cliente = TelaCliente(self.mudar_tela)
        self.tela_inicial_compra = TelaCompras(self.mudar_tela)
        self.tela_inicial_vendas = TelaVendas(self.mudar_tela)
        self.tela_cadastrar_produto = TelaCadastrarProduto(self.mudar_tela)
        # Adicionar as telas ao stacked widget
        self.stacked_widget.addWidget(self.tela_inicial)
        self.stacked_widget.addWidget(self.tela_inicial_fornecedor)
        self.stacked_widget.addWidget(self.tela_inicial_produto)
        self.stacked_widget.addWidget(self.tela_inicial_cliente)
        self.stacked_widget.addWidget(self.tela_inicial_compra)
        self.stacked_widget.addWidget(self.tela_inicial_vendas)
        self.stacked_widget.addWidget(self.tela_cadastrar_produto)
        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

    def mudar_tela(self, nome_tela):
        if nome_tela == "inicial":
            self.stacked_widget.setCurrentWidget(self.tela_inicial)
        elif nome_tela == "fornecedor":
            self.stacked_widget.setCurrentWidget(self.tela_inicial_fornecedor)
        elif nome_tela == "produto":
            self.stacked_widget.setCurrentWidget(self.tela_inicial_produto)
        elif nome_tela == "cliente":
            self.stacked_widget.setCurrentWidget(self.tela_inicial_cliente)
        elif nome_tela == "compras":
            self.stacked_widget.setCurrentWidget(self.tela_inicial_compra)
        elif nome_tela == "vendas":
            self.stacked_widget.setCurrentWidget(self.tela_inicial_vendas)
        elif nome_tela == "VoltarInicialProdutos":
            self.stacked_widget.setCurrentWidget(self.tela_inicial_produto)
        elif nome_tela == "CadastrarProduto":
            self.stacked_widget.setCurrentWidget(self.tela_cadastrar_produto)


# Inicialização do aplicativo
if __name__ == "__main__":
    app = QApplication([])
    gerenciador = GerenciadorDeTelas()
    gerenciador.show()
    app.exec_()
