CREATE TABLE IF NOT EXISTS usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(15),
    rede_social VARCHAR(100),
    image VARCHAR(255),
    senha VARCHAR(128) NOT NULL
);