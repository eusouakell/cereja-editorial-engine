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



## Progressive disclosure de contexto

Cada especialista recebe o **menor pacote de contexto suficiente** para sua decisão. Mais contexto não é automaticamente melhor: alternativas já rejeitadas, decisões de etapas futuras e documentos de execução podem induzir o agente a reabrir gates ou misturar papéis.

### Pacote por etapa

| Etapa | Recebe | Não recebe por padrão |
|---|---|---|
| Editorial Storyteller | fonte/editorial packet + evidências + contrato da skill | estratégia Instagram, outline, Flame visual, carrossel anterior como resposta |
| Instagram Strategist | história aprovada + estratégia Instagram + contrato da skill | direção visual, layout, copy final, alternativas narrativas rejeitadas |
| Carousel Planner | história aprovada + brief de objetivo/formato + contrato de carrossel | direção de arte, template, execução |
| Visual Storyteller | outline aprovado + objetivo/formato aprovado + Flame aplicável + contrato visual | rotas narrativas rejeitadas, redecisão de formato |
| Creative Director | artefatos aprovados + direção visual + Flame aplicável | liberdade para inventar nova rota ou novo objetivo |
| Executor | decisões aprovadas + tokens/componentes/ativos necessários | estratégia aberta, alternativas antigas, autoridade editorial |
| QA | saída executada + contratos específicos do que está sendo verificado | contexto irrelevante ao check/eval |

### Regra de gate

Depois que Kell aprova um gate, a etapa seguinte recebe **a decisão aprovada**, não o conjunto completo de alternativas.

Uma etapa só pode reabrir decisão anterior quando encontra:

- contradição explícita;
- requisito necessário ausente;
- conflito factual, de direitos ou acessibilidade;
- inviabilidade real de execução;
- mudança de uma fonte canônica;
- pedido explícito de Kell.

Fora desses casos, reabrir estratégia é **falha de boundary**.

### Hierarquia de autoridade

Quando houver dúvida:

```text
artefato aprovado da etapa anterior
→ Núcleo / Flame aplicável
→ contrato do canal/formato
→ contrato do especialista
→ referência externa / ferramenta
```

Referência externa e skill de execução não podem substituir uma decisão canônica ou aprovada.

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
