# Guia Codex

## Bootstrap
Leia AGENTS.md global e local, README e decisões. Consulte somente as notas relevantes da memória externa configurada; se inacessível, declare a lacuna. Registre a stack observada, os comandos disponíveis, o estado Git e as alterações de terceiros que devem ser preservadas.

Use scripts/install.py em prévia e depois --apply no destino. A skill ficará em `.agents/skills/vibe-codex/`; o modelo de AGENTS.md exige integração manual se já houver instruções diferentes. Não instale este toolkit dentro do próprio checkout.

## Trabalho completo
Diagnóstico → planejamento com critérios de aceite → implementação → verificação → revisão → entrega com evidências. Os nove fluxos estão em prompts/README.md. Cada entrega registra quais fluxos eram aplicáveis, resultado, limitação e justificativa para os demais. Não aplique cerimônia sem utilidade a uma correção pequena.

Na programação, use skills de domínio realmente relevantes e disponíveis. Superpowers pode ser usado se houver distribuição compatível instalada e revisada; esta edição fornece um fluxo próprio, não inclui nem finge instalar as skills do Superpowers ou da Anthropic. Registre capacidade ausente quando ela afetar o resultado.

## Execução e proteção
Instruções em Markdown não interceptam shell. Hooks de Claude não são transportados automaticamente. Mantenha as permissões efetivas do Codex, testes e CI; regras nativas podem ser avaliadas separadamente na versão instalada. Não altere sandbox ou aprovações para fazer o toolkit funcionar.

Delegação é condicional à autorização e às ferramentas da sessão. Quando disponível, cada tarefa tem arquivos exclusivos, dependências e critério de aceite; integração e commit ficam com um responsável. Sem delegação, as mesmas etapas são executadas sequencialmente com limite explicitado.

## Memória e privacidade
A configuração global pode apontar para Obsidian; não duplique o vault nem inclua caminhos pessoais na distribuição. Leitura não significa aprendizado permanente. Escrita de decisões no vault precisa de autorização específica. O contexto da tarefa e as notas canônicas continuam distintos.

## Qualidade e entrega
Integre os gates pelo fluxo 08, mantenha baseline da dívida sem crescimento silencioso e trate-a pelo fluxo 02. Em TypeScript, camada type-aware separada; em Vue/Svelte, parser/plugin do framework e testes específicos. Não alegue que regras JS/TS cobrem SFC sem validação.
Entregue comportamento alterado, verificações realmente executadas, achados, limitações e próximos passos. Commit, publicação e deploy seguem o escopo autorizado. Não instale todas as ferramentas citadas upstream só porque existem.
