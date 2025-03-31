-- 3.5. Query analítica para as 10 operadoras com maiores despesas
-- Último trimestre:
SELECT op.registro_ans, op.nome_fantasia, SUM(dc.vl_saldo_final - dc.vl_saldo_inicial) AS despesas
FROM demonstracoes_contabeis dc
JOIN operadoras_plano_saude op ON dc.reg_ans = op.registro_ans
WHERE dc.descricao ILIKE '%EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
AND dc.data >= NOW() - INTERVAL '3 months'
GROUP BY op.registro_ans, op.nome_fantasia
ORDER BY despesas DESC
LIMIT 10;

-- Último ano:
SELECT op.registro_ans, op.nome_fantasia, SUM(dc.vl_saldo_final - dc.vl_saldo_inicial) AS despesas
FROM demonstracoes_contabeis dc
JOIN operadoras_plano_saude op ON dc.reg_ans = op.registro_ans
WHERE dc.descricao ILIKE '%EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
AND dc.data >= NOW() - INTERVAL '12 months'
GROUP BY op.registro_ans, op.nome_fantasia
ORDER BY despesas DESC
LIMIT 10;
