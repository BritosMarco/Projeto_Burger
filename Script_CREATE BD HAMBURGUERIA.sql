
CREATE TABLE Clientes (
  id_cliente SERIAL,
  nome varchar(50) NOT NULL,
  sobrenome varchar(50) NOT NULL,
  email varchar(50) NOT NULL,
  telefone int8 NOT NULL,
  usuario varchar(50) NOT NULL,
  senha varchar(50) NOT NULL,
  PRIMARY KEY (id_cliente)
);


CREATE TABLE Enderecos (
  id_endereco SERIAL PRIMARY KEY,
  id_cliente int NOT NULL,
  cep int NOT NULL,
  numero int NOT NULL,
  rua varchar(50) NOT NULL,
  complemento varchar(50) NOT NULL,
  FOREING KEY (id_cliente) REFERENCES Clientes (id_cliente) 
);


CREATE TABLE Forma_pagamento (
  id_pagamento SERIAL PRIMARY KEY,
  id_cliente int NOT NULL,
  numero_cartao int8 NOT NULL,
  cpf int8 NOT NULL,
  nome varchar(50) NOT NULL,
  validade_mes int NOT NULL,
  validade_ano int NOT NULL,
  FOREING KEY (id_cliente) REFERENCES Clientes (id_cliente) 
);

CREATE TABLE Produtos (
  id_produto SERIAL PRIMARY KEY,
  nome varchar(50) NOT NULL,
  descricao TEXT DEFAULT NULL,
  link_img TEXT NOT NULL,
  preco int NOT NULL,
  categoria varchar(50) NOT NULL,
  quantidade int NOT NULL 
);

CREATE TABLE Pedidos (
  id_pedido SERIAL PRIMARY KEY,
  id_cliente int NOT NULL,
  id_endereco int NOT NULL,
  data DATE NOT NULL,
  observacao TEXT DEFAULT NULL,
  valor_total int NOT NULL,
  estado boolean DEFAULT FALSE,
  FOREING KEY (id_cliente) REFERENCES Clientes (id_cliente),
 FOREING KEY (id_endereco) REFERENCES Enderecos (id_eendereco) 
);

CREATE TABLE Pedido_produto (
  id_p SERIAL PRIMARY KEY,
  id_pedido int NOT NULL,
  id_produto int NOT NULL,
  FOREING KEY (id_pedido) REFERENCES Pedidos (id_pedido),
 FOREING KEY (id_produto) REFERENCES Produtos (id_produto) 
);
