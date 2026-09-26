# Vibe Coding Toolkit — edição Codex

Adaptação mantida por Marcos Otoni do [Vibe Coding Toolkit de Matheus Gomes](https://github.com/soumatheusgomes/vibe-coding-toolkit), sob licença MIT. Não é produto oficial da OpenAI nem do autor original.

Preserva histórico, licença e templates ESLint. A entrada para Codex é **[codex/GUIA.md](codex/GUIA.md)**; o [README original](README.upstream.md), `docs/` e os templates específicos do Claude permanecem como referência histórica, não como configuração executável do Codex.

## Usar

1. Leia o guia e a [matriz de compatibilidade](codex/COMPATIBILIDADE.md).
2. Execute `python3 scripts/install.py /caminho/do/projeto` para inspecionar a instalação proposta, sem escrever.
3. Execute com `--apply` para copiar a skill local e um modelo de AGENTS.md. Arquivos diferentes já existentes causam recusa antes de qualquer escrita; faça a integração manual preservando as instruções atuais.
4. Abra o projeto no Codex e peça para usar a skill `vibe-codex`. Ela consulta a documentação técnica do projeto e a memória externa configurada antes de implementar.

A instalação não muda configuração global, não instala plugins, não habilita agentes, não configura MCP e não instala dependências. Os gates são integrados à stack pelo fluxo 08 e verificados no projeto destino.

## Conteúdo

- [Nove fluxos adaptados](codex/prompts/README.md): diagnóstico, dívida, revisão, planejamento, ondas, memória, lint, gates e refatoração.
- [AGENTS.md de projeto](codex/templates/AGENTS.md.template): diretrizes, stack, comandos, papéis e convenções.
- Skill própria portátil com os nove fluxos e os templates ESLint preservados.
- Instalador com prévia e proteção contra sobrescrita; testes de idempotência e conflitos.
- [Proveniência](codex/PROVENIENCIA.md) e manifesto de integridade.

Requer Node 20.19+, 22.13+ ou 24+ para os testes ESLint; Python 3.9+ para os scripts.

## Verificar esta distribuição

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_integrity.py
npm ci --ignore-scripts
npm test
```

`npm test` executa os testes RuleTester originais das três regras ESLint. A versão da dependência é fixa no lockfile. Isso verifica a distribuição; não comprova a configuração ou os testes do seu aplicativo.
