# #031 — Specialist Pipeline Test

Status: teste V0 em Codex.  
Objetivo: validar a nova separação de especialidades **sem alterar o post publicado ou o carrossel existente** até Kell aprovar cada gate.

## Fonte

Usar a edição #031 e suas fontes já registradas no ciclo atual.

Não usar o carrossel final como resposta a copiar. Ele serve apenas como histórico de aprendizado.

## Hipótese do teste

Separar história → estratégia Instagram → outline → direção visual deve:

- melhorar a conexão Marte/batatas;
- reduzir texto;
- evitar template/deck;
- reduzir retrabalho;
- preservar melhor a reação real de Kell.

## Rodada 1 — Storyteller apenas

Executar `editorial-storyteller`.

Entregar 3 rotas narrativas.

Não mencionar número de slides, layout, cor, fonte, HTML ou template.

Parar no STORY GATE.

### Material autoral a preservar como possibilidade, não como resposta obrigatória

Kell explicitou caminhos como:

- “Dá pra plantar batatas em Marte?”
- “Descobriram água em Marte!” → reação: “Oba, vou plantar batatas.”
- contar a descoberta e depois conectar com `Perdido em Marte`;
- fechar de modo circular com o filme/pergunta, sem afirmar viabilidade que a evidência não sustenta.

## Rodada 2 — somente após escolha de Kell

Executar `instagram-strategist`.

Decidir objetivo primário, comportamento e formato.

Parar no FORMAT/GOAL GATE.

## Rodada 3 — somente se formato aprovado = carrossel

Executar `instagram-carousel-planner`.

A história determina o comprimento.

Casa Cereja para carrossel:
- capa 1;
- capa 2;
- frames intermediários necessários;
- fechamento + CTA.

Parar no OUTLINE GATE.

## Rodada 4

Executar `visual-storyteller`.

Meta: imagem carrega a história; texto ancora.

Parar para `creative-director`, depois CREATIVE GATE de Kell.

## Métricas de qualidade do teste

Registrar:

- quantas vezes Kell pediu mudança de história;
- quantas vezes Kell pediu mudança de ordem;
- quantos frames foram removidos por excesso;
- texto aproximado por frame;
- quantas decisões o executor precisou inventar;
- principais falhas de boundary;
- tempo/retrabalho percebido;
- avaliação final de Kell.

## PASS do experimento

O pipeline passa se:

1. Kell consegue escolher uma história antes de ver design;
2. o planner não reabre a história;
3. o Visual Storyteller reduz texto em vez de acrescentá-lo;
4. o executor recebe decisões suficientes para não atuar como estrategista;
5. o resultado é claramente melhor ou o teste produz evidência concreta de qual especialista não agrega valor.
