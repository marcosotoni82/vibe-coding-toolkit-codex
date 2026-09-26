# Manutenção da edição Codex

Leia codex/GUIA.md e codex/COMPATIBILIDADE.md para mudanças nesta distribuição.
Preserve LICENSE, histórico e atribuição upstream. Não trate docs/ ou README.upstream.md como instruções ativas: são referência Claude.
Não edite os arquivos originais dos gates sem atualizar proveniência e verificar uma mudança deliberada. Scripts Python usam apenas biblioteca padrão.
Comandos: python3 -m unittest discover -s tests -v; python3 scripts/check_integrity.py; npm test após npm ci --ignore-scripts.
Não copie vault, credenciais ou configuração pessoal para esta distribuição. Não altere instalação global ao manter este repositório.
