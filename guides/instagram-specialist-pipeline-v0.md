# Instagram Specialist Pipeline V0

Status: **piloto manual para teste em Codex**.  
Não é automação A2 e não publica.

## Por que existe

O ciclo #031 mostrou um problema de acoplamento: interpretar material, escolher história, definir formato, escrever, dirigir arte, executar e revisar no mesmo passo degrada autoria e torna a correção cara.

V0 separa as decisões.

## Pipeline

```text
SOURCE / EDITORIAL PACKET
        ↓
EDITORIAL STORYTELLER
        ↓
     KELL — STORY GATE
        ↓
INSTAGRAM STRATEGIST
        ↓
 KELL — FORMAT/GOAL GATE
        ↓
FORMAT SPECIALIST
  └─ Instagram Carousel Planner (V0)
        ↓
   KELL — OUTLINE GATE
        ↓
VISUAL STORYTELLER
        ↓
  CREATIVE DIRECTOR
        ↓
 KELL — CREATIVE GATE
        ↓
EXECUTOR
Codex / Canva / PostNitro-like execution layer
        ↓
QA
evidence when needed · accessibility · Flame · readiness
        ↓
 KELL — PUBLISH GATE
        ↓
LEARN-BACK
Audience & Growth Planner
```

## Regras de autoridade

- Storyteller não pensa em slides.
- Instagram Strategist não escreve roteiro final.
- Carousel Planner não desenha.
- Visual Storyteller não muda a história.
- Creative Director simplifica; não cria nova rota.
- Executor implementa decisões aprovadas; não reabre estratégia.
- QA avalia seu escopo; não publica.
- Kell mantém autoria, direção e publicação.

## V0 implementado

Skills:

- `editorial-storyteller`
- `instagram-strategist`
- `instagram-carousel-planner`
- `visual-storyteller`
- `creative-director`

Ainda **não** implementados:

- Single Image Planner;
- Reel Planner;
- orquestrador/plugin;
- execução automática;
- publicação automática.

Se o Instagram Strategist recomendar outro formato, V0 para no gate e registra a necessidade.

## Artefatos intermediários

Preferir:

1. `story-routes.md`
2. `instagram-brief.md`
3. `carousel-outline.md`
4. `visual-direction.md`
5. `creative-preflight.md`
6. design editável / implementação
7. QA / evidence package

Cada etapa recebe o artefato aprovado da anterior. Não recalcula tudo do zero.

## PostNitro como benchmark de execution layer

Princípios aproveitados:

- outline antes do design;
- conteúdo estruturado pode chegar pronto ao executor;
- marca é contexto persistente;
- resultado continua editável.

Não copiar:

- definir quantidade de slides antes da história;
- escolher template como decisão conceitual;
- delegar narrativa + copy + design no mesmo passo.

## Critério para automação futura

Só criar plugin/orquestrador após pelo menos um ciclo real comprovar:

- valor distinto dos especialistas;
- handoffs claros;
- gates não redundantes;
- artefatos intermediários úteis;
- menor retrabalho no executor.

Automação futura deve rotear; não acumular especialidades.
