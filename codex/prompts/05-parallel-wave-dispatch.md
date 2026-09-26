# Execução em ondas

Confirme autorização e ferramentas de delegação. Sem elas, execute sequencialmente. Para cada tarefa descreva Files, Depends-on, Owner e critério de aceite. Uma onda só contém conjuntos de escrita disjuntos; manifests/lockfiles e integração têm um único dono. Subagentes reportam mudanças/testes sem commit concorrente. O integrador verifica diff e testes cruzados antes de iniciar dependentes. Não criar novas tarefas do usuário para simular subagentes.

## Evidência de conclusão

Registre o que foi feito, os comandos realmente executados e seus resultados, pendências e justificativas. Uma instrução escrita não comprova execução.
