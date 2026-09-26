# Instalação dos gates

Use somente assets/eslint desta skill (ou templates/eslint no checkout revisado). Copie eslint-rules/*.cjs e verify.mjs byte a byte para uma pasta de ferramentas do projeto. Integre imports/config e adicione comando persistente lint:verify-rules chamando node verify.mjs com caminho explícito do plugin. Preserve o verificador. Dependência ESLint precisa ser compatível e fixada; não use latest. Execute RuleTester antes de lint; integre ambos no CI existente quando dentro do escopo. Configure teto de 350 linhas, acesso ao banco e logger conforme camadas reais. Gere baseline rastreável para código existente; não desligue gates para mascarar falha. Registre resultado dos três gates, integridade, CI e exceções. Não alegue 5/5 sem definir e medir os cinco critérios.

## Evidência de conclusão

Registre o que foi feito, os comandos realmente executados e seus resultados, pendências e justificativas. Uma instrução escrita não comprova execução.
