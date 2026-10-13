# #032 — pesquisa, seleção, briefing e revisão da recomposição

13/10/2026. Execução autorizada por Kell após merge da correção #39.
**Estado: composição candidata entregue; revisão final de Kell pendente.** Não aprova publicação.
Implementa o briefing v2 e os contratos existentes; não cria uma regra nova para editorias.

## Contexto e autoria

Leitor: audiência curiosa da Cereja, com explicação acessível para quem usa IA no trabalho.
Objetivo: uma curadoria de tecnologia, cultura e ciência; a pauta de Context Engineering informa o percurso principal sem dominar todos os blocos.
Canal/formato: newsletter quinzenal; peças sociais nativas separadas.
Base autoral: relato de Kell em 11/10, tese aprovada e correção explícita sobre uso do depoimento.
Fontes de voz: Núcleo editorial/voice-and-tone.md e curation-decisions.md; Engine brief-template e contratos de Cherry Bomb, ALT+TAB, On Fire e AiaiAI.
Acervo: percursos #002/#029 descritos no guia, usados como referência de variedade; não foi feita nova leitura integral das edições.
Excluídos: clientes/TreeID, notas médicas/financeiras, entrevista bruta, detalhes de familiares, fornecedor não identificado no ditado “cloud”.
A autoria do relato e a redação proposta pelo assistente permanecem distintas.

## Pesquisa executada antes da composição

Fontes lidas/consultadas em 13/10. Fonte institucional não significa avaliação independente do produto.

| ID | Fonte primária | Fato utilizável e limite | Seleção |
|---|---|---|---|
| EV-032-14 | [Thariq Shihipar/Anthropic](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models), 24/07/2026, redireciona para claude.dev | Relato de instruções conflitantes e simplificação de contexto; experiência do fornecedor em coding, sem generalização universal | Cherry Bomb |
| EV-032-04 | [Context Engineering, Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 29/09/2025 | Seleção de informações por etapa | Explicação de apoio, não notícia recente |
| EV-032-05 | [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), 19/12/2024 | Começar simples; tooling histórico tem aviso de atualização | Contraponto |
| EV-032-07 | [How We Designed Muse](https://introducing.muse.ai/), setembro de 2026 | Avatar, atividade e permissões; relato de design dos autores | Segundo objeto, não demonstra risco por fofura |
| EV-032-08 | [Meta: segurança Muse](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse), 08/09/2026 | Autoridade de ação separada; sistema pode errar | Contraponto atribuído |
| EV-032-09 | [IceCube](https://icecube.wisc.edu/news/awards/2026/10/francis-halzen-icecube-principal-investigator-wins-2026-physics-nobel-prize/), 06/10/2026 | Nobel Francis Halzen; atualização com dados esperados em 2026 | Radar científico; prêmio não é descoberta desta semana |
| EV-032-10 | [Academia Sueca](https://www.svenskaakademien.se/nobelpriset/2026) | Nobel Anne Carson e biobibliografia | Radar literário; não dizer que Kell leu |
| EV-032-11 | [DC Lanterns](https://www.dc.com/tv/lanterns-2026) | Hal/John e investigação; reação à finale é de Kell | Séries no radar, sem spoiler; sem promessa de disponibilidade brasileira |
| EV-032-12 | [Companhia das Letras](https://www.companhiadasletras.com.br/9788535947878-provas-nao-revisadas---um-quebra-cabeca-para-quem-ama-livros-10930/p) | Autores, tradutora e leitor-revisor investigando erros | ALT+TAB desenvolvido; sem alegar leitura concluída |
| EV-032-13 | [Instinct](https://instinct.com/) e [política](https://instinct.com/privacy-policy) | Assistente de texto/chamada e regras de dados | Fonte de verificação; experiência WhatsApp é relato de Kell. Domínio segue candidato, sem link no corpo da indicação |
| HS-SEARCH | Busca de fontes institucionais sobre empresa Instinct | Retornou homônimo instinct.xyz/YC de negociação financeira e dados secundários de investimento | Não transferir fundadores/funding de homônimo. Hot Startups omitida por duplicação e falta de dado empresarial verificado |

O post Dot/Meta não foi identificado; Muse não foi declarado como o produto daquele post. A frase “quanto mais fofo, mais risco” não entrou como lei ou dado. Busca de disponibilidade brasileira de Lanternas não deu confirmação suficiente; texto usa página de apresentação e relato, sem indicar assinatura/plataforma ao leitor.

## Seleção e descarte

| Parte | Objeto selecionado | Função e motivo | Costura / unidade candidata |
|---|---|---|---|
| Abertura | Dashboard/carrinho | Entrada autoral breve; não apresentar lista da semana | Carrinho → intervenções → pesquisa de instruções em conflito |
| Cherry Bomb | Relato Anthropic + contexto + Muse | Acontecimento externo concreto, explicação e escolhas de interface; não apenas ensinar Factory | TK-CONFLICT, TK-CONTEXT, TK-COUNTERPOINT, TK-AVATAR |
| ALT+TAB | Provas não revisadas | Desenvolve o livro como experiência de investigação com valor próprio | Presente → papel de revisor → erro como pista; TK-BOOK |
| On Fire — UP | IceCube, Anne Carson, Lanternas | Ciência, literatura e séries em ritmo breve | TK-ICECUBE, TK-CARSON, TK-SERIES |
| On Fire — Estou de olho | IceCube Upgrade | Próximo passo científico com status de expectativa, não outro ensaio de IA | TK-UPGRADE |
| Hot Startups | Omitida após pesquisa | Não repetir Instinct; homônimo e funding não confirmados não sustentam matéria | Descarte registrado |
| AiaiAI | Instinct + cardápio/lembretes | Experiência real e uma tarefa prática; política extensa fica no registro | TK-INSTINCT-USE, TK-TRY-SMALL |
| Encerramento | Livro/tarefa | Conversa curta, sem recapitular tese | Pergunta proposta pelo assistente |

Outros descartes: Carrie (evitar repetição solicitada por Kell); dados de economia estimados sem aferição; demonstração do dashboard sem captura; exemplo #31 no corpo (autorreferência desnecessária para esta versão).
Os tokens são **selecionados pelo assistente para composição candidata**, não aprovados por Kell em bloco. Não registrar seleção editorial como aprovação humana.

## Tese, contraponto e narrativa

Tese de Context Engineering aprovada em 11/10 preservada. Novos exemplos ilustram essa tese, sem atribuir a Kell novos testes.
Contrapontos: simplificação não garante resultado universal; mais estrutura tem custo; aparência e autoridade são questões distintas.
Narrativa do núcleo: objeto vivido → problema concreto de instruções → explicação → outro objeto de design.
Desvio do livro não serve como “prova” de engenharia de contexto. Radar tem job próprio.
Discoverability: título de trabalho aprovado; termos “Context Engineering”, contexto e instruções conflitantes no núcleo; obra/série/autores em seus blocos. Nenhum volume de busca, ranking ou promessa de indexação.

## Mídias

| Posição | Proposta | Estado |
|---|---|---|
| Abertura | Captura/trecho da animação do dashboard | Não recebida/inspecionada; texto funciona sem mídia |
| Livro | Link para página da editora | Sem capa/puzzle copiado |
| Série | Link para apresentação DC | Sem still, trailer embutido ou spoilers |
| Ciência | Link para observatório | Foto não copiada/licenciada nesta execução |

Sem assets novos, voz sintetizada ou publicação. E-mail, app e export visual não renderizados nesta etapa de conteúdo.

## Revisão executada sobre a composição candidata

Revisor: mesmo assistente autor; não é painel independente. Contratos usados: brief-template, editorias, editorial-gates, distinctiveness, voz de Núcleo.

| Critério | Resultado no escopo textual | Limite |
|---|---|---|
| Função das editorias | Cherry desenvolve fato externo; ALT+TAB tem objeto próprio; radar restaurado; AiaiAI curto e aplicável | Seleção/voz final de Kell pendentes |
| Variedade | Ciência, literatura, série e livro não repetem tese | Omissão de Hot Startups justificada |
| Autoria | Carrinho, teste, presente e finale sustentados pelo relato | Redação e associações novas são propostas, não transcrição |
| Honestidade | Estimativas/resultado; expectativa/observação; fabricante/auditoria distintos | Sem validação de números do painel |
| Evidência | Claims ligados às fontes, datas preservadas | Revalidar radar e serviços até 17/10 |
| Rights | Paráfrases curtas e links; nenhum arquivo de terceiros copiado | Novas mídias exigem rights gate |
| Linguagem | Sem inventar emoção/experiência; retirado “não trouxe para esta conversa” do texto de produto | Sem avaliação humana/áudio de voz |
| Canal | Cada composição usa unidades próprias | Sem export/design/gravação |
| Publicação | Pendente | Não substituída por CI |

## Pendências materiais para Kell

- Revisar a redação e as associações propostas; não precisa reaprová-las como tese nova se apenas ajustar voz/seleção.
- Confirmar a identidade do Instinct antes de adicionar URL de indicação. Até lá AiaiAI oferece uma experiência relatada e exercício, sem link presumido.
- Conferir se deseja mídia do dashboard; a ausência não bloqueia leitura do rascunho.
- Capturar baseline disponível antes do lançamento, sem inventar métricas.
- Aprovar publicação apenas depois da revisão final.

## Ordem de execução registrada

Guias/contexto → pesquisa e verificação → tokens com proveniência → inclusão/descarte por editoria → contraponto → costura/discoverability → composição → revisão textual → PR para Kell.
Este registro demonstra trabalho assistido; não afirma que o workflow JSON da Factory executou automaticamente todas as etapas.

Retomada: ler drafts/032-v2.md, este registro e as peças v2. Rascunhos v1 seguem históricos em revisão. Nenhuma publicação/agendamento/merge feito.
