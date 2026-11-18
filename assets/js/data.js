/* =========================================================
   CONTEÚDO DO PORTFÓLIO
   Para adicionar um vídeo: copie uma linha da categoria e troque o id
   (o id é o código depois de "watch?v=" ou "shorts/" no link do YouTube).
   Campos "en" ficam prontos para a versão em inglês.
   ========================================================= */
window.SITE = {
  name: "Carlos Raimundo",
  email: "decupalm@gmail.com",
  whatsapp: "5562996271992",
  whatsappLabel: "(62) 99627-1992",
  instagram: { handle: "@historiso", url: "https://www.instagram.com/historiso/" },
  instagramAutoral: { handle: "@decupalm", url: "https://www.instagram.com/decupalm/" },
  linkedin: "https://www.linkedin.com/in/carlos-raimundo-b557141a5/",
  /* Showreel no topo da Home: arquivos em assets/video (mudo, em loop).
     Para trocar, substitua os arquivos mantendo os nomes. */
  showreel: { hd: "assets/video/showreel-1080.mp4", sd: "assets/video/showreel-720.mp4", poster: "assets/video/showreel-poster.jpg" }
};

/* Grupos: só "decupalm" leva @decupalm; "parceiras" são trabalhos feitos para outras produtoras.
   O logo da Decupalm só aparece na página do grupo "decupalm". */
window.GROUPS = {
  autoral:   { pt: "Autorais", en: "Original work",
               desc: { pt: "Filmes que eu criei: curtas, documentários e videoclipes.", en: "Films I created: shorts, documentaries and music videos." } },
  decupalm:  { pt: "Decupalm", en: "Decupalm",
               desc: { pt: "Minha produtora. Casamentos produzidos por ela do início ao fim.", en: "My production company. Weddings it produced from start to finish." } },
  parceiras: { pt: "Para outras produtoras", en: "For other studios",
               desc: { pt: "Filmes que captei e editei como parte da equipe de outras empresas. Os clientes são dessas empresas.", en: "Films I shot and edited as part of other companies' crews. The clients belong to those companies." } }
};

window.CATEGORIES = [
  { id: "filmes", page: "trabalhos-filmes.html", group: "autoral", vertical: false,
    title: { pt: "Filmes", en: "Films" },
    sub: { pt: "Curtas, documentários e videoclipes", en: "Shorts, documentaries and music videos" },
    credit: { pt: "Trabalho autoral", en: "Original work" } },
  { id: "casamentos", page: "trabalhos-casamentos.html", group: "parceiras", vertical: false,
    title: { pt: "Casamentos", en: "Weddings" },
    sub: { pt: "Save the date, prévia, same day e trailer", en: "Save the date, preview, same day and trailer" },
    credit: { pt: "Feito para outra produtora", en: "Made for another studio" } },
  { id: "quinze", page: "trabalhos-15-anos.html", group: "parceiras", vertical: false,
    title: { pt: "15 anos", en: "Sweet Fifteen" },
    sub: { pt: "Save the date, entrada, same day e trailer", en: "Save the date, entrance, same day and trailer" },
    credit: { pt: "Feito para outra produtora", en: "Made for another studio" } },
  { id: "formatura", page: "trabalhos-formatura.html", group: "parceiras", vertical: false,
    title: { pt: "Formatura", en: "Graduation" },
    sub: { pt: "Same day de formatura", en: "Graduation same day edit" },
    credit: { pt: "Feito para outra produtora", en: "Made for another studio" } },
  { id: "shortform", page: "trabalhos-short-form.html", group: "parceiras", vertical: true,
    title: { pt: "Short form", en: "Short form" },
    sub: { pt: "Reels e anúncios verticais", en: "Reels and vertical ads" },
    credit: { pt: "Feito para outra empresa", en: "Made for another company" } },
  { id: "decupalm", page: "trabalhos-decupalm.html", group: "decupalm", vertical: false,
    title: { pt: "Casamentos Decupalm", en: "Decupalm Weddings" },
    sub: { pt: "Filmes de casamento da minha produtora", en: "Wedding films by my production company" },
    credit: { pt: "Decupalm", en: "Decupalm" } }
];

/* type: tipo de entrega · title: nome exibido · place: cidade (opcional)
   role, award, note: opcionais · featured: aparece nos destaques da Home */
window.WORKS = [
  /* ---------- Filmes (autoral) ---------- */
  { id: "tiFgOgUHBwo", cat: "filmes", featured: 1,
    type: { pt: "Videoclipe", en: "Music video" }, title: { pt: "O Que Te Faz Querer", en: "O Que Te Faz Querer" },
    artist: "Actemia", prod: "Clube dos Cinco",
    role: { pt: "Direção, direção de fotografia e montagem", en: "Director, cinematographer and editor" },
    award: { pt: "Melhor videoclipe pelo júri popular · 6º IFIDEVIDULA", en: "Best music video, audience award · 6th IFIDEVIDULA" } },
  { id: "65ni2V6kw5w", cat: "filmes", featured: 2,
    type: { pt: "Documentário", en: "Documentary" }, title: { pt: "Debaixo da Lona", en: "Debaixo da Lona" },
    role: { pt: "Direção de fotografia e montagem", en: "Cinematographer and editor" },
    award: { pt: "Menção honrosa · 12ª MAU, Mostra de Cinema e Audiovisual da UEG (2022)", en: "Honorable mention · 12th MAU, UEG Film Festival (2022)" } },
  { id: "8uf7sBXMdx4", cat: "filmes",
    type: { pt: "Videoclipe acadêmico", en: "Music video (film school)" }, title: { pt: "Unknown Aura", en: "Unknown Aura" },
    artist: "Urubu Rei",
    role: { pt: "Direção de fotografia e montagem", en: "Cinematographer and editor" } },
  { id: "l5r6pTkexrU", cat: "filmes", confirm: true,
    type: { pt: "Documentário", en: "Documentary" }, title: { pt: "Ponto de Vista", en: "Ponto de Vista" },
    role: { pt: "Montagem e idealização", en: "Editor and co-creator" } },

  /* ---------- Casamentos Decupalm (produtora, marca à parte) ---------- */
  { id: "B5BiSVGCpJ0", cat: "decupalm", type: { pt: "Trailer", en: "Trailer" }, title: { pt: "Camila e Mirela", en: "Camila & Mirela" } },
  { id: "hVk5vnKJZ68", cat: "decupalm", type: { pt: "Prévia", en: "Preview" }, title: { pt: "Camila e Mirela", en: "Camila & Mirela" } },
  { id: "r8i60H_v_Bw", cat: "decupalm", type: { pt: "Pré-wedding", en: "Engagement" }, title: { pt: "Camila e Mirela", en: "Camila & Mirela" } },
  { id: "QpH4m6G5-14", cat: "decupalm", type: { pt: "Pré-wedding", en: "Engagement" }, title: { pt: "Maria e Matheus", en: "Maria & Matheus" } },

  /* ---------- Casamentos (para outras produtoras) ---------- */
  { id: "Zm3D3CETCGo", cat: "casamentos", featured: 4, type: { pt: "Same day", en: "Same day edit" }, title: { pt: "Rafaella e Erick", en: "Rafaella & Erick" } },
  { id: "p0RknQ96gOY", cat: "casamentos", type: { pt: "Same day", en: "Same day edit" }, title: { pt: "Yasmin e Heitor", en: "Yasmin & Heitor" } },
  { id: "KL5psXjVOPA", cat: "casamentos", type: { pt: "Same day", en: "Same day edit" }, title: { pt: "Ana Carolina e Luiz", en: "Ana Carolina & Luiz" } },
  { id: "lp6k6E5f8eM", cat: "casamentos", featured: 3, type: { pt: "Trailer", en: "Trailer" }, title: { pt: "Lourenzo e Aguirre", en: "Lourenzo & Aguirre" } },
  { id: "V9mQ34zN1ss", cat: "casamentos", type: { pt: "Trailer", en: "Trailer" }, title: { pt: "Cristiane e Saulo", en: "Cristiane & Saulo" } },
  { id: "C_9cE0grqsM", cat: "casamentos", type: { pt: "Prévia", en: "Preview" }, title: { pt: "Pricilla e Juan", en: "Pricilla & Juan" } },
  { id: "5jPrFY1EQac", cat: "casamentos", type: { pt: "Prévia", en: "Preview" }, title: { pt: "Paloma e Ícaro", en: "Paloma & Ícaro" } },
  { id: "yC0HWtLtZUE", cat: "casamentos", type: { pt: "Save the date", en: "Save the date" }, title: { pt: "Anaisa e Jairo", en: "Anaisa & Jairo" }, place: "Cidade de Goiás" },
  { id: "Np17NRTZim8", cat: "casamentos", type: { pt: "Save the date", en: "Save the date" }, title: { pt: "Isabella e Ricardo", en: "Isabella & Ricardo" }, place: "Rio de Janeiro" },
  { id: "E3j0xFdjriI", cat: "casamentos", type: { pt: "Save the date", en: "Save the date" }, title: { pt: "Natalia e Daniel", en: "Natalia & Daniel" } },
  { id: "0YSD7kWoTBc", cat: "casamentos", type: { pt: "Save the date", en: "Save the date" }, title: { pt: "Zara e Lucas", en: "Zara & Lucas" } },
  { id: "67pzyiGn99o", cat: "casamentos", type: { pt: "Save the date", en: "Save the date" }, title: { pt: "Beatriz e Guilherme", en: "Beatriz & Guilherme" } },

  /* ---------- 15 anos (para outras produtoras) ---------- */
  { id: "OEQT03_7slk", cat: "quinze", type: { pt: "Trailer", en: "Trailer" }, title: { pt: "Sofia Ruelles", en: "Sofia Ruelles" } },
  { id: "auiiK_ntPgY", cat: "quinze", type: { pt: "Entrada", en: "Entrance" }, title: { pt: "Sofia Ruelles", en: "Sofia Ruelles" } },
  { id: "bTI_RbufPJ8", cat: "quinze", type: { pt: "Same day", en: "Same day edit" }, title: { pt: "Beatriz", en: "Beatriz" } },
  { id: "Btqo1jCUVnc", cat: "quinze", type: { pt: "Save the date", en: "Save the date" }, title: { pt: "Beatriz", en: "Beatriz" } },

  /* ---------- Formatura (para outras produtoras) ---------- */
  { id: "SDBKltF8wxA", cat: "formatura", type: { pt: "Same day", en: "Same day edit" }, title: { pt: "Formatura", en: "Graduation" } },

  /* ---------- Short form (para outras empresas) ---------- */
  { id: "tM4t6mhgLSg", cat: "shortform", type: { pt: "Reels para tráfego pago", en: "Paid ad reel" }, title: { pt: "Anúncio 1", en: "Ad 1" } },
  { id: "0XwMZ3jwq9Y", cat: "shortform", type: { pt: "Reels para tráfego pago", en: "Paid ad reel" }, title: { pt: "Anúncio 2", en: "Ad 2" } }
];
