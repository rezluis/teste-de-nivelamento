# TESTES DE NIVELAMENTO v.250321

## Descrição
Este repositório contém os testes de nivelamento realizados, abrangendo web scraping, transformação de dados, manipulação de banco de dados e desenvolvimento de API.

---

## 1. TESTE DE WEB SCRAPING
### Objetivo
Realizar web scraping utilizando Python ou Java para acessar um site, baixar arquivos PDF e compactá-los.

## 2. TESTE DE TRANSFORMAÇÃO DE DADOS
### Objetivo
Extrair dados estruturados de arquivos PDF e armazená-los em formato CSV.

### Observação
Para realizar o Teste 2, é necessário executar primeiro o Teste 1 para obter os arquivos PDF necessários.

---

## 3. TESTE DE BANCO DE DADOS
### Objetivo
Criar e estruturar tabelas para armazenar dados de demonstrativos contábeis e operadoras de planos de saúde.

---

## 4. TESTE DE API
### Objetivo
Desenvolver uma API e interface web para busca de operadoras de planos de saúde.

---

## Como Executar os Testes
### 1. Teste de Web Scraping
Execute o script `main.py` para baixar e compactar os arquivos PDF.

### 2. Teste de Transformação de Dados
Garanta que os arquivos PDF estejam na pasta correta e execute `extracao_dados.py` para gerar o CSV estruturado.

### 3. Teste de Banco de Dados
- Utilize as queries SQL fornecidas para criar e popular as tabelas no banco de dados.
- Utilize PostgreSQL >10.0 ou MySQL 8+ para execução.

### 4. Teste de API
- Execute `backend.py` para iniciar o servidor.
- Utilize a interface Vue.js (`frontend/`) para interagir com a API.
- Teste as requisições com o Postman.

---

## Autor
Luis Felipe Silva Rezende

