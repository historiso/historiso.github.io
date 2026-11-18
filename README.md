# Portfólio Carlos Raimundo · v1 (português)

Site estático, sem build obrigatório. Abra `index.html` para ver localmente.

## Publicar (grátis, GitHub Pages)
O site fica num repositório do GitHub chamado `historiso.github.io` e vai ao ar em `https://historiso.github.io`.
Para atualizar: salve as mudanças, faça commit e push na branch `main`. Em 1 ou 2 minutos o site atualiza.

## Showreel
Fica em `assets/video` (mudo, em loop no topo da Home, e em tela cheia no botão "Ver showreel").
Para trocar, gere os arquivos com o mesmo nome a partir do vídeo novo:
- `showreel-1080.mp4` (computador), `showreel-720.mp4` (celular), `showreel-poster.jpg` (imagem enquanto carrega).

## Formulário de orçamento
Usa o FormSubmit, que envia para decupalm@gmail.com. No primeiro envio chega um e-mail de ativação nessa caixa: clique para ativar. Se o envio falhar, o site abre o app de e-mail com a mensagem pronta.

## Adicionar ou retirar vídeos
Tudo fica em `assets/js/data.js`. Cada vídeo é uma linha com o id do YouTube (o código depois de `watch?v=` ou `shorts/`). Não precisa rodar nada: salve e publique de novo.

## Mudar textos das páginas
Os textos ficam em `build.py`. Depois de editar, rode `python3 build.py` para gerar as páginas.

## Versão em inglês
Já está preparada: os vídeos têm campos `en` em `data.js` e `build.py` tem os textos da navegação em inglês.
Para lançar: escrever os textos `en` de cada página em `build.py`, mudar `BUILD_EN = True` e rodar o script. As páginas saem em `/en`.

## Pendências
- O vídeo `l5r6pTkexrU` (Ponto de Vista, a confirmar) está com incorporação bloqueada ou privado no YouTube. Libere em YouTube Studio > Detalhes > Mais opções > Permitir incorporação.
- Domínio definitivo e `SITE_URL` em `build.py`.
