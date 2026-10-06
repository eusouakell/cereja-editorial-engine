# #031 — QA da execução

Data: 06/10/2026. Estado: **PASS para revisão humana; KELL — PUBLISH GATE pendente.** Não publicar nem agendar.

## Autoridades

Execution Gate aprovado por Kell após revisão externa de `51efd68`. Copy exata da revisão de Kell; direção única da Rodada 4 consolidada; Rodada 5 preservada como REVISE histórico com revisões incorporadas. Nenhuma skill alterada. A aprovação de execução não aprova automaticamente assets ou publicação.

## Evidence / fatos e direitos

- Fonte NASA/JPL do achado conferida: mais de 185 alvos de rocha, sinais de interação antiga com água. Nenhum mapa ou gráfico dos alvos foi inventado. O panorama do 1 contextualiza o local, sem servir de prova mineral.
- Fonte NASA Kennedy conferida: foto do experimento terrestre Norland em 1992; hidroponia; interesse da Frito-Lay; possibilidades de cultivo em ambiente protegido, com desafios de água, luz, radiação e pressão. A legenda proposta explicita condições e testes terrestres, sem afirmar batatas já cultivadas em Marte.
- Créditos dos itens conferidos: NASA/JPL-Caltech/MSSS para panorama; NASA para experimento; NASA/JPL para captura de título. Nenhuma pessoa, marca d'água ou indicação de copyright de terceiro identificada nos itens selecionados. Uso previsto: editorial informativo orgânico com crédito, sem endosso. A revisão não libera mídia paga ou merchandise.
- Os dois assets gerados foram reinspecionados antes da seleção técnica, com justificativas e hashes na provenance. São interpretação/recorte, não documentos NASA, imagens oficiais do filme ou prova científica. Originais exploratórios preservados sem aprovação retroativa.
- Legenda: proposta do assistente, pendente de aprovação humana; “nossa amada ciência” é expressão fornecida por Kell nesta revisão. Copy visível: cinco formulações escritas por Kell nesta revisão, sem atribuição retroativa de versões anteriores.

Fontes primárias:

- [NASA/JPL — achado](https://www.nasa.gov/solar-system/planets/mars/nasa-discovery-reveals-complex-water-systems-on-early-mars/)
- [NASA Kennedy — cultivo](https://www.nasa.gov/science-research/nasa-plant-researchers-explore-question-of-deep-space-food-crops/)
- [NASA — uso de mídia](https://www.nasa.gov/nasa-brand-center/images-and-media/)

## Accessibility / verificações executadas

- Cinco PNGs 1080 × 1350, copy comparada palavra/pontuação/caixa com o handoff. Imagens carregadas, caixas e ranges de texto dentro das margens, sem corte. Relatório: `render-check.json`.
- Texto editorial com largura de 390 px: mínimos por frame de 23,5 / 19,9 / 20,2 / 20,9 / 17,3 px. No 5, 17,3 px corresponde ao convite secundário; a resposta principal fica maior. Não houve redução de tipografia para acomodar conteúdo.
- Créditos: cerca de 12,3 px na largura de 390 px, legíveis na simulação. Reconferir após compressão/upload.
- Contraste calculado: ink/canvas 11,37:1; ink/lime 8,08:1; action.cherry/canvas 6,33:1. Texto essencial sobre áreas limpas, sem depender de cor.
- Alt de cada PNG escrito a partir da composição executada, incluindo texto essencial e estatuto da mídia. Ilustração conceitual não recebe descrição de fotografia documental.
- Preview conferido em 320, 390 e 768 px, inclusive com painel de leitura aberto: sem rolagem horizontal; alt presente; foco visível na navegação por Tab. PNGs estáticos, sem motion.
- Simulações e checks não equivalem a teste com pessoas ou certificação integral WCAG. Não houve teste em aparelho físico ou upload para Instagram neste gate.

## Flame / revisão independente

Revisor: agente `creative_director_round5`, em QA delimitado da execução atual. Parecer: **PASS para revisão humana**, sem alterar o REVISE histórico. Inspecionou conjunto e cinco imagens de 390 px; não editou copy, direção ou arquivos.

- 1: recorte atravessa margem branca, montagem assumida.
- 2: documento legível, sem evidência ou visualização fabricada dos 185 alvos.
- 3: cultivo + abrigo, sem pessoa, panorama espacial ou quase-still.
- 4: foto documental domina e preserva batatas, raízes, bandejas e aparato. “Na Terra” explícito; Frito-Lay subordinada.
- 5: retorno menor do mesmo objeto, respiro e ausência de marca gráfica. Sem CTA de assinatura.
- Composições e densidades distintas; sem deck, cartões, logos em sequência, rodapé universal ou repetição decorativa intermediária da batata.

Papéis Flame existentes preservados. Georgia/Arial são os fallbacks disponíveis, não novas fontes canônicas. Sem mudança de identidade ou tokens.

## Readiness / pendências reais

1. Kell aprovar visualmente os cinco frames, a legenda proposta e os alt texts no Publish Gate.
2. Na etapa posterior de upload autorizada, inserir alt por imagem e reconferir créditos, quebras e legibilidade na prévia da plataforma. Publicar somente com a legenda qualificadora aprovada, porque o frame 5 a promete.

Não há blocker técnico identificado nesta exportação. Nenhuma estimativa de conversão, compreensão pública ou performance é afirmada. Artefatos do pacote e links locais conferidos; resultados em `qa-checks.json`.
