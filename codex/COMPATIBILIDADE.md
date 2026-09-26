# Matriz Claude → Codex

| Origem | Adaptação | Estado e limite |
|---|---|---|
| CLAUDE.md | AGENTS.md | Template próprio; preservar global e instruções existentes |
| Marketplace /plugin | Skill local `.agents/skills` | Não são comandos intercambiáveis; terceiros não incluídos |
| Superpowers | Fluxo próprio planejar–implementar–verificar | Não é port integral das skills externas |
| Subagentes em ondas | Tarefas com posse disjunta, integração central | Só quando autorizados e disponíveis; fallback sequencial |
| Hooks PreToolUse/settings.json | Permissões efetivas, CI e regras nativas avaliadas à parte | Hook Claude não instalado; nenhum bloqueio equivalente alegado |
| ESLint/Biome | Templates originais + integração por stack | ESLint testado nesta distribuição; Biome é alternativa, não substitui regras AST customizadas |
| Memória Claude | AGENTS global + memória externa existente | Vault não copiado, leitura seletiva |
| Context7/browser | Ferramentas disponíveis da sessão | Conectores não configurados pelo instalador |
| RTK/Graphify/Ponytail/Caveman/aia-harness | Referência histórica | Nenhum binário/plugin instalado |
| Skills Anthropic/domínio | Seleção das capacidades compatíveis disponíveis | Sem alegação de equivalência ou instalação das 31 skills |

## Documentação oficial consultada em 2026-09-26

- [Instruções AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Skills e descoberta local](https://learn.chatgpt.com/docs/build-skills)
- [Regras de execução](https://learn.chatgpt.com/docs/agent-configuration/rules)

AGENTS.md configura orientação por escopo; skills empacotam procedimentos. Regras de execução têm função distinta e dependem da configuração de confiança e do ambiente. Esta edição não modifica essas permissões.
