#!/usr/bin/env python3
"""Gera as páginas estáticas do portfólio.

Uso:  python3 build.py
- Gera as páginas em português na raiz.
- A versão em inglês já está preparada: preencha os textos "en" abaixo,
  mude BUILD_EN para True e rode de novo. Ela sai na pasta /en.
- Os vídeos ficam em assets/js/data.js e não exigem rodar este script.
"""
import os, html, hashlib

BUILD_EN = False
SITE_URL = "https://historiso.github.io"
OUT = os.path.dirname(os.path.abspath(__file__))
def ver(rel):  # muda quando o arquivo muda: evita que o navegador use versão antiga
    with open(os.path.join(OUT, rel), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]
FONTS = "https://fonts.googleapis.com/css2?family=Anybody:wdth,wght@50..150,300..900&family=Hanken+Grotesk:wght@400;500;600;700&family=VT323&display=swap"

T = {
  "pt": {
    "nav_work": "Trabalhos", "nav_about": "Sobre", "nav_services": "Serviços", "nav_quote": "Orçamento",
    "skip": "Pular para o conteúdo", "menu": "Abrir menu", "close": "Fechar",
    "foot_big": "Vamos filmar?", "foot_cta": "Fale comigo", "foot_nav": "NAVEGAÇÃO", "foot_contact": "CONTATO",
    "foot_insta": "Instagram", "foot_autoral": "Autorais e Decupalm", "foot_place": "Goiânia, Brasil",
    "foot_rights": "Carlos Raimundo · filmmaker e editor",
  },
  "en": {
    "nav_work": "Work", "nav_about": "About", "nav_services": "Services", "nav_quote": "Get a quote",
    "skip": "Skip to content", "menu": "Open menu", "close": "Close",
    "foot_big": "Let's shoot?", "foot_cta": "Talk to me", "foot_nav": "NAVIGATION", "foot_contact": "CONTACT",
    "foot_insta": "Instagram", "foot_autoral": "Original work and Decupalm", "foot_place": "Goiânia, Brazil",
    "foot_rights": "Carlos Raimundo · filmmaker and editor",
  },
}

def page_url(fn, lang="pt"):
    path = ("" if lang == "pt" else "en/") + ("" if fn == "index.html" else fn)
    return f"{SITE_URL}/{path}"

def head(lang, title, desc, prefix, fn="index.html", extra=""):
    og = (SITE_URL + "/assets/img/og.jpg") if SITE_URL else f"{prefix}assets/img/og.jpg"
    url = page_url(fn, lang)
    return f"""<!DOCTYPE html>
<html lang="{'pt-BR' if lang=='pt' else 'en'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">{GSC_META}
<meta name="author" content="Carlos Raimundo">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Carlos Raimundo · Filmmaker e editor">
<meta property="og:locale" content="{'pt_BR' if lang=='pt' else 'en_US'}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B0612">{extra}
<link rel="icon" href="{prefix}assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/css/site.css?v={ver("assets/css/site.css")}">
</head>
<body>
<a class="skip" href="#conteudo">{T[lang]['skip']}</a>
"""

def nav(lang, current, prefix):
    t = T[lang]
    items = [("trabalhos.html", t["nav_work"], "work"), ("sobre.html", t["nav_about"], "about"), ("servicos.html", t["nav_services"], "services")]
    cur = ' aria-current="page"'
    links = "".join(f'<a href="{h}"{cur if k==current else ""}>{l}</a>' for h, l, k in items)
    return f"""<header class="nav"><div class="wrap">
  <a class="brand" href="index.html" aria-label="Carlos Raimundo, início"><i aria-hidden="true"></i>Carlos Raimundo</a>
  <button class="menu-btn" aria-label="{t['menu']}" aria-expanded="false"><span></span></button>
  <nav class="links" aria-label="Principal">{links}<a class="cta" href="orcamento.html"{cur if current=="quote" else ""}>{t['nav_quote']}</a></nav>
</div></header>
<main id="conteudo">
"""

def footer(lang, prefix):
    t = T[lang]
    return f"""</main>
<footer class="site"><div class="wrap">
  <div class="foot">
    <div><p class="big">{t['foot_big']}</p><p style="margin-top:18px"><a class="btn foot-cta" href="mailto:decupalm@gmail.com">{t['foot_cta']} <span aria-hidden="true">→</span></a></p><p class="foot-mail">decupalm@gmail.com</p></div>
    <div><h4>{t['foot_nav']}</h4><ul><li><a href="trabalhos.html">{t['nav_work']}</a></li><li><a href="sobre.html">{t['nav_about']}</a></li><li><a href="servicos.html">{t['nav_services']}</a></li><li><a href="orcamento.html">{t['nav_quote']}</a></li></ul></div>
    <div><h4>{t['foot_contact']}</h4><ul>
      <li><a href="https://wa.me/5562996271992" target="_blank" rel="noopener">WhatsApp (62) 99627-1992</a></li>
      <li><a href="https://www.instagram.com/historiso/" target="_blank" rel="noopener">{t['foot_insta']} @historiso</a></li>
      <li><a href="https://www.linkedin.com/in/carlos-raimundo-b557141a5/" target="_blank" rel="noopener">LinkedIn</a></li>
    </ul></div>
  </div>
  <div class="foot-bottom"><span>© 2026 {t['foot_rights']}</span><span class="osd" style="font-size:1.1rem">{t['foot_place']} · UTC−3</span></div>
</div></footer>
<div class="reel" id="reel" role="dialog" aria-modal="true" aria-label="Showreel" hidden>
  <video muted playsinline loop preload="none"></video>
  <button class="reel-close" type="button" aria-label="{t['close']}">×</button>
</div>
<div class="modal" id="player" role="dialog" aria-modal="true" aria-label="Player">
  <button class="close" aria-label="{t['close']}">×</button>
  <div class="modal-box"><div class="player"></div><div class="modal-body"></div></div>
</div>
<script src="{prefix}assets/js/data.js?v={ver("assets/js/data.js")}"></script>
<script src="{prefix}assets/js/site.js?v={ver("assets/js/site.js")}"></script>
</body>
</html>
"""

def g(text):  # título com glitch
    return f'<span class="glitch" data-text="{html.escape(text)}">{html.escape(text)}</span>'

# ------------------------------------------------------------------ páginas
PAGES = {}

PAGES["index.html"] = {"key": "home",
 "title": {"pt": "Carlos Raimundo · Filmmaker e editor em Goiânia", "en": None},
 "desc": {"pt": "Filmmaker e editor em Goiânia. Mais de 5 anos filmando e editando casamentos, 15 anos, formaturas, videoclipes, documentários, reels e anúncios.", "en": None},
 "body": {"pt": f"""
<div class="hero-wrap">
  <section class="hero" aria-label="Apresentação">
    <div class="bg"></div><span class="scan"></span>
    <div class="bar t"></div><div class="bar b"></div>
    <div class="hud t"><span>▶ PLAY</span><span class="rec hide-sm">REC</span><span data-tc>SP 0:00:00</span></div>
    <div class="hero-copy">
      <h1><span class="sr-only">Carlos Raimundo, filmmaker e editor de vídeo em Goiânia: </span><span class="line glitch" data-text="Histórias">Histórias</span> <span class="line glitch" data-text="em emoção">em emoção</span> <span class="line acc glitch" data-text="e ritmo.">e ritmo.</span></h1>
      <blockquote class="hero-quote">“Uma boa montagem faz um filme parecer bem dirigido. Uma excepcional montagem faz o filme parecer que não foi dirigido.”<footer>— WALTER MURCH</footer></blockquote>
      <div class="actions"><button class="btn" type="button" data-reel-open><svg viewBox="0 0 14 14" width="14" height="14" aria-hidden="true"><path d="M3 1.5v11l9-5.5z" fill="currentColor"/></svg>Ver showreel</button><a class="btn ghost" href="trabalhos.html">Ver trabalhos</a></div>
    </div>
    <div class="hud b"><span class="hide-sm">SHOWREEL · 2026</span><span data-pct>CH 03 · 0%</span></div>
  </section>
</div>

<section class="sec bio-sec" aria-label="Sobre mim">
  <div class="wrap bio">
    <figure class="bio-photo" data-reveal><img src="assets/img/carlos.jpg" alt="Carlos Raimundo, sentado num sofá de couro durante uma festa à noite, em preto e branco" loading="lazy" decoding="async" width="1000" height="1268"><figcaption class="osd">● REC · CARLOS RAIMUNDO</figcaption></figure>
    <div class="bio-text">
      <p class="eyebrow">Sobre</p>
      <h2 data-stretch>{g("Prazer, Carlos")}</h2>
      <p class="lede">Sou Carlos Raimundo, filmmaker e editor em Goiânia. Há mais de 5 anos filmo e edito casamentos, 15 anos, formaturas, videoclipes, documentários e vídeos para redes.</p>
      <div class="stats" data-reveal>
        <div class="stat"><b>+5 anos</b><span>filmando e editando profissionalmente</span></div>
        <div class="stat"><b>2 prêmios</b><span>em festivais de cinema</span></div>
      </div>
      <p style="margin-top:24px"><a class="btn ghost" href="sobre.html">Conhecer minha história</a></p>
    </div>
  </div>
</section>

<section class="sec">
  <div class="glow" style="width:620px;height:620px;right:-220px;top:-120px"></div>
  <div class="wrap" style="position:relative">
    <div class="head"><div><p class="eyebrow">Trabalhos</p><h2 data-stretch>{g("Escolha o formato")}</h2></div>
      <p class="lede" style="margin:0">Cada tipo de trabalho tem a sua página, para você ver só o que interessa.</p></div>
    <div class="cats" data-cats="" data-reveal></div>
  </div>
</section>

<section class="sec line">
  <div class="wrap">
    <div class="head"><div><p class="eyebrow">Destaques</p><h2 data-stretch>{g("Para começar")}</h2></div></div>
    <div class="feature" data-featured data-reveal></div>
  </div>
</section>

<section class="awards" aria-label="Prêmios" data-reveal>
  <div class="award"><span class="osd">★</span><div><b>Melhor videoclipe pelo júri popular</b><span>O Que Te Faz Querer, Actemia · 6º IFIDEVIDULA</span></div></div>
  <div class="award"><span class="osd">★</span><div><b>Menção honrosa</b><span>Debaixo da Lona · 12ª MAU, Mostra de Cinema e Audiovisual da UEG, 2022</span></div></div>
</section>

<section class="sec line" id="processo">
  <div class="glow" style="width:560px;height:560px;left:-240px;top:40px"></div>
  <div class="wrap" style="position:relative">
    <div class="head"><div><p class="eyebrow">Processo</p><h2 data-stretch>{g("Da câmera ao corte")}</h2></div>
      <p class="lede" style="margin:0">Casamentos, 15 anos, formaturas, videoclipes, documentários, curtas, reels e anúncios: cada formato pede um ritmo, e a edição é onde a história ganha forma.</p></div>
    <div class="ai-grid four" data-reveal>
      <article class="ai"><span class="osd r">● CAPTAÇÃO</span><h3>Direção em cena</h3><p>Câmera principal ou secundária, dirigindo quem está à frente da lente de forma confortável e dinâmica, com ou sem experiência diante da câmera.</p></article>
      <article class="ai"><span class="osd g">● MONTAGEM</span><h3>Edição em todos os nichos</h3><p>Do save the date ao filme completo, do same day ao videoclipe e ao documentário: ritmo, emoção e história em cada corte.</p></article>
      <article class="ai"><span class="osd b">● FINALIZAÇÃO</span><h3>Acabamento e versões</h3><p>Motion graphics, mixagem de áudio e acabamento, com versões para cada formato e rede.</p></article>
      <article class="ai"><span class="osd o">● IA NO FLUXO</span><h3>Fluxo mais ágil</h3><p>Ferramentas de IA, como o Adobe Firefly e o Claude, para organizar o material, agilizar etapas repetitivas e ampliar o tipo de trabalho que consigo entregar.</p></article>
    </div>
  </div>
</section>

""", "en": None}}

PAGES["trabalhos.html"] = {"key": "work",
 "title": {"pt": "Trabalhos · Carlos Raimundo", "en": None},
 "desc": {"pt": "Trabalhos autorais e filmes feitos para outras produtoras: casamentos, 15 anos, formatura e verticais.", "en": None},
 "body": {"pt": f"""
<section class="page-top">
  <div class="glow" style="width:600px;height:600px;right:-200px;top:-200px"></div>
  <div class="wrap" style="position:relative">
    <p class="crumbs">▶ PLAY · TRABALHOS</p>
    <h1>{g("Trabalhos")}</h1>
    <p class="lede">Separados por tipo, como fichas de uma estante de fitas. Escolha uma categoria para ver os vídeos.</p>
  </div>
</section>
<section class="sec" style="padding-top:20px">
  <div class="wrap groups">
    <div><div class="group-head"><h3>Autorais</h3><p>Filmes que eu criei: curtas, documentários e videoclipes.</p></div><div class="cats" data-cats="autoral" data-wide data-reveal></div></div>
    <div><div class="group-head"><h3>Para outras produtoras</h3><p>Filmes que captei e editei como parte da equipe de outras empresas. Os clientes são dessas empresas.</p></div><div class="cats" data-cats="parceiras" data-reveal></div></div>
    <div class="group-sep"><div class="group-head"><h3>Decupalm</h3><p>Minha produtora, uma marca à parte deste portfólio. Aqui ficam os casamentos que ela produziu do início ao fim.</p></div><div class="cats" data-cats="decupalm" data-wide data-reveal></div></div>
  </div>
</section>
""", "en": None}}

def cat_page(cid, title, group_label, group_desc, sub, extra_top="", note=""):
    return {"pt": f"""
<section class="page-top">
  <div class="glow" style="width:600px;height:600px;right:-200px;top:-200px"></div>
  <div class="wrap" style="position:relative">
    <p class="crumbs"><a href="trabalhos.html">TRABALHOS</a> / {html.escape(group_label.upper())} · <span data-count></span></p>
    {extra_top}
    <h1>{g(title)}</h1>
    <p class="lede">{html.escape(sub)}</p>
  </div>
</section>
<section class="sec" style="padding-top:10px">
  <div class="wrap">
    <div class="grid" data-grid="{cid}" data-reveal></div>
    <p class="note-box">{html.escape(group_desc)}{(' ' + note) if note else ''}</p>
    <div class="head" style="margin:56px 0 18px"><div><p class="eyebrow">Outras categorias</p></div></div>
    <div class="cats" data-cats="" data-exclude="{cid}" data-wide></div>
  </div>
</section>
""", "en": None}

PARC = "Trabalhos feitos como parte da equipe de outras produtoras. Os clientes são dessas empresas."
DECU_TOP = '<img src="assets/img/decupalm.png" alt="Decupalm" style="width:min(220px,50vw);margin-bottom:22px;filter:drop-shadow(0 0 26px rgba(107,47,153,.85))">'
CATPAGES = [
  ("trabalhos-filmes.html", "filmes", "Filmes", "Autorais", "Trabalhos autorais.", "Curtas, documentários e videoclipes que criei, com dois prêmios em festivais.", "", ""),
  ("trabalhos-decupalm.html", "decupalm", "Casamentos Decupalm", "Decupalm", "Casamentos produzidos pela Decupalm, minha produtora. No Instagram: @decupalm.", "A Decupalm é minha produtora de vídeo e foto. Aqui ficam os casamentos que ela produziu do início ao fim: trailer, prévia e pré-wedding.", DECU_TOP, ""),
  ("trabalhos-casamentos.html", "casamentos", "Casamentos", "Para outras produtoras", PARC, "Save the date, prévia, same day e trailer de casamentos que captei e editei.", "", ""),
  ("trabalhos-15-anos.html", "quinze", "15 anos", "Para outras produtoras", PARC, "Save the date, entrada, same day e trailer de festas de 15 anos.", "", ""),
  ("trabalhos-formatura.html", "formatura", "Formatura", "Para outras produtoras", PARC, "Same day editado durante a festa de formatura.", "", ""),
  ("trabalhos-verticais.html", "shortform", "Verticais", "Redes", "Vídeos verticais para marcas e redes sociais.", "Reels, anúncios para tráfego pago e vídeos para redes.", "", ""),
]
for fn, cid, title, gl, gd, sub, top, note in CATPAGES:
    PAGES[fn] = {"key": "work", "title": {"pt": f"{title} · Carlos Raimundo", "en": None}, "desc": {"pt": sub, "en": None},
                 "body": cat_page(cid, title, gl, gd, sub, top, note)}

PAGES["sobre.html"] = {"key": "about",
 "title": {"pt": "Sobre · Carlos Raimundo", "en": None},
 "desc": {"pt": "Carlos Raimundo, filmmaker e editor em Goiânia. Cinema na UEG, mais de 5 anos de mercado, dois prêmios em festivais e edição em todos os nichos.", "en": None},
 "body": {"pt": f"""
<section class="page-top">
  <div class="glow" style="width:600px;height:600px;right:-200px;top:-200px"></div>
  <div class="wrap" style="position:relative">
    <p class="crumbs">● REC · SOBRE</p>
    <h1>{g("Prazer,")} <br><span class="acc">{g("Carlos.")}</span></h1>
    <p class="lede">Um profissional que transforma história em emoção e ritmo.</p>
  </div>
</section>
<section class="sec" style="padding-top:20px">
  <div class="wrap about">
    <div class="story">
      <p>Desde criança eu montava pequenos filmes no MovieMaker com vídeos que achava na internet. Vendo as grandes produções nas telonas, eu sabia que era aquilo que queria fazer.</p>
      <p>Comecei a trabalhar com vídeo pelo celular, postando no Instagram, até passar no vestibular de Cinema e Audiovisual na UEG. Na faculdade fiz documentários e videoclipes que ganharam prêmios em festivais e me mostraram que eu estava no caminho certo.</p>
      <p>Depois passei quase 3 anos numa empresa de foto e filme para casamentos, onde cheguei a liderar o departamento de vídeo: câmera principal, edição dos filmes principais, controle de qualidade e direção dos clientes em cena. Foi ali que desenvolvi minha direção durante a captação, minha linguagem e minha postura profissional.</p>
      <p>No fim de 2025 decidi seguir por conta própria. Hoje sou freelancer, faço captação e edição sem distinção de nicho, uso IA para ampliar o que consigo entregar e estou concluindo a graduação em Cinema.</p>
      <p>É um prazer ter você aqui.</p>
      <p style="margin-top:28px;display:flex;gap:12px;flex-wrap:wrap"><a class="btn" href="carlos-raimundo-curriculo.pdf" target="_blank" rel="noopener">Baixar currículo (PDF)</a><a class="btn ghost" href="orcamento.html">Falar comigo</a></p>
    </div>
    <div>
      <blockquote>“Uma boa montagem faz um filme parecer bem dirigido. Uma excepcional montagem faz o filme parecer que não foi dirigido.”<footer>— WALTER MURCH</footer></blockquote>
      <ol class="timeline" data-reveal>
        <li><span class="osd">INFÂNCIA</span>Primeiros filmes no MovieMaker</li>
        <li><span class="osd">CELULAR</span>Vídeos gravados no celular e postados no Instagram</li>
        <li><span class="osd">UEG</span>Cinema e Audiovisual: documentários e videoclipes</li>
        <li><span class="osd">2022</span>Menção honrosa na 12ª MAU com Debaixo da Lona</li>
        <li><span class="osd">2022–2025</span>Empresa de casamentos: de editor júnior a líder do departamento de vídeo</li>
        <li><span class="osd">2025 – ATUALMENTE</span>Freelancer, captação e edição em todos os nichos</li>
      </ol>
    </div>
  </div>
</section>
<section class="sec line">
  <div class="wrap">
    <div class="head"><div><p class="eyebrow">Habilidades</p><h2 data-stretch>{g("O que eu faço")}</h2></div></div>
    <div class="skills" data-balance="230" data-reveal>
      <div class="skill"><b>Adobe Premiere Pro</b><span>Edição em domínio pleno, desde o início da carreira</span></div>
      <div class="skill"><b>Finalização</b><span>Motion graphics e mixagem de áudio no acabamento</span></div>
      <div class="skill"><b>Captação</b><span>Câmera profissional e mobile, como câmera principal ou secundária</span></div>
      <div class="skill"><b>Direção de set</b><span>Posição, expressão e cena, inclusive com quem não é ator</span></div>
      <div class="skill"><b>IA no fluxo</b><span>Ferramentas como o Adobe Firefly e o Claude para organizar, agilizar e ampliar as entregas</span></div>
      <div class="skill"><b>Liderança</b><span>Gestão de equipe de filmagem e de todo o fluxo, da pré à pós</span></div>
      <div class="skill"><b>Atendimento</b><span>Briefing, alinhamento criativo e apresentação das entregas</span></div>
    </div>
  </div>
</section>
<section class="sec line">
  <div class="wrap">
    <div class="head"><div><p class="eyebrow">Prêmios</p><h2 data-stretch>{g("Reconhecimento")}</h2></div></div>
    <div class="award-cards" data-reveal>
      <button class="award-card" type="button" data-play="tiFgOgUHBwo" aria-label="Assistir O Que Te Faz Querer, melhor videoclipe pelo júri popular">
        <img src="assets/img/premio-o-que-te-faz-querer.jpg" alt="" loading="lazy" decoding="async">
        <span class="award-body"><span class="osd">★ 6º IFIDEVIDULA</span><b>Melhor videoclipe pelo júri popular</b><span class="award-film">O Que Te Faz Querer · Actemia</span><span class="award-cta">▶ Assistir ao filme</span></span>
      </button>
      <button class="award-card" type="button" data-play="65ni2V6kw5w" aria-label="Assistir Debaixo da Lona, menção honrosa na 12ª MAU">
        <img src="assets/img/premio-debaixo-da-lona.jpg" alt="" loading="lazy" decoding="async">
        <span class="award-body"><span class="osd">★ 12ª MAU · UEG, 2022</span><b>Menção honrosa</b><span class="award-film">Debaixo da Lona · documentário</span><span class="award-cta">▶ Assistir ao filme</span></span>
      </button>
    </div>
  </div>
  <div class="wrap"><p class="note-box">Meus filmes autorais estão em <a href="trabalhos-filmes.html">Filmes</a>, e o restante em <a href="trabalhos.html">Trabalhos</a>.</p></div>
</section>
""", "en": None}}

PAGES["servicos.html"] = {"key": "services",
 "title": {"pt": "Serviços · Carlos Raimundo", "en": None},
 "desc": {"pt": "Filmes de casamento e eventos, videoclipes e documentários, reels e anúncios, e edição a distância.", "en": None},
 "body": {"pt": f"""
<section class="page-top">
  <div class="glow" style="width:600px;height:600px;right:-200px;top:-200px"></div>
  <div class="wrap" style="position:relative">
    <p class="crumbs">▶ PLAY · SERVIÇOS</p>
    <h1>{g("Serviços")}</h1>
    <p class="lede">Da captação à entrega. Também faço só a edição, quando você já tem o material.</p>
  </div>
</section>
<section class="sec" style="padding-top:20px">
  <div class="wrap services" data-reveal>
    <article class="service"><div><span class="osd" style="color:var(--ch-r);font-size:1.2rem">● 01</span><h3>Casamentos e eventos</h3></div>
      <div><p>Casamentos, pré-wedding, 15 anos e formaturas. Eu dirijo vocês em cena, então ninguém precisa saber posar.</p><div class="tags"><span>Save the date</span><span>Prévia</span><span>Same day</span><span>Trailer</span><span>Filme completo</span><span>Entrada</span></div></div>
      <a class="btn ghost" href="trabalhos-casamentos.html">Ver trabalhos</a></article>
    <article class="service"><div><span class="osd" style="color:var(--ch-g);font-size:1.2rem">● 02</span><h3>Música e cinema</h3></div>
      <div><p>Videoclipes, documentários e curtas, com direção de fotografia e montagem pensadas para a história.</p><div class="tags"><span>Videoclipe</span><span>Documentário</span><span>Curta-metragem</span><span>Direção de fotografia</span><span>Montagem</span></div></div>
      <a class="btn ghost" href="trabalhos-filmes.html">Ver trabalhos</a></article>
    <article class="service"><div><span class="osd" style="color:var(--ch-b);font-size:1.2rem">● 03</span><h3>Redes e marcas</h3></div>
      <div><p>Vídeos verticais com ritmo para segurar a atenção: reels, anúncios para tráfego pago e conteúdo de marca.</p><div class="tags"><span>Reels</span><span>Shorts</span><span>Anúncios</span><span>Institucional</span></div></div>
      <a class="btn ghost" href="trabalhos-verticais.html">Ver trabalhos</a></article>
    <article class="service"><div><span class="osd" style="color:var(--orchid);font-size:1.2rem">● 04</span><h3>Só a edição</h3></div>
      <div><p>Já tem o material gravado? Eu edito a distância, em qualquer nicho, com IA no fluxo para organizar o material e entregar versões para cada rede.</p><div class="tags"><span>Edição remota</span><span>Todos os nichos</span><span>Versões para redes</span><span>Roteiro e decupagem</span></div></div>
      <a class="btn ghost" href="orcamento.html">Pedir orçamento</a></article>
  </div>
</section>
""", "en": None}}

PAGES["orcamento.html"] = {"key": "quote",
 "title": {"pt": "Orçamento · Carlos Raimundo", "en": None},
 "desc": {"pt": "Peça um orçamento para casamento, evento, videoclipe, documentário, reels ou só a edição.", "en": None},
 "body": {"pt": f"""
<section class="page-top">
  <div class="glow" style="width:600px;height:600px;right:-200px;top:-200px"></div>
  <div class="wrap" style="position:relative">
    <p class="crumbs">● REC · ORÇAMENTO</p>
    <h1>{g("Vamos")} <br><span class="acc">{g("filmar?")}</span></h1>
    <p class="lede">Conte o que você precisa. Quanto mais detalhes, mais certa sai a proposta. Respondo em até 24 horas.</p>
  </div>
</section>
<section class="sec" style="padding-top:20px">
  <div class="wrap quote-grid">
    <form class="form" id="quote-form" novalidate>
      <div class="field"><label for="f-nome">Nome</label><input id="f-nome" name="nome" required autocomplete="name"></div>
      <div class="field"><label for="f-email">E-mail</label><input id="f-email" name="email" type="email" required autocomplete="email"></div>
      <div class="field"><label for="f-whats">WhatsApp</label><input id="f-whats" name="whatsapp" type="tel" autocomplete="tel"></div>
      <div class="field"><label for="f-tipo">Tipo de trabalho</label><select id="f-tipo" name="tipo" required>
        <option value="">Selecione</option><option>Casamento</option><option>Pré-wedding</option><option>15 anos</option><option>Formatura</option><option>Videoclipe</option><option>Documentário ou curta</option><option>Reels e anúncios</option><option>Só edição</option><option>Outro</option></select></div>
      <div class="field"><label for="f-data">Data do evento ou prazo</label><input id="f-data" name="data" placeholder="ex.: 12/04/2027"></div>
      <div class="field"><label for="f-cidade">Cidade</label><input id="f-cidade" name="cidade" placeholder="ex.: Goiânia"></div>
      <div class="field full"><label for="f-inv">Investimento previsto</label><select id="f-inv" name="investimento">
        <option value="">Selecione</option><option>Até R$ 1.500</option><option>R$ 1.500 a R$ 3.000</option><option>R$ 3.000 a R$ 6.000</option><option>Acima de R$ 6.000</option><option>Ainda não sei</option></select></div>
      <div class="field full"><label for="f-msg">Sobre o projeto</label><textarea id="f-msg" name="mensagem" required placeholder="Conte a ideia, o local, quantas pessoas, referências…"></textarea></div>
      <input type="text" name="_honey" tabindex="-1" autocomplete="off" style="display:none" aria-hidden="true">
      <div class="full" style="display:flex;gap:16px;align-items:center;flex-wrap:wrap"><button class="btn" type="submit">Enviar pedido</button><p class="form-status" role="status"></p></div>
    </form>
    <div class="contacts">
      <a class="contact" href="https://wa.me/5562996271992" target="_blank" rel="noopener"><span class="osd">WHATSAPP</span><div><b>(62) 99627-1992</b><small>O jeito mais rápido</small></div></a>
      <a class="contact" href="mailto:decupalm@gmail.com"><span class="osd">E-MAIL</span><div><b>decupalm@gmail.com</b><small>Para briefings e arquivos</small></div></a>
      <a class="contact" href="https://www.instagram.com/historiso/" target="_blank" rel="noopener"><span class="osd">INSTAGRAM</span><div><b>@historiso</b><small>Bastidores e trabalhos</small></div></a>
      <a class="contact" href="https://www.instagram.com/decupalm/" target="_blank" rel="noopener"><span class="osd">DECUPALM</span><div><b>@decupalm</b><small>Minha produtora de casamentos</small></div></a>
    </div>
  </div>
</section>
""", "en": None}}

# ------------------------------------------------------------------ SEO
# Títulos e descrições pensados para as buscas (ex.: "filmmaker Goiânia", "filmagem de casamento Goiânia").
SEO = {
  "index.html": ("Carlos Raimundo · Filmmaker e Editor de Vídeo em Goiânia",
                 "Filmmaker e editor de vídeo em Goiânia. Filmagem e edição de casamentos, 15 anos, formaturas, videoclipes, documentários e reels. Veja o showreel e peça seu orçamento."),
  "trabalhos.html": ("Portfólio de Vídeos · Carlos Raimundo, Filmmaker em Goiânia",
                 "Portfólio de Carlos Raimundo: filmes de casamento, 15 anos, formatura, videoclipes, documentários e reels, separados por tipo de trabalho."),
  "trabalhos-filmes.html": ("Videoclipes e Documentários · Carlos Raimundo",
                 "Curtas, documentários e videoclipes de Carlos Raimundo, filmmaker em Goiânia, com dois prêmios em festivais de cinema."),
  "trabalhos-casamentos.html": ("Filmes de Casamento em Goiânia · Carlos Raimundo",
                 "Save the date, prévia, same day e trailer de casamentos filmados e editados por Carlos Raimundo, filmmaker em Goiânia."),
  "trabalhos-15-anos.html": ("Filmes de 15 Anos em Goiânia · Carlos Raimundo",
                 "Save the date, entrada, same day e trailer de festas de 15 anos filmados e editados por Carlos Raimundo em Goiânia."),
  "trabalhos-formatura.html": ("Filme de Formatura · Carlos Raimundo, Filmmaker em Goiânia",
                 "Same day de formatura editado durante a festa por Carlos Raimundo, filmmaker e editor de vídeo em Goiânia."),
  "trabalhos-verticais.html": ("Reels e Vídeos Verticais · Carlos Raimundo",
                 "Reels, anúncios para tráfego pago e vídeos verticais para marcas e redes sociais, editados por Carlos Raimundo em Goiânia."),
  "sobre.html": ("Sobre Carlos Raimundo · Filmmaker e Editor em Goiânia",
                 "Carlos Raimundo, filmmaker e editor de vídeo em Goiânia. Cinema e Audiovisual na UEG, mais de 5 anos de mercado e dois prêmios em festivais."),
  "servicos.html": ("Filmagem e Edição de Vídeo em Goiânia · Carlos Raimundo",
                 "Filmagem e edição de casamentos e eventos, videoclipes, documentários, reels e anúncios em Goiânia. Também faço só a edição, a distância."),
  "orcamento.html": ("Orçamento de Filmagem e Edição · Carlos Raimundo",
                 "Peça um orçamento de filmagem ou edição de vídeo em Goiânia: casamento, 15 anos, formatura, videoclipe, documentário ou reels. Resposta em até 24 horas."),
}
# Código de verificação do Google Search Console (cole só o valor de content="...")
GSC_CODE = ""
GSC_META = f'\n<meta name="google-site-verification" content="{GSC_CODE}">' if GSC_CODE else ""

def jsonld_home():
    import json
    data = {"@context": "https://schema.org", "@graph": [
      {"@type": "Person", "@id": f"{SITE_URL}/#carlos", "name": "Carlos Raimundo", "alternateName": "Carlos Raimundo Macedo",
       "jobTitle": "Filmmaker e editor de vídeo", "url": f"{SITE_URL}/", "image": f"{SITE_URL}/assets/img/carlos.jpg",
       "email": "mailto:decupalm@gmail.com", "telephone": "+55-62-99627-1992",
       "address": {"@type": "PostalAddress", "addressLocality": "Goiânia", "addressRegion": "GO", "addressCountry": "BR"},
       "alumniOf": {"@type": "CollegeOrUniversity", "name": "Universidade Estadual de Goiás (UEG)"},
       "award": ["Melhor videoclipe pelo júri popular · 6º IFIDEVIDULA (O Que Te Faz Querer)",
                 "Menção honrosa · 12ª MAU, Mostra de Cinema e Audiovisual da UEG (Debaixo da Lona)"],
       "knowsAbout": ["Filmagem de casamento", "Edição de vídeo", "Videoclipe", "Documentário", "Reels", "Adobe Premiere Pro"],
       "sameAs": ["https://www.instagram.com/historiso/", "https://www.linkedin.com/in/carlos-raimundo-b557141a5/", "https://www.youtube.com/@farpanation4559"]},
      {"@type": "ProfessionalService", "@id": f"{SITE_URL}/#servico", "name": "Carlos Raimundo · Filmmaker e editor de vídeo",
       "url": f"{SITE_URL}/", "image": f"{SITE_URL}/assets/img/og.jpg", "telephone": "+55-62-99627-1992", "email": "decupalm@gmail.com",
       "founder": {"@id": f"{SITE_URL}/#carlos"},
       "address": {"@type": "PostalAddress", "addressLocality": "Goiânia", "addressRegion": "GO", "addressCountry": "BR"},
       "areaServed": [{"@type": "City", "name": "Goiânia"}, {"@type": "City", "name": "Aparecida de Goiânia"}, {"@type": "State", "name": "Goiás"}],
       "serviceType": ["Filmagem de casamento", "Filmagem de 15 anos", "Filmagem de formatura", "Videoclipe", "Documentário", "Edição de vídeo", "Reels e anúncios"],
       "sameAs": ["https://www.instagram.com/historiso/", "https://www.linkedin.com/in/carlos-raimundo-b557141a5/"]},
      {"@type": "WebSite", "@id": f"{SITE_URL}/#site", "url": f"{SITE_URL}/", "name": "Carlos Raimundo · Filmmaker e editor", "inLanguage": "pt-BR",
       "publisher": {"@id": f"{SITE_URL}/#carlos"}}
    ]}
    return f'\n<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'

def write_seo_files(pages):
    import datetime
    today = datetime.date.today().isoformat()
    prio = {"index.html": "1.0", "trabalhos.html": "0.9", "servicos.html": "0.8", "sobre.html": "0.7", "orcamento.html": "0.8"}
    urls = "".join(f"  <url><loc>{page_url(fn)}</loc><lastmod>{today}</lastmod><priority>{prio.get(fn, '0.7')}</priority></url>\n" for fn in pages)
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    print("ok sitemap.xml e robots.txt")

def write_404():
    body = """
<section class="page-top">
  <div class="wrap" style="position:relative">
    <p class="crumbs">■ STOP · ERRO 404</p>
    <h1>Fita<br><span class="acc">não encontrada.</span></h1>
    <p class="lede">Esta página não existe ou mudou de endereço.</p>
    <p style="margin-top:28px;display:flex;gap:12px;flex-wrap:wrap"><a class="btn" href="/">Voltar ao início</a><a class="btn ghost" href="/trabalhos.html">Ver trabalhos</a></p>
  </div>
</section>
"""
    page = head("pt", "Página não encontrada · Carlos Raimundo", "Esta página não existe ou mudou de endereço.", "/", "404.html",
                '\n<meta name="robots" content="noindex">').replace(f'<link rel="canonical" href="{page_url("404.html")}">', "")
    page += nav("pt", "", "/").replace('href="index.html"', 'href="/"') + body + footer("pt", "/")
    for a in ["trabalhos.html", "sobre.html", "servicos.html", "orcamento.html"]:
        page = page.replace(f'href="{a}"', f'href="/{a}"')
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write(page)
    print("ok 404.html")

def build():
    langs = ["pt"] + (["en"] if BUILD_EN else [])
    for lang in langs:
        outdir = OUT if lang == "pt" else os.path.join(OUT, "en")
        prefix = "" if lang == "pt" else "../"
        os.makedirs(outdir, exist_ok=True)
        for fn, p in PAGES.items():
            body = p["body"].get(lang)
            if body is None:
                continue
            title, desc = p["title"][lang], p["desc"][lang]
            if lang == "pt" and fn in SEO:
                title, desc = SEO[fn]
            extra = jsonld_home() if fn == "index.html" else ""
            page = head(lang, title, desc, prefix, fn, extra) + nav(lang, p["key"], prefix) + body + footer(lang, prefix)
            with open(os.path.join(outdir, fn), "w", encoding="utf-8") as f:
                f.write(page)
            print("ok", lang, fn)
    write_seo_files([fn for fn in PAGES])
    write_404()

if __name__ == "__main__":
    build()
