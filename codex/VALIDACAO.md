# Validação da edição Codex — 2026-09-26

- Cinco testes do instalador passaram: prévia sem escrita, aplicação/idempotência, conflito inicial, conflito tardio e recusa de symlink/destino próprio (dois comportamentos compartilham o primeiro teste).
- Integridade: 12 arquivos ESLint (originais e cópias portáteis) com hashes verificados.
- RuleTester original executado: max-lines, no-direct-console, no-direct-data-access passaram com ESLint 10.11.0 e Node 24.19.0.
- Validador da skill: válido.
- Revisão própria de referências, limites, conflitos do instalador e atribuição. Sem revisão independente e sem teste ponta a ponta de uma sessão Codex em projeto consumidor.
- AGENTS.md e skill não são hooks de segurança; não há promessa de bloqueio de comandos nem de descoberta em todas as versões do aplicativo.

## Destino dos nove fluxos nesta adaptação

| Fluxo | Aplicação nesta entrega |
|---|---|
| 01 diagnóstico | Leitura do upstream, versão remota e templates; nenhuma alteração no clone original |
| 02 dívida lint | Não aplicável: distribuição de documentação e scripts, sem baseline de aplicativo |
| 03 revisão | Revisão própria; delegação não solicitada |
| 04 plano | Sequência de adaptação, integração e verificações registrada no guia e nas atualizações de execução |
| 05 ondas | Não aplicável: execução sequencial |
| 06 memória | Integração com fonte externa existente, sem copiar notas |
| 07 lint completo | Configs originais distribuídas; integração de stack ocorre no consumidor, não declarada pronta aqui |
| 08 gates | Assets preservados e RuleTester executado; CI de aplicativo não configurado |
| 09 tamanho | Scripts próprios abaixo de 350 linhas; sem refatoração upstream |

Limites: as skills externas do Superpowers/Anthropic e ferramentas MCP citadas não fazem parte desta distribuição. O instalador faz pré-validação de conflitos; não é uma transação atômica contra falhas de disco ou alterações concorrentes durante a cópia. Usar em projeto sem outro processo escrevendo os mesmos arquivos.
