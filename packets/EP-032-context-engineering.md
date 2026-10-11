# EP-032 — Context Engineering não é escrever um prompt melhor

Preparado em 2026-10-11. Estado: tese aprovada por Kell em 2026-10-11; liberado para composição, publicação pendente.
Tema aprovado na issue #37. A tese foi proposta pelo assistente e aprovada por Kell nesta conversa. Aprovação não altera a proveniência de autoria.

```yaml
id: EP-032
status: ready-for-composition
intent:
  question: "Que informação, decisão e evidência precisam acompanhar um trabalho de IA para que ele continue sem depender da memória de um chat?"
  why_now: "O ciclo #31 deixou artefatos concretos de revisão; o piloto V3 inicia em 12/10."
  audience: "Pessoas que usam IA no trabalho; practitioners e lideranças, com explicação acessível à audiência editorial."
  publication_band: thought-leadership
thesis:
  thesis_ids: [TH-032-PROPOSED]
  approved_thesis: "Trabalhos com IA precisam de contexto relevante, decisões vigentes e limites recuperáveis por etapa; a qualidade disso deve ser avaliada no trabalho concreto."
  open_question: "Como preparar contexto suficiente, atual e autorizado para cada etapa de um trabalho com IA?"
  counterpoint_required: true
context:
  selected_context_ids: [CTX-V3, CTX-VOICE, CTX-ROUTER, CTX-031-REVIEW]
  excluded_context_ids: [CTX-FULL-ARCHIVE, CTX-BUSSOLA, CTX-PRIVATE, CTX-031-SCIENCE]
  exclusion_reasons:
    CTX-FULL-ARCHIVE: "Selecionar exemplos de voz apenas na composição; não carregar todo o acervo."
    CTX-BUSSOLA: "A implementação da Bússola não é evidência necessária para esta edição."
    CTX-PRIVATE: "Não usar clientes, TreeID ou informações privadas."
    CTX-031-SCIENCE: "Não reproduzir alegações científicas de Marte sem nova checagem; o objeto aqui é a revisão editorial."
evidence:
  evidence_ids: [EV-032-01, EV-032-02, EV-032-03, EV-032-04, EV-032-05]
  unresolved_claims:
    - "Não há comparação controlada que atribua ganho de qualidade ou redução de retrabalho ao contexto."
    - "Publicação/aprovação final do Instagram #31 não confirmada neste levantamento."
  stale_or_revalidation_required:
    - "Fontes externas conferidas em 11/10; revalidar alegações materiais até o fechamento em 17/10."
tokens:
  candidate_ids: [TK-032-QUESTION, TK-032-CASE, TK-032-CONTEXT, TK-032-COUNTERPOINT, TK-032-PRACTICE]
  approved_for_composition: [TK-032-QUESTION, TK-032-CASE, TK-032-CONTEXT, TK-032-COUNTERPOINT, TK-032-PRACTICE]
story:
  route_selected: "documentary-case-proposed"
  why_story_or_not: "Uma sequência de artefatos mostra mudanças concretas; não há base para fabricar uma cena pessoal ou atribuir causalidade."
  tension: "O próximo executor sabe qual decisão vale e qual material é apenas hipótese?"
  stakes: "Reabrir decisões, publicar além da evidência ou transferir coordenação rotineira à autora."
  concrete_material: [EV-032-01, EV-032-02]
  expected_result_gap: "O teste propõe reduzir retrabalho, mas os registros disponíveis não medem esse resultado."
  turn: "A revisão registra sequência, escopo factual, tratamento de mídia e pendência humana em um objeto recuperável."
  meaning: "Contexto inclui estado e limites do trabalho; a utilidade deve ser testada, não presumida."
  situated_voice_note: "Caso do sistema editorial da Cereja; não generalizar como prova universal."
  oral_test_note: "Pendente na composição; explicar por um artefato antes de nomear a arquitetura."
discoverability:
  durable_question: "O que é Context Engineering e como organizar contexto para agentes de IA?"
  entities_terms: ["Context Engineering", "engenharia de contexto", "agentes de IA", "proveniência", "memória", "avaliação"]
  lifecycle: evergreen
  canonical_destination: null
  public_proof_links:
    - "https://github.com/eusouakell/cereja-editorial-engine/blob/main/router/context-contract.md"
    - "https://github.com/eusouakell/cereja-editorial-engine/blob/main/growth/cycles/031-mars/review-issue26.md"
formats:
  newsletter: quinzenal-cereja
  linkedin: metapost
  instagram: revista-visual
  stories: research-desk
  medium: null
  devto: null
  youtube: null
constraints:
  voice:
    - "Preservar curiosidade, variedade e ritmo; não transformar todas as editorias em uma mesma tese."
    - "Não inventar vivência, reação ou frase de Kell."
    - "Manter o tema aprovado como título de trabalho; evitar repetir oposição não-é/é ao longo do texto."
  rights:
    - "Preferir explicação própria e diagramas originais; sem screenshots privados ou imagens de terceiros nesta preparação."
    - "Citação direta ou mídia adicional exige registro de direitos por ativo."
  disclosure:
    - "Separar fato, inferência, proposta editorial e hipótese de teste."
  channel_specific:
    - "Pilotos DEV.to e YouTube dependem de substância e capacidade; nenhuma entrega adicional é quota."
human_decisions:
  pending: []
  approved_by: Kell
  approved_at: "2026-10-11"
```

## Proposta editorial para o gate de tese

**TH-032-PROPOSED:** Em trabalhos com IA que atravessam várias etapas, preparar contexto significa decidir quais evidências, instruções, decisões vigentes e limites cada etapa recebe, além de registrar o que mudou para a próxima. A qualidade dessa preparação precisa ser avaliada no trabalho concreto.

Não afirmar que prompt engineering morreu, que modelos fortes dispensam instruções claras ou que uma arquitetura com muitos agentes é necessária. Governança e gates são escolhas do sistema Cereja; não apresentá-los como definição universal do termo.

**Pergunta alternativa:** Como preparar contexto suficiente, atual e autorizado para cada etapa de um trabalho com IA?

## Registro de evidências

| ID | Fonte e verificação | O que sustenta | Limite |
|---|---|---|---|
| EV-032-01 | [Teste especialista #31](../growth/cycles/031-specialist-pipeline-test.md), lido em 11/10 | Há hipótese de melhorar conexão, preservar autoria e reduzir retrabalho; há critérios de teste | Documento de protocolo, sem resultado quantitativo preenchido |
| EV-032-02 | [Revisão de 05/10](../growth/cycles/031-mars/review-issue26.md), lida em 11/10 | Registra sequência definida por Kell, correção de assets ausentes, revisão de leitura e limites factuais | Parecer registrado não é avaliação independente desta execução; aprovação final continuava pendente no arquivo |
| EV-032-03 | [Contrato de contexto](../router/context-contract.md), lido em 11/10 | Define seleção/exclusão, proveniência, decisões e mínimo suficiente para renderers | Contrato de desenho; não prova roteamento automático implantado |
| EV-032-04 | [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 29/09/2025; consultado em 11/10/2026 | Trata contexto como recurso finito e sua curadoria como processo que inclui instruções, ferramentas, dados e histórico | Orientação de engenharia do fornecedor; não valida os resultados da Cereja |
| EV-032-05 | [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), 19/12/2024; consultado em 11/10/2026 | Recomenda começar simples e acrescentar complexidade quando necessária; custo e latência entram na decisão | A própria página avisa que o tooling mudou; usar o princípio, não a lista histórica como recomendação atual |

Não importar os números de Marte para esta pauta. Não usar o preflight de tokens como resultado do #31: pertence a outro corpus e mede tamanho de entrada, sem comprovar qualidade.

## Claim ledger

| Formulação | Classe | Decisão |
|---|---|---|
| A revisão #31 registrou imagens ausentes na pasta de prévia e sua inclusão no repositório | Fato documental, EV-032-02 | Usável com atribuição ao registro |
| O teste #31 reduziu retrabalho | Resultado não medido | Bloqueado |
| Separar contexto, decisão vigente e pendência pode facilitar retomada | Hipótese operacional | Usar como pergunta/proposta, não resultado |
| Mais contexto sempre melhora a resposta | Generalização sem suporte | Bloqueado |
| Bons prompts ainda podem ser suficientes para tarefas simples | Contraponto de engenharia, EV-032-05 | Preservar; não vender arquitetura como obrigação |
| Aprovação humana transforma texto gerado em autoria original de Kell | Contraria Núcleo | Bloqueado; conservar proveniência |

## Tokens candidatos

Selecionados para composição sob a tese aprovada; publicação e redação final permanecem pendentes.

| ID | Unidade e origem | Uso candidato |
|---|---|---|
| TK-032-QUESTION | Pergunta aberta do packet | Abertura e fechamento curto |
| TK-032-CASE | Um registro da revisão #31, EV-032-02 | Exemplo documental, sem narrar emoção ou causalidade |
| TK-032-CONTEXT | Informação necessária por etapa, EV-032-03/04 | Explicação acessível e objeto visual |
| TK-032-COUNTERPOINT | Solução simples e custo de complexidade, EV-032-05 | Contraponto no núcleo do argumento |
| TK-032-PRACTICE | Proposta: fonte vigente, decisão, pendência e próximo passo | Pergunta prática; exemplo ilustrativo claramente identificado |

## Percurso candidato da newsletter

1. Abrir por uma pergunta concreta: o que precisa acompanhar um trabalho para outra pessoa ou agente continuá-lo?
2. Examinar um trecho da revisão #31: o que foi decidido, o que é evidência e o que ainda requer aprovação.
3. Explicar seleção de contexto e estado recuperável; ligar à fonte externa sem transformar o texto em manual da Factory.
4. Trazer o contraponto: uma tarefa curta pode funcionar com instrução clara e pouca infraestrutura.
5. AiaiAI pode oferecer um pequeno exercício de contexto para uma tarefa real do leitor.
6. Selecionar um desvio cultural/radar só se trouxer descoberta própria. Ainda não selecionado; a #32 não precisa ser monotemática.
7. Encerrar com pergunta que o leitor possa aplicar, sem recapitular tudo.

A rota documental substitui a narrativa de “falha → sistema novo → sucesso” enquanto não houver evidência do resultado. Não fabricar depoimentos ou uma história de transformação.

## Revisão desta preparação

Revisão feita pelo mesmo assistente que preparou o packet, por critérios; não constitui parecer de agentes independentes.

- Evidência: claims materiais ligados às fontes; causalidade e ganhos de qualidade retirados.
- Contraponto: tarefa simples e custo de complexidade preservados.
- Autoria: tese proposta identificada; primeira pessoa de Kell não redigida.
- Narrativa: documentos concretos disponíveis; arco de sucesso não demonstrado.
- Discoverability: termos candidatos, sem volume de busca ou trend claim inventado.
- Direitos: nenhum ativo de terceiros copiado; novos ativos seguem gate próprio.
- Estado: ready-for-composition após aprovação explícita de Kell; publicação não autorizada.

## Fontes canônicas e continuidade

- [Issue #37](https://github.com/eusouakell/cereja-editorial-engine/issues/37)
- [Piloto #36](https://github.com/eusouakell/cereja-editorial-engine/issues/36)
- [ADR editorial V3](../docs/decisions/ADR-0001-editorial-growth-model-v3.md), aprovado pelo merge do PR #35
- [Voz em Núcleo](https://github.com/eusouakell/cereja-knowledge-system/blob/main/editorial/voice-and-tone.md)
- [Plano de execução e baseline](../growth/cycles/032-context-engineering.md)

Aprovação: Kell respondeu “sim” à tese resumida nesta conversa em 11/10/2026. Escopo: tese e composição; não publicação. Próximo passo: incorporar o gancho real da semana oferecido por Kell ao briefing, preservar suas palavras e compor nativamente. Não inventar a experiência enquanto o relato não chega.
