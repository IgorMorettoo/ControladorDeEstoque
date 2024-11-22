-- Tabela Cliente
CREATE TABLE Cliente (
    IDCliente INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    CPF_CNPJ VARCHAR(20) NOT NULL UNIQUE,
    Telefone VARCHAR(15) NULL
);

-- Tabela Fornecedor
CREATE TABLE Fornecedor (
    IDFornecedor INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    CPF_CNPJ VARCHAR(20) NOT NULL UNIQUE,
    Telefone VARCHAR(15) NULL
);

-- Tabela Produto
CREATE TABLE Produto (
    IDProduto INT AUTO_INCREMENT PRIMARY KEY,
    Descricao VARCHAR(100) NOT NULL,
    CodigoBarra VARCHAR(20) UNIQUE,
    Preco DECIMAL(10, 2) NOT NULL CHECK (Preco > 0),
    Quantidade INT NOT NULL CHECK (Quantidade >= 0),
    categoria VARCHAR(50)
);

-- Tabela Compra
CREATE TABLE Compra (
    IDCompra INT AUTO_INCREMENT PRIMARY KEY,
    IDProduto INT NOT NULL,
    Quantidade INT NOT NULL CHECK (Quantidade > 0),
    PrecoUnitario DECIMAL(10, 2) NOT NULL CHECK (PrecoUnitario > 0),
    ValorTotal DECIMAL(10, 2) NOT NULL,
    IDFornecedor INT NOT NULL,
    FOREIGN KEY (IDProduto) REFERENCES Produto(IDProduto) ON DELETE CASCADE,
    FOREIGN KEY (IDFornecedor) REFERENCES Fornecedor(IDFornecedor) ON DELETE CASCADE
);

-- Tabela Venda
CREATE TABLE Venda (
    IDVenda INT AUTO_INCREMENT PRIMARY KEY,
    IDProduto INT NOT NULL,
    QuantidadeVendida INT NOT NULL CHECK (QuantidadeVendida > 0),
    ValorUnitario DECIMAL(10, 2) NOT NULL CHECK (ValorUnitario > 0),
    ValorTotal DECIMAL(10, 2) NOT NULL,
    IDCliente INT NULL,
    FOREIGN KEY (IDProduto) REFERENCES Produto(IDProduto) ON DELETE CASCADE,
    FOREIGN KEY (IDCliente) REFERENCES Cliente(IDCliente) ON DELETE SET NULL
);
