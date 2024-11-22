from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QStackedWidget, QLineEdit, QComboBox, QMessageBox
import mysql.connector
from mysql.connector import Error
import pandas as pd
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
        self.botaoLProdutos.clicked.connect(lambda: mudar_tela_callback("ListarProduto"))
        # Gerenciador de Produtos
        self.botaoEprodutos = QPushButton("Editar Produtos", self)
        self.botaoEprodutos.setGeometry(550, 140, 150, 80)  
        self.botaoEprodutos.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)
        self.botaoEprodutos.clicked.connect(lambda: mudar_tela_callback("EditarProduto"))

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
        self.botaoLCategorias = QPushButton("Deletar Produto", self)
        self.botaoLCategorias.setGeometry(340, 270, 150, 80)  
        self.botaoLCategorias.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)
        self.botaoLCategorias.clicked.connect(lambda: mudar_tela_callback("DeletarProduto"))
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

class TelaDeletarProduto(QWidget):
    def __init__(self, mudar_tela_callback):
        super().__init__()

        # Configuração geral
        self.setWindowTitle("Deletar Produto")
        self.setGeometry(100, 100, 800, 600)

        # Layout principal
        layout = QVBoxLayout()

        # Campo para código de barras
        self.campo_texto_add_codigo_barras = QLineEdit(self)
        self.campo_texto_add_codigo_barras.setPlaceholderText("Digite o código de barras")
        self.campo_texto_add_codigo_barras.setStyleSheet("""
            border: 1px solid grey;
            border-radius: 5px;
            padding: 5px;
            font-size: 12px;
        """)
        layout.addWidget(self.campo_texto_add_codigo_barras)


        # Botão para salvar
        self.botao_salvar = QPushButton("Salvar", self)
        self.botao_salvar.setGeometry(200, 300, 100, 40)  
        self.botao_salvar.setStyleSheet("""
            color: white;
            background-color: blue;
            border: 2px solid black;
            border-radius: 10px;
            font-size: 14px;
            font-weight: bold;
        """)
        
        self.botao_salvar.clicked.connect(self.salvar_dados)
        layout.addWidget(self.botao_salvar)

        # Botão para voltar
        self.botao_voltar = QPushButton("Voltar para Tela de Produtos", self)
        self.botao_voltar.setStyleSheet("""
            color: white;
            background-color: gray;
            border: 2px solid black;
            border-radius: 10px;
            font-size: 14px;
        """)
        self.botao_voltar.clicked.connect(lambda: mudar_tela_callback("VoltarInicialProdutos"))
        layout.addWidget(self.botao_voltar)

        # Aplicar layout
        self.setLayout(layout)
        
    def salvar_dados(self):
            codigoBarra = self.campo_texto_add_codigo_barras.text()
            try:
                connection = mysql.connector.connect(
                    host='127.0.0.1',         # Endereço do servidor MySQL
                    database='dw',     # Nome do banco de dados
                    user='root',       # Nome de usuário
                    password='server'      # Senha do usuário
                )
            
                if connection.is_connected():
                    print("Conexão com o banco de dados bem-sucedida!")
                    cursor = connection.cursor()
                    
                    # Comando SQL para UPDATE
                    sql_update = f"""
                    Delete from dw.Produto
                    WHERE CodigoBarra = {codigoBarra}
                    """
                    

                    # Executando o comando SQL
                    cursor.execute(sql_update)

                    # Confirmação da atualização
                    connection.commit()

                    # Exibindo mensagem ao usuário
                    QMessageBox.information(
                        self,
                        "Dados deletados!",
                        f"Codigo: {codigoBarra}\n"
                    )
            finally:
                if connection.is_connected():
                    connection.close()
                    print("Conexão com o banco encerrada.")

class TelaEditarProduto(QWidget):
    def __init__(self, mudar_tela_callback):
        super().__init__()

        # Configuração geral
        self.setWindowTitle("Editar Produto")
        self.setGeometry(100, 100, 800, 600)

        self.categorias = ["Eletrônicos", "Alimentos", "Roupas", "Livros"]
        # Layout principal
        layout = QVBoxLayout()

        # Campo para nome do produto
        self.campo_texto_add_produto = QLineEdit(self)
        self.campo_texto_add_produto.setPlaceholderText("Digite o nome do produto")
        self.campo_texto_add_produto.setStyleSheet("""
            border: 1px solid grey;
            border-radius: 5px;
            padding: 5px;
            font-size: 12px;
        """)
        layout.addWidget(self.campo_texto_add_produto)

        # Campo para código de barras
        self.campo_texto_add_codigo_barras = QLineEdit(self)
        self.campo_texto_add_codigo_barras.setPlaceholderText("Digite o código de barras")
        self.campo_texto_add_codigo_barras.setStyleSheet("""
            border: 1px solid grey;
            border-radius: 5px;
            padding: 5px;
            font-size: 12px;
        """)
        layout.addWidget(self.campo_texto_add_codigo_barras)

        # Campo para preço
        self.campo_texto_add_preco = QLineEdit(self)
        self.campo_texto_add_preco.setPlaceholderText("Digite o preço")
        self.campo_texto_add_preco.setStyleSheet("""
            border: 1px solid grey;
            border-radius: 5px;
            padding: 5px;
            font-size: 12px;
        """)
        layout.addWidget(self.campo_texto_add_preco)

        # Campo para quantidade
        self.campo_texto_add_quantidade = QLineEdit(self)
        self.campo_texto_add_quantidade.setPlaceholderText("Digite a quantidade")
        self.campo_texto_add_quantidade.setStyleSheet("""
            border: 1px solid grey;
            border-radius: 5px;
            padding: 5px;
            font-size: 12px;
        """)
        layout.addWidget(self.campo_texto_add_quantidade)

        # Caixa de seleção para categoria
        self.campo_texto_add_categoria = QComboBox(self)
        self.campo_texto_add_categoria.addItems(self.categorias)
        self.campo_texto_add_categoria.setStyleSheet("""
            border: 1px solid grey;
            border-radius: 5px;
            padding: 5px;
            font-size: 12px;
        """)
        layout.addWidget(self.campo_texto_add_categoria)

        # Botão para salvar
        self.botao_salvar = QPushButton("Salvar", self)
        self.botao_salvar.setGeometry(200, 300, 100, 40)  
        self.botao_salvar.setStyleSheet("""
            color: white;
            background-color: blue;
            border: 2px solid black;
            border-radius: 10px;
            font-size: 14px;
            font-weight: bold;
        """)
        
        self.botao_salvar.clicked.connect(self.salvar_dados)
        layout.addWidget(self.botao_salvar)

        # Botão para voltar
        self.botao_voltar = QPushButton("Voltar para Tela de Produtos", self)
        self.botao_voltar.setStyleSheet("""
            color: white;
            background-color: gray;
            border: 2px solid black;
            border-radius: 10px;
            font-size: 14px;
        """)
        self.botao_voltar.clicked.connect(lambda: mudar_tela_callback("VoltarInicialProdutos"))
        layout.addWidget(self.botao_voltar)

        # Aplicar layout
        self.setLayout(layout)
    def salvar_dados(self):
            produto = self.campo_texto_add_produto.text()
            codigo_barras = self.campo_texto_add_codigo_barras.text()
            preco = self.campo_texto_add_preco.text()
            quantidade = self.campo_texto_add_quantidade.text()
            categoria = self.campo_texto_add_categoria.currentText()
            try:
                connection = mysql.connector.connect(
                    host='127.0.0.1',         # Endereço do servidor MySQL
                    database='dw',     # Nome do banco de dados
                    user='root',       # Nome de usuário
                    password='server'      # Senha do usuário
                )
            
                if connection.is_connected():
                    print("Conexão com o banco de dados bem-sucedida!")
                    cursor = connection.cursor()
                    
                    # Comando SQL para UPDATE
                    sql_update = """
                    UPDATE dw.Produto
                    SET descricao = %s, Preco = %s, Quantidade = %s, Categoria = %s
                    WHERE CodigoBarra = %s
                    """
                    valores = (produto, preco, quantidade, categoria, codigo_barras)

                    # Executando o comando SQL
                    cursor.execute(sql_update, valores)

                    # Confirmação da atualização
                    connection.commit()
                    print("Dados atualizados com sucesso!")

                    # Exibindo mensagem ao usuário
                    QMessageBox.information(
                        self,
                        "Dados Atualizados",
                        f"Produto: {produto}\n"
                        f"Código de Barras: {codigo_barras}\n"
                        f"Preço: {preco}\n"
                        f"Quantidade: {quantidade}\n"
                        f"Categoria: {categoria}"
                    )
            finally:
                if connection.is_connected():
                    connection.close()
                    print("Conexão com o banco encerrada.")

class TelaCadastrarProduto(QWidget):
    def __init__(self, mudar_tela_callback):
        super().__init__()

        # Configuração geral
        self.setWindowTitle("Cadastrar Produto")
        self.setGeometry(100, 100, 800, 600)

        # Lista de categorias (substituir por consulta ao banco no futuro)
        self.categorias = ["Eletrônicos", "Alimentos", "Roupas", "Livros"]

        # Layout principal
        layout = QVBoxLayout()

        # Campo para nome do produto
        self.campo_texto_add_produto = QLineEdit(self)
        self.campo_texto_add_produto.setPlaceholderText("Digite o nome do produto")
        self.campo_texto_add_produto.setStyleSheet("""
            border: 1px solid grey;
            border-radius: 5px;
            padding: 5px;
            font-size: 12px;
        """)
        layout.addWidget(self.campo_texto_add_produto)

        # Campo para código de barras
        self.campo_texto_add_codigo_barras = QLineEdit(self)
        self.campo_texto_add_codigo_barras.setPlaceholderText("Digite o código de barras")
        self.campo_texto_add_codigo_barras.setStyleSheet("""
            border: 1px solid grey;
            border-radius: 5px;
            padding: 5px;
            font-size: 12px;
        """)
        layout.addWidget(self.campo_texto_add_codigo_barras)

        # Campo para preço
        self.campo_texto_add_preco = QLineEdit(self)
        self.campo_texto_add_preco.setPlaceholderText("Digite o preço")
        self.campo_texto_add_preco.setStyleSheet("""
            border: 1px solid grey;
            border-radius: 5px;
            padding: 5px;
            font-size: 12px;
        """)
        layout.addWidget(self.campo_texto_add_preco)

        # Campo para quantidade
        self.campo_texto_add_quantidade = QLineEdit(self)
        self.campo_texto_add_quantidade.setPlaceholderText("Digite a quantidade")
        self.campo_texto_add_quantidade.setStyleSheet("""
            border: 1px solid grey;
            border-radius: 5px;
            padding: 5px;
            font-size: 12px;
        """)
        layout.addWidget(self.campo_texto_add_quantidade)

        # Caixa de seleção para categoria
        self.campo_texto_add_categoria = QComboBox(self)
        self.campo_texto_add_categoria.addItems(self.categorias)
        self.campo_texto_add_categoria.setStyleSheet("""
            border: 1px solid grey;
            border-radius: 5px;
            padding: 5px;
            font-size: 12px;
        """)
        layout.addWidget(self.campo_texto_add_categoria)

        # Botão para salvar
        self.botao_salvar = QPushButton("Salvar", self)
        self.botao_salvar.setGeometry(200, 300, 100, 40)  
        self.botao_salvar.setStyleSheet("""
            color: white;
            background-color: blue;
            border: 2px solid black;
            border-radius: 10px;
            font-size: 14px;
            font-weight: bold;
        """)

        self.botao_salvar.clicked.connect(self.salvar_dados)
        layout.addWidget(self.botao_salvar)

        # Botão para voltar
        self.botao_voltar = QPushButton("Voltar para Tela de Produtos", self)
        self.botao_voltar.setStyleSheet("""
            color: white;
            background-color: gray;
            border: 2px solid black;
            border-radius: 10px;
            font-size: 14px;
        """)
        self.botao_voltar.clicked.connect(lambda: mudar_tela_callback("VoltarInicialProdutos"))
        layout.addWidget(self.botao_voltar)

        # Aplicar layout
        self.setLayout(layout)
    
    def salvar_dados(self):
        # Coletar os dados dos campos
        produto = self.campo_texto_add_produto.text()
        codigo_barras = self.campo_texto_add_codigo_barras.text()
        preco = self.campo_texto_add_preco.text()
        quantidade = self.campo_texto_add_quantidade.text()
        categoria = self.campo_texto_add_categoria.currentText()
        try:
        # Configurações de conexão
            connection = mysql.connector.connect(
                host='127.0.0.1',         # Endereço do servidor MySQL
                database='dw',     # Nome do banco de dados
                user='root',       # Nome de usuário
                password='server'      # Senha do usuário
            )
        
            if connection.is_connected():
                print("Conexão com o banco de dados bem-sucedida!")
                cursor = connection.cursor()
                
                sql_insert = """
                INSERT INTO dw.Produto(descricao, CodigoBarra, Preco, Quantidade, Categoria)
                VALUES (%s, %s, %s, %s, %s)
                """
                valores = (produto,codigo_barras,preco,quantidade,categoria)  

                # Executando o comando SQL
                cursor.execute(sql_insert, valores)

                # Confirmação da inserção
                connection.commit()
                print("Dados inseridos com sucesso!")

                QMessageBox.information(
                self,
                "Dados Salvos",
                f"Produto: {produto}\n"
                f"Código de Barras: {codigo_barras}\n"
                f"Preço: {preco}\n"
                f"Quantidade: {quantidade}\n"
                f"Categoria: {categoria}"
            )
        finally:
            if connection.is_connected():
                connection.close()
                print("Conexão com o banco encerrada.")
        
        
class ListarProduto(QWidget):
    def __init__(self, mudar_tela_callback):
        super().__init__()

        # Configuração geral
        self.setWindowTitle("Listar Produto")
        self.setGeometry(100, 100, 800, 600)

        # Layout principal
        layout = QVBoxLayout()

        # Botão para salvar
        self.botaoListar = QPushButton("Listar Produtos", self)
        self.botaoListar.setGeometry(200, 300, 100, 40)  
        self.botaoListar.setStyleSheet("""
            color: white;
            background-color: blue;
            border: 2px solid black;
            border-radius: 10px;
            font-size: 14px;
            font-weight: bold;
        """)
        self.botaoListar.clicked.connect(self.listar_dados)
        
        layout.addWidget(self.botaoListar)

        # Botão para voltar
        self.botao_voltar = QPushButton("Voltar para Tela de Produtos", self)
        self.botao_voltar.setStyleSheet("""
            color: white;
            background-color: gray;
            border: 2px solid black;
            border-radius: 10px;
            font-size: 14px;
        """)
        self.botao_voltar.clicked.connect(lambda: mudar_tela_callback("VoltarInicialProdutos"))
        layout.addWidget(self.botao_voltar)
    
        # Aplicar layout
        self.setLayout(layout)
    def listar_dados(self):
        try:
        # Configurações de conexão
            connection = mysql.connector.connect(
                host='127.0.0.1',         # Endereço do servidor MySQL
                database='dw',     # Nome do banco de dados
                user='root',       # Nome de usuário
                password='server'      # Senha do usuário
            )
        
            if connection.is_connected():
                print("Conexão com o banco de dados bem-sucedida!")
                cursor = connection.cursor()

                # Consulta SQL
                sql_select = "SELECT * FROM dw.Produto"
                cursor.execute(sql_select)
                resultados = cursor.fetchall()

                
                colunas = [desc[0] for desc in cursor.description] 
                df = pd.DataFrame(resultados, columns=colunas)

                QMessageBox.information(
                    self,
                    "Dados",
                    df.to_string(index=False)  
                )
        finally:
            if connection.is_connected():
                connection.close()
                print("Conexão com o banco encerrada.")



        
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
        # Clientes
        self.botaoClientes = QPushButton("Clientes", self)
        self.botaoClientes.setGeometry(-10, 390, 150, 80)  
        self.botaoClientes.setStyleSheet("""
            color: white;                     
            background-color: darkblue;      
            border: 2px solid white;          
            border-radius: 10px;               
        """)
        self.botaoClientes.clicked.connect(lambda: mudar_tela_callback("cliente"))
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
        self.tela_editar_produto = TelaEditarProduto(self.mudar_tela)
        self.tela_deletar_produto = TelaDeletarProduto(self.mudar_tela)
        self.tela_listar_produto = ListarProduto(self.mudar_tela)
        # Adicionar as telas ao stacked widget
        self.stacked_widget.addWidget(self.tela_inicial)
        self.stacked_widget.addWidget(self.tela_inicial_fornecedor)
        self.stacked_widget.addWidget(self.tela_inicial_produto)
        self.stacked_widget.addWidget(self.tela_inicial_cliente)
        self.stacked_widget.addWidget(self.tela_inicial_compra)
        self.stacked_widget.addWidget(self.tela_inicial_vendas)
        self.stacked_widget.addWidget(self.tela_cadastrar_produto)
        self.stacked_widget.addWidget(self.tela_editar_produto)
        self.stacked_widget.addWidget(self.tela_deletar_produto)
        self.stacked_widget.addWidget(self.tela_listar_produto)
        
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
        elif nome_tela == "EditarProduto":
            self.stacked_widget.setCurrentWidget(self.tela_editar_produto)
        elif nome_tela == "DeletarProduto":
            self.stacked_widget.setCurrentWidget(self.tela_deletar_produto)
        elif nome_tela == "ListarProduto":
            self.stacked_widget.setCurrentWidget(self.tela_listar_produto)


# Inicialização do aplicativo
if __name__ == "__main__":
    app = QApplication([])
    gerenciador = GerenciadorDeTelas()
    gerenciador.show()
    app.exec_()
