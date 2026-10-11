# Ciclo #32 — execução e baseline

Atualizado em 2026-10-11. Estado: tese aprovada; rascunhos e revisão entregues. Nenhuma publicação/agendamento.
Packet: [EP-032](../../packets/EP-032-context-engineering.md). Issue de execução: [#37](https://github.com/eusouakell/cereja-editorial-engine/issues/37).

## Estado e dependências

Cereja PR #35 e Factory PR #37 foram mergeados em 11/10/2026; Factory #36 já estava mergeado. A estratégia V3 e a governança compartilhada estão disponíveis em main. Esta preparação aplica os ADRs existentes; não cria decisão transversal nem altera Bússola.

O tema aprovado é “Context Engineering não é escrever um prompt melhor”. Kell aprovou a tese resumida no packet em 11/10 e autorizou executar a composição após fornecer o relato da semana. O título é de trabalho; a redação final deve evitar repetir títulos e frases por oposição.

## Agenda de produção — BRT

| Prazo | Trabalho | Condição de saída |
|---|---|---|
| 12–14/10 | Conferir evidências #31, capturar baseline disponível, selecionar desvio/radar | Fontes, faltas e proveniência registradas |
| Até 17/10 | Fechar packet e realizar gate de tese/pergunta | Aprovação registrada; claims pendentes removidos ou resolvidos |
| 18/10 | Composição e revisão da newsletter, Note e Stories | Voz, evidência, direitos e leitura revisados |
| 19/10, 06:45 | Newsletter e peças de lançamento | Publicação autorizada por Kell; horário é alvo, não agendamento |
| 20/10 | Instagram | Só produzir/publicar se objeto visual entregar descoberta própria |
| 22/10 | LinkedIn | Implicação profissional completa dentro do post |
| 24/10 | YouTube candidato | Demonstração honesta + capacidade + roteiro/aprovação disponíveis |
| 26/10 | DEV.to candidato | Método reproduzível + exemplo e limites, sem reapresentar a newsletter |
| 01/11 | Learn-back | Resultados observados + esforço + limites de atribuição |

Se a tese não fechar no prazo, registrar o desvio e ajustar o lançamento. Não compensar pendências com claims sem suporte.

## Seleção por canal

| Canal | Job e proposta nativa | Tokens | Decisão atual |
|---|---|---|---|
| Newsletter | Percurso de descoberta: retomar trabalho, examinar artefato, explicar contexto, desafiar complexidade | QUESTION, CASE, CONTEXT, COUNTERPOINT | Rascunho em drafts/032.md |
| Note | Uma pergunta útil sobre o contexto necessário para continuar uma tarefa + link quando existir | QUESTION, PRACTICE | Texto composto; URL de edição ainda não disponível |
| Stories | Objeto da pesquisa, uma pendência/descoberta real e link da edição | CASE, QUESTION | Textos compostos; sem screenshots privados |
| Instagram | Comparar dois handoffs ilustrativos da mesma tarefa: material solto e estado com fonte/decisão/pendência | CASE, CONTEXT, PRACTICE | Candidato; exemplo deve ser marcado como ilustrativo, não teste A/B |
| LinkedIn | Consequência organizacional de decisões que só vivem em chats; mostrar um artefato recuperável | CASE, COUNTERPOINT, PRACTICE | Texto próprio composto |
| YouTube | Percorrer um handoff público e explicar o que o próximo executor precisa saber | CASE, CONTEXT | HOLD: sem capacidade/roteiro demonstrados; data é slot |
| DEV.to | Implementar e validar um manifesto mínimo de contexto, mostrando limites de checks estruturais | CONTEXT, COUNTERPOINT, PRACTICE | HOLD: exemplo executável ainda precisa ser produzido e testado |
| Medium | Não há job distinto necessário neste ciclo | — | Não selecionado |

Não decidir número de slides, estilos ou layout antes do objetivo e da história do Instagram. Nem a seleção acima nem um merge deste PR autorizam publicação.

## Baseline — registro inicial

**Captura real ainda não disponível.** Este quadro registra ausência de evidência, não uma medição concluída. Não há acesso a analytics autenticados nesta execução; números públicos não substituem métricas de conta.

| Superfície | Campos a capturar antes de #32 | Valor em 11/10 | Evidência/status |
|---|---|---|---|
| Substack | Assinantes, novos/cancelados no período, entregas, aberturas/cliques com denominador, replies, referrals disponíveis | null | Não coletado |
| Instagram | Seguidores, alcance, envios/shares, saves, visitas, ações de perfil/link; período e denominador | null | Não coletado; publicação flagship #31 não confirmada |
| LinkedIn | Seguidores, impressões, interações substantivas, cliques disponíveis; janela e denominador | null | Não coletado |
| Site | Visitas, origem, cliques/assinaturas instrumentadas, cobertura do rastreamento | null | Não coletado |
| Autoridade | Convites, colaboração, inbound qualificado, citações; data e evidência | null | Não coletado; ausência de coleta não significa zero |
| Produção #31 | Tempos, rounds, intervenções e mudanças de Kell | null | Documentos mostram revisões, sem série quantitativa consolidada |

Formato de cada captura: `data_hora_BRT / período / métrica / valor / denominador / origem / limitações`.
Usar exportação ou leitura autorizada da conta; não solicitar credenciais. Guardar dados detalhados/identificáveis fora do repo público. Registrar aqui apenas agregados adequados.

Assinaturas líquidas: base final menos base inicial; registrar entradas e cancelamentos separadamente quando disponíveis. Atribuição só quando a origem for observável. Não somar saves, replies e views como uma medida única de profundidade.

## Registro operacional iniciado

| Evento | Classe | Evidência |
|---|---|---|
| 11/10: autorização “pode executar” | Início de preparação | Conversa atual; não equivale a aprovação da nova tese |
| 11/10: recuperação de PRs/issues e artefatos #31 | Preparação interna | Fontes identificadas no packet |
| 11/10: troca do arco de sucesso por caso documental | Revisão interna por critérios | Ganhos de qualidade/retrabalho não medidos |
| Gate de tese/pergunta | Intervenção humana planejada | Aprovado por Kell em 11/10 nesta conversa |
| Revisão final/publicação | Intervenção humana planejada | Pendente |

Tempos, número total de rounds e esforço de Kell: não medidos. Não registrar zero nem apresentar esta revisão do mesmo assistente como convergência independente de especialistas.

Para cada intervenção futura, registrar: planejada/inesperada, etapa, motivo, mudança pedida, rodada e tempo se medido. Para learn-back: publicação real, objetos usados/removidos, mudanças de Kell, claims retirados, resultados por canal e decisão sobre os pilotos.

## Handoff imediato

1. Kell revisa drafts/032.md e as pendências de growth/cycles/032-brief-and-review.md; tese já aprovada.
2. Capturar baseline disponível antes do lançamento; continuar pesquisa/composição sem inventar valores faltantes.
3. Desvios selecionados do relato: Lanternas e Provas não revisadas. Confirmar temporalidade e identidade de Instinct antes de fechar.
4. Newsletter, LinkedIn, Note e Stories compostos; revisar voz/redação final com Kell.
5. Resolver fit/capacidade de Instagram, YouTube e DEV.to; cancelar slots sem valor distinto.
6. Kell decide a publicação; registrar URLs e timestamps reais só depois.


## Entrega de composição — 11/10

- [Newsletter](../../drafts/032.md)
- [Peças por canal](032-channel-drafts.md)
- [Briefing e revisão](032-brief-and-review.md)

Abertura usa dashboard do relato autoral. Estimativas não são apresentadas como economia realizada. Post sobre assistentes fofos excluído até localizar fonte. Publicação permanece pendente; baseline não coletado. Revisão feita pelo assistente autor, sem alegar painel independente.
