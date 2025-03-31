-- 3.4. Importação dos dados CSV
COPY operadoras_plano_saude 
FROM 'C:\Users\luis felipe\workspace\teste-de-nivelamento\teste 3\Relatorio_cadop.csv'
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demonstracoes_contabeis 
FROM 'C:\Users\luis felipe\workspace\teste-de-nivelamento\teste 3\2024\1T2024.csv' 
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demonstracoes_contabeis 
FROM 'C:\Users\luis felipe\workspace\teste-de-nivelamento\teste 3\2024\2T2024.csv' 
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demonstracoes_contabeis 
FROM 'C:\Users\luis felipe\workspace\teste-de-nivelamento\teste 3\2024\3T2024.csv' 
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demonstracoes_contabeis 
FROM 'C:\Users\luis felipe\workspace\teste-de-nivelamento\teste 3\2024\4T2024.csv' 
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demonstracoes_contabeis 
FROM 'C:\Users\luis felipe\workspace\teste-de-nivelamento\teste 3\2023\1T2023.csv' 
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demonstracoes_contabeis 
FROM 'C:\Users\luis felipe\workspace\teste-de-nivelamento\teste 3\2023\2t2023.csv' 
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demonstracoes_contabeis 
FROM 'C:\Users\luis felipe\workspace\teste-de-nivelamento\teste 3\2023\3T2023.csv' 
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demonstracoes_contabeis 
FROM 'C:\Users\luis felipe\workspace\teste-de-nivelamento\teste 3\2023\4T2023.csv' 
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

