-- Tabela Cliente
CREATE TABLE Cliente (
    IDCliente INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    CPF_CNPJ VARCHAR(20) NOT NULL UNIQUE,
    Telefone VARCHAR(15)
);

-- Tabela Fornecedor
CREATE TABLE Fornecedor (
    IDFornecedor INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    CPF_CNPJ VARCHAR(20) NOT NULL UNIQUE,
    Telefone VARCHAR(15)
);

-- Tabela Compra
CREATE TABLE Compra (
    IDCompra INT AUTO_INCREMENT PRIMARY KEY,
    IDProduto INT NOT NULL,
    Quantidade INT NOT NULL,
    PrecoUnitario DECIMAL(10, 2) NOT NULL,
    ValorTotal DECIMAL(10, 2) NOT NULL,
    IDFornecedor INT NOT NULL,
    FOREIGN KEY (IDProduto) REFERENCES Produto(IDProduto),
    FOREIGN KEY (IDFornecedor) REFERENCES Fornecedor(IDFornecedor)
);

-- Tabela Venda
CREATE TABLE Venda (
    IDVenda INT AUTO_INCREMENT PRIMARY KEY,
    ValorTotal DECIMAL(10, 2) NOT NULL,
    IDProduto INT NOT NULL,
    QuantidadeVendida INT NOT NULL,
    ValorUnitario DECIMAL(10, 2) NOT NULL,
    IDCliente INT,
    FOREIGN KEY (IDProduto) REFERENCES Produto(IDProduto),
    FOREIGN KEY (IDCliente) REFERENCES Cliente(IDCliente)
);

-- Tabela Produto
CREATE TABLE Produto (
    IDProduto INT AUTO_INCREMENT PRIMARY KEY,
    Descricao VARCHAR(100) NOT NULL,
    CodigoBarra VARCHAR(20) UNIQUE,
    Preco DECIMAL(10, 2) NOT NULL,
    Quantidade INT NOT NULL
);