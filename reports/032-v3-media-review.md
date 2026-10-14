# #032 — mídias e assinatura da v3

Aditivo à v3 já incorporada pelo PR #41. Preserva editorias, texto e voz; acrescenta dois vídeos, uma imagem, um GIF e assinatura ao fim do corpo.

## Seleção e direitos

| Mídia | Origem | Uso / crédito |
|---|---|---|
| IC 348 pelo Webb | https://esawebb.org/images/weic2619a/ | CC BY 4.0; ESA/Webb, NASA, CSA, K. Luhman, C. Alves De Oliveira, M. Zamani (ESA/Webb). Política: https://esawebb.org/copyright/ |
| Anã marrom animada | https://www.jpl.nasa.gov/images/pia21752-brown-dwarf-weather-artists-concept/ | Conceito artístico de 2017, não observação de IC 348. NASA/JPL-Caltech. Política: https://www.jpl.nasa.gov/jpl-image-use-policy/ . GIF hospedado no Wikimedia Commons. |
| Demonstração Muse | https://www.youtube.com/watch?v=wHn0hTjvFoo | Player oficial indicado por https://introducing.muse.ai/ ; crédito Muse/Meta. Sem download ou republicação. |
| Teaser Lanternas | https://www.youtube.com/watch?v=nAD5MIjwCEE | Canal oficial WarnerPlay; crédito WarnerPlay/HBO Max. Sem download ou republicação. |

Imagens têm texto alternativo; créditos acompanham cada asset; imagem Webb preserva proporção. Players não iniciam automaticamente; links diretos acompanham ambos.

## Inserção no Substack e validação

O Markdown contém imagens e iframes para a prévia HTML. No editor Substack, colar cada URL YouTube numa linha vazia para gerar o bloco nativo: não colar iframe como texto. Inserir imagem e GIF nos mesmos pontos com as legendas e os créditos.

Referência oficial: https://support.substack.com/hc/en-us/articles/360037832971-How-do-I-embed-media-in-my-post-e-g-images-video-GIFs

A prévia HTML contém os players incorporados e links de alternativa. Validação em 13/10/2026: ambos os vídeos existem nos canais oficiais e oferecem a opção Incorporar com iframe gerado pelo próprio YouTube. Muse reproduziu na prévia incorporada (0:16 de 2:37, com legendas e cenas avançando). Lanternas reproduziu na página oficial (0:13 de 2:27, com legendas e cenas avançando); sua prévia de incorporação carregou título/thumbnail em modo de privacidade, mas depois ficou preta e não permitiu confirmar reprodução dentro do iframe nesse navegador. Não declarar reprodução de Lanternas no embed ou dentro do Substack validada. O erro 153 anterior ocorreu ao abrir o endereço de iframe diretamente, sem Referer. Conferir reprodução no bloco nativo do Substack e enviar e-mail de teste antes de publicar. Vídeos precisam de alternativa clicável no e-mail. Nenhum teste de envio, agendamento ou publicação foi realizado.

## Rodapé observado em 13/10/2026

Inspeção autenticada, somente leitura, em https://cerejaflamejante.substack.com/publish/settings/preamble .

“Rodapé para todos os posts”:
- Imagem da chama.
- “A newsletter para explodir a sua mente. 🍒”
- “Curadoria interessante e divertida sobre cultura e tecnologia.”
- “Produzida por” — nome não visível na prévia de configurações. A inspeção posterior do editor revelou uma menção a “eusouakell”, em vez de ausência de autor.
- “Curtiu a edição de hoje?” e “Me conta!” apontando para https://tally.so/r/w4B0jX .

O rodapé do site tem © 2026 Kell Bonassoli e links institucionais. É distinto do rodapé configurado para os e-mails.

A assinatura **Kell Bonassoli** agora fecha o corpo da edição, acompanhando cópias e encaminhamentos. Após autorização explícita da autora, a configuração global foi salva com “Produzida por Kell Bonassoli” em texto normal. Chama, descrição e link “Me conta!” preservados. A prévia de configurações após salvar mostra o nome completo. Evidência local: outputs/substack-rodape-kell.jpg . Nenhum post publicado ou agendado.
