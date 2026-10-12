# #032 — briefing editorial corrigido após auditoria do fluxo

**Estado: pesquisa/curadoria; rascunhos anteriores retirados de revisão final.**
11/10/2026. A tese aprovada permanece aprovada. A seleção de conteúdos, editorias e peças anteriores precisa ser reconstruída. O depoimento de Kell é uma base de autoria e associação, não um sumário da edição.

## Autoridades consultadas

| Fonte | Regra aplicável |
|---|---|
| [Núcleo: curadoria e autoria](https://github.com/eusouakell/cereja-knowledge-system/blob/main/editorial/curation-decisions.md) | A semente da autora inicia pesquisa; procurar descobertas fora dela. Aprovação preserva proveniência. |
| [Núcleo: arquitetura editorial](https://github.com/eusouakell/cereja-knowledge-system/blob/main/editorial/editorial-architecture.md) | Editorias são formatos de entrega, diferentes dos domínios de conhecimento. |
| [Núcleo: mecânica](https://github.com/eusouakell/cereja-knowledge-system/blob/main/editorial/mecanica-editorial.md) | Consultar guias, produzir, verificar, revisar, aprovação, publicar e aprender. |
| [Engine: briefing](../../formats/newsletter/brief-template.md) | Seleção e costura precedem redação; preencher função, fontes, autoria e mídia. |
| [Engine: editorias](../../formats/newsletter/editorias/README.md) | Funções e ritmos distintos; sem quotas de palavras nem presença obrigatória de todas. |
| [Engine: pipeline](../../pipelines/multiformat.md) | Pesquisa → tokens → curadoria → tese/contraponto → história/discoverability → composição → evals → Kell → arquivo. |
| [Engine: especificação](../../SYSTEM-SPEC.md) | Aprovar tese não aprova automaticamente todos os tokens nem as peças por canal. |
| [Factory: integração](https://github.com/eusouakell/agentic-factory/blob/main/integrations/cereja-editorial-engine.md) | Factory fornece capacidades; autoridade editorial permanece no Engine. |
| [Factory: workflow JSON](https://github.com/eusouakell/agentic-factory/blob/main/orchestration/workflows/cereja-editorial.json) | Piloto registra story e quality; não codifica todo o processo editorial e não substitui contratos de domínio. |

Hashes consultados: Engine main 9bdf1bd658552d9cb91f6da2798ef46f6341ceda; Núcleo main bc15fe6f3457462b76da7f556093d6641c0b5fde; Factory main c9200a870d67a32efb7680650b39f206dedf01ad.

## Diagnóstico concreto da execução anterior

1. Transformou o relato semanal no conjunto quase completo de assuntos. Checagem de nomes/links substituiu pesquisa e curadoria.
2. Cherry Bomb virou explicação de arquitetura e do próprio processo da Cereja, sem desenvolver suficientemente um acontecimento externo.
3. ALT+TAB reuniu duas indicações breves em vez de investigar qual objeto merecia desenvolvimento.
4. On Fire foi omitido porque não havia pesquisa selecionada. Isso é falta de execução da busca, não razão editorial de descarte.
5. AiaiAI recebeu um trecho longo de política; sua função de exploração prática ficou diluída.
6. Os textos de outros canais repetiram a costura escolhida prematuramente. Sibling outputs exigem seleção própria de tokens/contexto.
7. Aprovação da tese virou aprovação automática de todos os tokens no packet. Isso contradiz SYSTEM-SPEC.
8. Checks estruturais aprovados e autoavaliação não demonstravam prontidão editorial. O parecer de prontidão do #39 foi retirado.

Não é preciso mudar governança ou criar agentes. É preciso executar o processo já descrito.

## O que Kell trouxe — uso na costura

- Dashboard, bonequinha/carrinho, corrida, gates/intervenções e consumo: possível entrada autoral; não é pauta suficiente nem demo comprovada por esta execução.
- Planning poker, horas/reais com e sem IA: estimativa relatada; sem números ou alegação de economia.
- Aniversário da mãe e bolo buscado com Instinct: contexto humano e exemplo prático; sem expor informações de saúde/finanças.
- Lanternas: finale assistida e reação confirmada. Série candidata; Carrie não abre esta edição e não será repetida por inércia.
- Provas não revisadas: livro recebido, reação e interação; sem afirmar que foi concluído.
- Post sobre assistentes fofos: pista de pesquisa; origem não identificada. “Quanto mais fofo, mais risco” não é conclusão comprovada.

Não publicar a entrevista bruta. Não completar sentimentos ou transformar frases propostas pelo assistente em citações de Kell.

## Pesquisa complementar — shortlist e claim ledger

Consultada em 11/10. Fontes externas são evidência para seleção, não aprovação automática dos assuntos.

| ID | Acontecimento/objeto | Fonte e natureza | O que acrescenta / limite |
|---|---|---|---|
| EV-032-06 | Muse, anunciado pela Meta em setembro | [Anúncio oficial](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) | Agente pessoal atuando entre serviços. Afirmações do fabricante, não desempenho auditado. Não presumir que seja o produto do post visto por Kell. |
| EV-032-07 | Escolhas de avatar, atividade e aprovações no Muse | [How We Designed Muse](https://introducing.muse.ai/), setembro | O relato dos designers relaciona personalidade/avatares a transparência e controles de ações. Fonte concreta para investigar interfaces simpáticas sem alegar que fofura causa risco. |
| EV-032-08 | Proteções de execução e dados no Muse | [Meta: segurança](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse), 08/09 | Descreve isolamento e autoridade de permissões. Design declarado pelo fornecedor; não prova invulnerabilidade. |
| EV-032-09 | Francis Halzen / IceCube, Nobel de Física 2026 | [IceCube](https://icecube.wisc.edu/news/awards/2026/10/francis-halzen-icecube-principal-investigator-wins-2026-physics-nobel-prize/), 06/10 | Sinal científico fora de IA; oportunidade de explicar observação de neutrinos. Não confundir anúncio do prêmio com descoberta ocorrida nesta semana. |
| EV-032-10 | Anne Carson, Nobel de Literatura 2026 | [Academia Sueca](https://www.svenskaakademien.se/nobelpriset/2026), anúncio de 08/10 | Sinal literário fora do relato; oportunidade de curadoria de obra. Não dizer que Kell leu Carson. |
| EV-032-11 | Lanternas | [DC: série](https://www.dc.com/tv/lanterns-2026) + relato de Kell | Apresentação sem spoilers; disponibilidade brasileira ainda a conferir se houver convite para assistir. |
| EV-032-12 | Provas não revisadas | [Editora](https://www.companhiadasletras.com.br/9788535947878-provas-nao-revisadas---um-quebra-cabeca-para-quem-ama-livros-10930/p) + Kell | Objeto interativo para desenvolver, preservando limites de experiência. |
| EV-032-13 | Instinct | [Site](https://instinct.com/) e [política](https://instinct.com/privacy-policy) + Kell | Teste prático; confirmar identidade do serviço antes de linkar indicação. Sem preço/promessas universais. |

URLs Nobelprize.org tiveram erro de acesso; o levantamento encontrou fontes institucionais alternativas. Não inferir ausência de anúncio a partir de falha de fetch. Itens 09/10 têm anúncio institucional localizado em busca, ainda precisam de leitura completa antes de redação científica/literária.

## Mapa de editorias — seleção de trabalho, ainda sem composição final

| Parte | Função canônica | Seleção proposta e pesquisa necessária | Costura possível |
|---|---|---|---|
| Abertura | Presença da autora e entrada na curadoria | Uma cena do dashboard ou do aniversário; curta, sem despejar o diário inteiro | Um detalhe leva ao primeiro acontecimento; não explicar estratégia da edição ao leitor |
| Cherry Bomb | Notícias/descobertas desenvolvidas | Investigar agentes pessoais e as escolhas reais de avatar, transparência e permissão do Muse. Desenvolver o fato externo e seu contraponto | Dashboard/Instinct fornecem experiência situada; Factory/#31 ficam como evidência secundária quando acrescentarem |
| ALT+TAB | Desvio cultural, pessoal ou investigativo | Desenvolver Provas não revisadas: leitura que pede intervenção do leitor. Não usar o livro só como metáfora para agentes | Presente do marido abre o desvio; o mistério tem valor próprio |
| On Fire — UP | Radar e mudança de ritmo | Candidatos de ciência/literatura: IceCube e Anne Carson. Lanternas pode ser indicação breve de séries se esse tratamento respeitar a reação de Kell | Links com contexto curto; marcadores editoriais sem ranking/viralização inventados |
| On Fire — Estou de olho em | Sinal/pergunta com motivo | Design dos assistentes e o post visto por Kell, se for localizado e não duplicar Cherry Bomb; caso contrário selecionar outro sinal | Questão aberta, sem completar opinião da autora |
| Hot Startups | Empresa com motivo concreto para acompanhar | Pesquisa/seleção explícita. Instinct pode ser candidato empresarial somente se houver informação de negócio suficiente e sem duplicar AiaiAI. Não escolhida automaticamente | Decidir inclusão/descarte por valor, não por falta de pesquisa |
| AiaiAI | Recurso prático e primeiro passo | Instinct: tarefa pequena, experiência real, link e restrição relevante concisos | Bolo/lembretes ou cardápio; trecho técnico de política permanece no packet |
| Encerramento | Conversa curta | Escolher depois da composição | Sem moral recapitulando todos os assuntos |

Esse mapa é proposta do assistente para executar os contratos, não nova regra canônica. Editorias podem ser omitidas com motivo de curadoria depois da pesquisa; não são slots obrigatórios. Lanternas não precisa ficar no radar se o desenvolvimento cultural justificar outro arranjo.

## Tokens candidatos com proveniência

- TK-032-MUSE-ANNOUNCEMENT / EV-06: fato externo.
- TK-032-AVATAR-CONTROL / EV-07/08: escolhas de interface e limites, atribuídas ao fornecedor.
- TK-032-ICECUBE / EV-09: candidato científico.
- TK-032-CARSON / EV-10: candidato literário.
- TK-032-BOOK / EV-12 e relato: descoberta e autoria distintas.
- TK-032-SERIES / EV-11 e relato: identificação + reação literal.
- TK-032-INSTINCT-USE / relato: experiência delimitada.
- TK-032-DASHBOARD / relato: entrada autoral possível.

Todos são candidatos para curadoria. A tese aprovada não aprova esses tokens nem suas redações.

## Retomada do fluxo

| Etapa | Estado real nesta correção | Saída necessária |
|---|---|---|
| Guias/contexto | Consultados nos três repos | Referências acima e escopo |
| Signal Scout/Researcher | Shortlist ampliada; fontes institucionais localizadas | Leitura completa, datas/escopo, contraponto e mídia candidata |
| Tokenizer | Candidatos com proveniência | Separar fato, relato, hipótese e interpretação |
| Curator | Mapa proposto; seleção final ainda em trabalho | Justificativas de inclusão/descarte por editoria |
| Thesis Builder/Devil's Advocate | Tese existente preservada | Desafiar complexidade, concentração em IA e autopromoção |
| Story/discoverability | Não transformar cada bloco na mesma história | Percurso, desvios, radar e perguntas de busca próprios |
| Composer | Rascunho v1 retirado | Redação após briefing e seleção completos |
| Channel composition | Textos v1 retirados de prontidão | Contextos/tokens por canal, seleção e capacidade |
| Evals/readiness | Prontidão anterior revogada | Verificação semântica, autoral, direitos, acessibilidade e channel fit |
| Kell/publicação/learn-back | Não executados | Revisão final depois de concretizar composição e avaliação |

Papéis indicam funções do contrato; esta auditoria foi executada pelo assistente, sem alegar agentes independentes ou pipeline automático.

## Critérios da correção

- Descobertas fora do depoimento pesquisadas, com fontes e limites.
- Briefing da edição e briefings por editoria efetivamente usados.
- Cada seção entrega algo diferente e muda ritmo conforme seu material.
- Depoimento sustenta autoria/costura; não determina a cobertura inteira.
- Não transformar o calendário estratégico em quota temática da newsletter.
- Nenhum ready de packet/CI substitui curadoria, voz ou gate de publicação.
- Retomar pesquisa/curadoria antes de pedir nova aprovação editorial.

