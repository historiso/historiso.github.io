(function(){
"use strict";
const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
const lang = (document.documentElement.lang || "pt").toLowerCase().startsWith("en") ? "en" : "pt";
const tx = v => typeof v === "string" ? v : (v && (v[lang] || v.pt)) || "";
const L = {
  pt:{works:"vídeos",work:"vídeo",open:"Abrir",watchYT:"Assistir no YouTube",loading:"Carregando o vídeo…",role:"Função",artist:"Artista",prod:"Produção",close:"Fechar",sent:"Recebi sua mensagem. Respondo em até 24 horas.",fail:"Não consegui enviar agora. Seus dados continuam aqui: toque em Enviar de novo.",sending:"Enviando…",retry:"Enviar de novo",send:"Enviar pedido",count:n=>n===1?"1 vídeo":`${n} vídeos`},
  en:{works:"videos",work:"video",open:"Open",watchYT:"Watch on YouTube",loading:"Loading video…",role:"Role",artist:"Artist",prod:"Production",close:"Close",sent:"Got your message. I reply within 24 hours.",fail:"Couldn't send right now. Your details are still here: tap Send again.",sending:"Sending…",retry:"Send again",send:"Send request",count:n=>n===1?"1 video":`${n} videos`}
}[lang];
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const S = window.SITE || {}, CATS = window.CATEGORIES || [], WORKS = window.WORKS || [], GROUPS = window.GROUPS || {};
const catOf = id => CATS.find(c => c.id === id);
const thumb = id => `https://i.ytimg.com/vi/${id}/hqdefault.jpg`;
const esc = s => String(s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const PLAY = '<svg viewBox="0 0 14 14" aria-hidden="true"><path d="M3 1.5v11l9-5.5z" fill="currentColor"/></svg>';

/* ---------- glitch e faixa VHS ---------- */
function glitch(el){ if(reduce || !el) return; el.classList.remove("on"); void el.offsetWidth; el.classList.add("on"); setTimeout(() => el.classList.remove("on"), 360); }
function track(el){ const t = el && el.querySelector(".track"); if(!t || reduce) return; t.classList.remove("go"); void t.offsetWidth; t.classList.add("go"); }
function bindGlitch(root = document){
  $$(".glitch", root).forEach(el => { if(el._gb) return; el._gb = 1; el.addEventListener("pointerenter", () => glitch(el)); glIO.observe(el); });
}
const glIO = new IntersectionObserver(es => es.forEach(e => { if(e.isIntersecting){ glIO.unobserve(e.target); setTimeout(() => glitch(e.target), 120); } }), { rootMargin: "0px 0px -20% 0px" });

/* ---------- entrada em cascata (150 / 900 / 700 ms) ---------- */
const revIO = new IntersectionObserver(es => es.forEach(e => {
  if(!e.isIntersecting) return; revIO.unobserve(e.target);
  if(reduce) return;
  [...e.target.children].forEach((el, i) => {
    el.animate([{opacity:0},{opacity:1}], {duration:900, delay:i*150, easing:"ease-out", fill:"backwards"});
    el.animate([{transform:"translateY(30px)"},{transform:"none"}], {duration:700, delay:i*150, easing:"cubic-bezier(.33,1,.68,1)", fill:"backwards"});
  });
}), { rootMargin: "0px 0px -12% 0px" });
function bindReveal(root = document){ $$("[data-reveal]", root).forEach(g => { if(g.getBoundingClientRect().top > innerHeight * .9) revIO.observe(g); }); }

/* ---------- nav ---------- */
const nav = $(".nav");
const onScrollNav = () => nav && nav.classList.toggle("solid", scrollY > 30);
addEventListener("scroll", onScrollNav, { passive: true }); onScrollNav();
const menuBtn = $(".menu-btn"), links = $(".links");
if(menuBtn) menuBtn.addEventListener("click", () => { const o = links.classList.toggle("open"); menuBtn.setAttribute("aria-expanded", o); });

/* ---------- cartões ---------- */
function imgHTML(id, alt){ return `<img src="${thumb(id)}" alt="${esc(alt)}" loading="lazy" decoding="async" onerror="this.outerHTML='<span class=&quot;fallback&quot;></span>'">`; }
function workCard(w){
  const c = catOf(w.cat), v = c && c.vertical;
  const sub = [tx(w.type), w.artist, w.place].filter(Boolean).join(" · ");
  const b = document.createElement("button");
  b.className = "card" + (v ? " v" : ""); b.dataset.id = w.id;
  b.setAttribute("aria-label", `${L.open}: ${tx(w.title)}, ${sub}`);
  b.innerHTML = `${imgHTML(w.id, "")}<span class="tint"></span><span class="shade"></span><span class="scan"></span><span class="track"></span>
    <span class="osdc"><span>▶ PLAY</span><span>${esc(c ? tx(c.title).toUpperCase() : "")}</span></span>
    <span class="play">${PLAY}</span>
    <span class="meta"><span class="pill${c && c.group === "parceiras" ? " dark" : ""}">${esc(tx(w.type))}</span><b>${esc(tx(w.title))}</b><small>${esc([w.artist, w.place, w.award ? "★ " + tx(w.award).split(" · ")[0] : ""].filter(Boolean).join(" · "))}</small></span>`;
  b.addEventListener("pointerenter", () => track(b));
  b.addEventListener("click", () => openPlayer(w));
  return b;
}
function catCard(c, wide){
  const list = WORKS.filter(w => w.cat === c.id), cover = list[0];
  const a = document.createElement("a");
  a.className = "cat" + (wide ? " wide" : ""); a.href = c.page;
  a.innerHTML = `${cover ? imgHTML(cover.id, "") : '<span class="fallback"></span>'}<span class="tint"></span><span class="shade"></span><span class="scan"></span><span class="track"></span>
    <span class="osdc"><span>${c.group !== "parceiras" ? "● REC" : "▶ PLAY"}</span><span>${esc(L.count(list.length).toUpperCase())}</span></span>
    <span class="meta"><span class="pill${c.group === "parceiras" ? " dark" : ""}">${esc(tx(GROUPS[c.group]))}</span><b class="glitch" data-text="${esc(tx(c.title))}">${esc(tx(c.title))}</b><small>${esc(tx(c.sub))}</small></span>`;
  a.addEventListener("pointerenter", () => { track(a); glitch(a.querySelector(".glitch")); });
  return a;
}

/* hub de categorias */
$$("[data-cats]").forEach(box => {
  const g = box.dataset.cats, wide = box.hasAttribute("data-wide");
  CATS.filter(c => (!g || c.group === g) && c.id !== box.dataset.exclude).forEach(c => box.appendChild(catCard(c, wide)));
});
/* destaques */
$$("[data-featured]").forEach(box => {
  WORKS.filter(w => w.featured).sort((a, b) => a.featured - b.featured).forEach(w => box.appendChild(workCard(w)));
});
/* página de categoria */
$$("[data-grid]").forEach(box => {
  const c = catOf(box.dataset.grid); if(!c) return;
  if(c.vertical) box.classList.add("vertical");
  WORKS.filter(w => w.cat === c.id).forEach(w => box.appendChild(workCard(w)));
  const cnt = $("[data-count]"); if(cnt) cnt.textContent = L.count(WORKS.filter(w => w.cat === c.id).length).toUpperCase();
});

/* ---------- player ---------- */
const modal = $("#player");
let lastFocus = null;
function openPlayer(w){
  if(!modal) return;
  const c = catOf(w.cat);
  lastFocus = document.activeElement;
  const box = $(".modal-box", modal);
  box.classList.toggle("v", !!(c && c.vertical));
  const lines = [];
  if(w.role) lines.push(`${L.role}: ${tx(w.role)}`);
  if(w.artist) lines.push(`${L.artist}: ${w.artist}`);
  if(w.prod) lines.push(`${L.prod}: ${w.prod}`);
  if(c) lines.push(tx(c.credit));
  if(c && c.group === "decupalm") lines.push(S.instagramAutoral.handle);
  $(".player", modal).innerHTML = `<div class="wait"><div>${L.loading}<br><a href="https://www.youtube.com/watch?v=${w.id}" target="_blank" rel="noopener">${L.watchYT} ↗</a></div></div>
    <iframe src="https://www.youtube-nocookie.com/embed/${w.id}?autoplay=1&rel=0&modestbranding=1&playsinline=1" title="${esc(tx(w.title))}" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>`;
  $(".modal-body", modal).innerHTML = `<div><span class="pill">${esc(tx(w.type))}</span><h3 style="margin-top:10px">${esc(tx(w.title))}${w.place ? ` <span class="muted" style="font-size:.55em">· ${esc(w.place)}</span>` : ""}</h3>
    <p class="credit">${esc(lines.join(" · "))}</p>${w.award ? `<p class="award-line">★ ${esc(tx(w.award))}</p>` : ""}</div>
    <a class="btn ghost" href="https://www.youtube.com/watch?v=${w.id}" target="_blank" rel="noopener">${L.watchYT} ↗</a>`;
  modal.classList.add("open"); document.body.style.overflow = "hidden";
  if(!reduce) box.animate([{opacity:0, transform:"translateY(20px) scale(.97)"},{opacity:1, transform:"none"}], {duration:450, easing:"cubic-bezier(.33,1,.68,1)"});
  history.replaceState(null, "", "#" + w.id);
  $(".close", modal).focus();
}
function closePlayer(){
  if(!modal || !modal.classList.contains("open")) return;
  modal.classList.remove("open"); document.body.style.overflow = "";
  $(".player", modal).innerHTML = "";
  history.replaceState(null, "", location.pathname + location.search);
  lastFocus && lastFocus.focus();
}
if(modal){
  $(".close", modal).addEventListener("click", closePlayer);
  modal.addEventListener("click", e => { if(e.target === modal) closePlayer(); });
  addEventListener("keydown", e => { if(e.key === "Escape") closePlayer(); });
  // botões que abrem um vídeo pelo id (ex.: quadros de prêmios)
  $$("[data-play]").forEach(b => b.addEventListener("click", () => { const w = WORKS.find(x => x.id === b.dataset.play); if(w) openPlayer(w); }));
  const h = decodeURIComponent(location.hash.slice(1));
  const w = h && WORKS.find(x => x.id === h);
  if(w) setTimeout(() => openPlayer(w), 300);
}

/* ---------- hero com tarjas ---------- */
const heroWrap = $(".hero-wrap"), hero = $(".hero");
if(heroWrap && hero){
  const bg = $(".bg", hero), barT = $(".bar.t", hero), barB = $(".bar.b", hero), tc = $("[data-tc]", hero), pct = $("[data-pct]", hero);
  const lines = $$(".line", hero);
  const ease = t => 1 - Math.pow(1 - t, 3);
  // quanto cada linha pode alargar sem passar da largura da tela (evita quebrar linha e o texto pular)
  let caps = lines.map(() => 35);
  function measureCaps(){
    const avail = hero.clientWidth - 40;
    caps = lines.map(l => {
      const prev = l.style.fontVariationSettings;
      l.style.fontVariationSettings = '"wdth" 100'; const a = l.getBoundingClientRect().width;
      l.style.fontVariationSettings = '"wdth" 135'; const b = l.getBoundingClientRect().width;
      l.style.fontVariationSettings = prev;
      return b <= avail ? 35 : Math.max(0, 35 * (avail - a) / Math.max(1, b - a));
    });
    last = -1;
  }
  let last = -1;
  const fmt = s => { const S2 = Math.floor(s) % 60, M = Math.floor(s / 60) % 60; return `SP 0:${String(M).padStart(2,"0")}:${String(S2).padStart(2,"0")}`; };
  function render(){
    const r = heroWrap.getBoundingClientRect(), total = r.height - hero.offsetHeight;
    const p = Math.min(1, Math.max(0, -r.top / Math.max(1, total)));
    if(Math.abs(p - last) < .0005) return; last = p;
    const w = hero.offsetWidth, h = hero.offsetHeight, bar = Math.max(0, (h - w / 2.39) / 2);
    const b = bar * (1 - ease(Math.min(1, p * 1.6)));
    barT.style.height = b + "px"; barB.style.height = b + "px";
    bg.style.transform = `scale(${1.15 - .15 * ease(p)})`;
    lines.forEach((l, i) => {
      if(reduce) return;
      const lp = Math.min(1, Math.max(0, (p - i * .06) / .5)), e = ease(lp);
      // "translate" (e não "transform"): o glitch anima o transform e não pode desfazer a subida da linha
      l.style.translate = `0 ${(-e * (30 + i * 14)).toFixed(1)}px`;
      l.style.fontVariationSettings = `"wdth" ${(100 + caps[i] * e).toFixed(1)}`;
      if(lp > .02 && lp < 1 && !l._g){ l._g = 1; glitch(l); } if(lp === 0) l._g = 0;
    });
    if(tc) tc.textContent = fmt(p * 24);
    if(pct) pct.textContent = `CH 03 · ${Math.round(p * 100)}%`;
  }
  const loop = () => { render(); requestAnimationFrame(loop); }; loop();
  measureCaps();
  if(document.fonts && document.fonts.ready) document.fonts.ready.then(measureCaps);
  addEventListener("resize", measureCaps);
  setTimeout(() => lines.forEach((l, i) => setTimeout(() => glitch(l), i * 140)), 350);
  // showreel no fundo (mudo, em loop); só o pôster se "reduzir movimento" ou economia de dados
  const saveData = navigator.connection && navigator.connection.saveData;
  const R = S.showreel;
  if(R){
    bg.style.backgroundImage = `url("${R.poster}")`;
    bg.classList.add("has-poster");
    if(!reduce && !saveData){
      const v = document.createElement("video");
      v.muted = true; v.loop = true; v.playsInline = true; v.autoplay = true; v.setAttribute("aria-hidden", "true");
      v.poster = R.poster; v.src = innerWidth > 900 ? R.hd : R.sd;
      v.addEventListener("playing", () => v.classList.add("ready"), { once: true });
      bg.appendChild(v); v.play().catch(() => {});
    }
  }
}

/* ---------- showreel em tela cheia, sem nada por cima ---------- */
const reel = $("#reel");
if(reel && S.showreel){
  const rv = $("video", reel), rc = $(".reel-close", reel);
  let idle, lastF = null;
  const wake = () => { reel.classList.remove("idle"); clearTimeout(idle); idle = setTimeout(() => reel.classList.add("idle"), 1800); };
  function openReel(){
    lastF = document.activeElement;
    if(!rv.getAttribute("src")){ rv.poster = S.showreel.poster; rv.src = innerWidth > 900 ? S.showreel.hd : S.showreel.sd; }
    reel.hidden = false; document.body.style.overflow = "hidden";
    requestAnimationFrame(() => reel.classList.add("open"));
    rv.currentTime = 0; rv.play().catch(() => {});
    rc.focus(); wake();
  }
  function closeReel(){
    if(reel.hidden) return;
    reel.classList.remove("open"); rv.pause(); document.body.style.overflow = "";
    setTimeout(() => { reel.hidden = true; }, 300);
    lastF && lastF.focus();
  }
  $$("[data-reel-open]").forEach(b => b.addEventListener("click", openReel));
  rc.addEventListener("click", closeReel);
  rv.addEventListener("click", closeReel);
  reel.addEventListener("pointermove", wake);
  addEventListener("keydown", e => { if(e.key === "Escape") closeReel(); });
}

/* ---------- grades sem buraco na última linha ----------
   Escolhe o nº de colunas para equilibrar as linhas e estica os itens da última linha. */
function balance(box, minW, ratio, maxH){
  const items = [...box.children], n = items.length; if(!n) return;
  const gap = 16, W = box.clientWidth;
  const maxCols = Math.max(1, Math.min(n, Math.floor((W + gap) / (minW + gap))));
  const rows = Math.ceil(n / maxCols), cols = Math.ceil(n / rows);
  const last = n - (rows - 1) * cols;
  const tracks = last === cols ? cols : cols * last;
  const itemW = (W - (cols - 1) * gap) / cols;
  box.style.gridTemplateColumns = `repeat(${tracks}, 1fr)`;
  box.style.gridAutoRows = Math.min(maxH, itemW * ratio) + "px";
  box.classList.add("balanced");
  items.forEach((el, i) => { el.style.gridColumn = `span ${i >= (rows - 1) * cols ? tracks / last : tracks / cols}`; });
}
/* quadros de texto (ex.: habilidades): mesmo equilíbrio, sem altura fixa */
function balanceText(box){
  const items = [...box.children], n = items.length; if(!n) return;
  const minW = +box.dataset.balance || 220, gap = parseFloat(getComputedStyle(box).columnGap) || 12, W = box.clientWidth;
  const maxCols = Math.max(1, Math.min(n, Math.floor((W + gap) / (minW + gap))));
  const rows = Math.ceil(n / maxCols), cols = Math.ceil(n / rows), last = n - (rows - 1) * cols;
  const tracks = last === cols ? cols : cols * last;
  box.style.gridTemplateColumns = `repeat(${tracks}, minmax(0,1fr))`;
  items.forEach((el, i) => { el.style.gridColumn = `span ${i >= (rows - 1) * cols ? tracks / last : tracks / cols}`; });
}
const balanced = [];
$$("[data-balance]").forEach(box => balanced.push(() => balanceText(box)));
$$("[data-cats]").forEach(box => { const wide = box.hasAttribute("data-wide"); balanced.push(() => balance(box, 270, wide ? 10/16 : 5/4, wide ? 380 : 520)); });
$$("[data-grid]").forEach(box => { const v = box.classList.contains("vertical"); balanced.push(() => balance(box, v ? 220 : 320, v ? 16/9 : 9/16, v ? 640 : 420)); });
const runBalance = () => balanced.forEach(f => f());
runBalance();
if(window.ResizeObserver){ let t; new ResizeObserver(() => { cancelAnimationFrame(t); t = requestAnimationFrame(runBalance); }).observe(document.body); }

/* ---------- largura da fonte no scroll (títulos de seção) ---------- */
const stretch = $$("h2[data-stretch]");
if(stretch.length && !reduce){
  const upd = () => { const vh = innerHeight; stretch.forEach(el => { const r = el.getBoundingClientRect(); const p = Math.min(1, Math.max(0, (vh - r.top) / (vh * .6))); el.style.fontVariationSettings = `"wdth" ${(140 - 40 * (1 - Math.pow(1 - p, 3))).toFixed(1)}`; }); };
  addEventListener("scroll", upd, { passive: true }); upd();
}

/* ---------- formulário de orçamento ---------- */
const form = $("#quote-form");
if(form){
  const ENDPOINT = `https://formsubmit.co/ajax/${S.email}`;
  // abre a conexão com o serviço de envio antes do clique (tira ~0,5 s do envio)
  const pre = document.createElement("link"); pre.rel = "preconnect"; pre.href = "https://formsubmit.co"; pre.crossOrigin = ""; document.head.appendChild(pre);
  let warmed = false;
  form.addEventListener("focusin", () => { if(warmed) return; warmed = true; fetch("https://formsubmit.co/", { mode: "no-cors", cache: "no-store" }).catch(() => {}); });
  const btn = $('button[type="submit"]', form), st = $(".form-status", form);
  form.addEventListener("submit", async e => {
    e.preventDefault();
    if(!form.reportValidity()) return;
    const data = Object.fromEntries(new FormData(form));
    if(data._honey) return;
    // tudo acontece aqui no site: resposta na hora e, se o envio falhar, os dados ficam no formulário para tentar de novo
    // o FormSubmit pode levar mais de 1 minuto para responder: confirmamos na hora e o envio termina em segundo plano
    // (keepalive mantém o envio mesmo se a pessoa fechar a página). Se o serviço recusar, avisamos e os dados voltam.
    const saved = Object.fromEntries(new FormData(form));
    btn.disabled = true; btn.classList.add("is-sent");
    st.className = "form-status ok"; st.textContent = L.sent;
    // envio "simples" (FormData, sem JSON): não precisa da consulta prévia do navegador, então chega mais rápido
    const fd = new FormData(form);
    fd.delete("_honey");
    fd.append("_subject", `Orçamento pelo site · ${data.tipo || ""}`);
    fd.append("_template", "table");
    fd.append("_captcha", "false");
    form.reset();
    setTimeout(() => { btn.disabled = false; btn.classList.remove("is-sent"); btn.textContent = L.send; }, 3000);
    let ok = false, answered = false;
    try{
      const r = await fetch(ENDPOINT, { method: "POST", keepalive: true, headers: { Accept: "application/json" }, body: fd });
      const j = await r.json().catch(() => ({}));
      answered = true;
      ok = r.ok && String(j.success) === "true";
      if(!ok) console.warn("Envio do orçamento:", r.status, j.message || "");
    }catch(err){ console.warn("Envio do orçamento:", err); }
    if(!ok && (answered || navigator.onLine === false)){
      // recusado ou sem internet: devolve o que a pessoa escreveu e oferece tentar de novo
      Object.entries(saved).forEach(([k, v]) => { if(form.elements[k] && k !== "_honey") form.elements[k].value = v; });
      st.className = "form-status err"; st.textContent = L.fail; btn.textContent = L.retry; btn.disabled = false; btn.classList.remove("is-sent");
    }
  });
}

/* ---------- troca de página: efeito rebobinar ---------- */
if(!reduce){
  document.body.classList.add("page-in");
  setTimeout(() => document.body.classList.remove("page-in"), 400);
  document.addEventListener("click", e => {
    const a = e.target.closest("a[href]"); if(!a) return;
    const href = a.getAttribute("href");
    if(!href || a.target === "_blank" || e.metaKey || e.ctrlKey || e.shiftKey || href.startsWith("#") || /^(https?:|mailto:|tel:)/.test(href)) return;
    e.preventDefault(); document.body.classList.add("page-out");
    setTimeout(() => { location.href = href; }, 190);
  });
  addEventListener("pageshow", ev => { if(ev.persisted) document.body.classList.remove("page-out"); });
}

bindGlitch(); bindReveal();
})();
