-- Tabela para operadoras de plano de saúde
CREATE TABLE operadoras_plano_saude (
    registro_ans VARCHAR(20) PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social TEXT,
    nome_fantasia TEXT,
    modalidade TEXT,
    logradouro TEXT,
    numero TEXT,
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    uf VARCHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(3),
    telefone VARCHAR(30),
    fax VARCHAR(30),
    endereco_eletronico TEXT,
    representante TEXT,
    cargo_representante TEXT,
    regiao_comercializacao TEXT,
    data_registro_ans DATE
);

-- Tabela para demonstracoes_contabeis
CREATE TABLE demonstracoes_contabeis (
    data DATE,
    reg_ans VARCHAR(20),
    cd_conta_contabil VARCHAR(50),
    descricao TEXT,
    vl_saldo_inicial NUMERIC(15,2),
    vl_saldo_final NUMERIC(15,2)
);