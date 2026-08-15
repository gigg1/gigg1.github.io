---
layout: page
title: Mutong LIU
show-avatar: false
<!-- subtitle: This is a page to show my basic information :> -->
---

<div class="profile-intro">
  <div class="profile-intro__photo">
    <img src="/assets/img/IMG_7496-2.jpeg" alt="Mutong LIU">
  </div>
  <div class="profile-intro__text">

<p>Hello there! I am <strong>Mutong LIU</strong> (刘牧潼), a Ph.D. candidate in the <a href="https://www.comp.hkbu.edu.hk/v1/">Department of Computer Science at Hong Kong Baptist University</a>, supervised by <a href="https://www.comp.hkbu.edu.hk/v1/?page=profile&id=csygliu">Prof. Yang LIU</a> and co-supervised by <a href="https://www.comp.hkbu.edu.hk/v1/?page=profile&id=jiming">Prof. Jiming LIU</a>.</p>
<p>My primary research interests inlcudes <strong>artificial intelligence, machine learning, reinforcement learning, computational epidemiology, and complex system modeling</strong>, specifically focus on developing multi-agent reinforcement learning algorithms, physical/epidemiological-informed machine learning methods, and spatiotemporal analysis methods, as well as their applications in practical scenarios.</p>
<!--I also maintain a broad interest in methodology development of multi-agent RL and spatiotemporal analytics.-->
<!--developing and leveraging methodology in machine learning (ML) and reinforcement learning (RL) combined with epidemiological modeling to assess, predict, and control infectious diseases risk. I also maintain a broad interest in methodology development of multi-agent RL and spatiotemporal analytics.-->


<!--I believe that data-driven, spatiotemporally aware methods are key to building resilient public health systems.-->
  </div>
</div>

------
<!-- ### Research Interests
- Machine Learning, Reinforcement Learning, Spatiotemporal Analytics, Epidemic Prediction, Infectious Disease Modeling and Control -->
### Research Topics
My work aims to solve complex real-world problems such as infectious disease transmission risk assessment and prediction, adaptive intervention strategy inference, and effective cooperative behavior learning in multi-agent systems. Specifically, My research spans AI/ML methodology development and application deployment in the context of infectious disease dynamics:

<div class="research-grid">
<div class="research-card">
  <div class="research-card__title">MLs for Assessing Infectious Disease Risk and Inferring Transmission Patterns</div>
  <div class="research-card__links">
<a href="/papers/2023-Assessing-IDM.pdf">Malaria Transmission Intensity Assessment (IDM’23)</a>
<a href="/papers/2023-TransCode-IDP.pdf">TransCode for COVID‑19 Transmission Patterns (IDP’23)</a>
  
  </div>
</div>

<div class="research-card">
  <div class="research-card__title">MLs for Epidemic Dynamics Prediction</div>
  <div class="research-card__links">
<a href="/papers/2025-Machine-ACMCSUR.pdf">Survey on ML for Infectious Disease Risk Prediction (ACM CSUR’25)</a>
<a href="/papers/2023-Epidemiology-aware-CIKM.pdf">EpiDL (CIKM’23)</a>
  
  </div>
</div>

<div class="research-card">
  <div class="research-card__title">MARL for Learning Cooperative Behavior in Multi-agent Systems</div>
  <div class="research-card__links">
<a href="https://www.sciencedirect.com/science/article/pii/S0004370226001293">Diametric Coordination Graphs for MARL (AIJ'26)</a>
  
  </div>
</div>

<div class="research-card">
  <div class="research-card__title">MLs &amp; RLs for Infectious Disease Control</div>
  <div class="research-card__links">
<a href="/papers/2026-Empowering-WI.pdf">RLs in Infectious Disease Control (WI‑IAT’25)</a>
<a href="/papers/2022-Optimal-IDP.pdf">Resource Allocation for Effective Disease Control (IDP’22)</a>
  
  </div>
</div>
</div>
<!--	effective coordination in cooperative Multi-agent RL-->


<!--* **Application/Deployment for Public Health:**  
   · -->
  
<!--[Influential Spreaders (Frontiers’22)](./papers/2022-Identifying-Frontiers.pdf)-->

<!--with Complex Network-->


<!--If you are interested in my research work or any other aspects, you can reach me via my email address (<a href="mailto:gigg0@icloud.com">gigg0@icloud.com</a> or  <a href="mailto:csmtliu@comp.hkbu.edu.hk">csmtliu@comp.hkbu.edu.hk</a>).-->

------
Email address: <a href="mailto:csmtliu@comp.hkbu.edu.hk">csmtliu@comp.hkbu.edu.hk</a> (Academic)  ·  <a href="mailto:gigg0@icloud.com">gigg0@icloud.com</a> (Personal)


<!-- ------

### Education and Academic Qualification

| Period                | Degree                                                       | Major               |
| --------------------- | ------------------------------------------------------------ | ------------------- |
| Jan.2021 - Present    | PhD Candidate in Computer Science, **Hong Kong Baptist University**, Hong Kong, China | Computer Science    |
| Sept.2016 - Jul. 2020 | B.E. in Network Engineering, **Southwest University**, Chongqing, China | Network Engineering |
| Sept.2015 - Jul. 2016 | Student in Plant Protection Faculty, **Southwest University**, Chongqing, China | Plant Protection    | -->

------
### Publications ([Google Scholar](https://scholar.google.com/citations?user=erU2odMAAAAJ&hl=en))

{% assign pubs = site.data.publications %}

{% comment %} 分组：Published 和 Under Review {% endcomment %}
{% assign published_pubs = pubs | where: "status", "published" %}
{% assign under_review_pubs = pubs | where: "status", "under_review" %}

<style>
  /* 整页字体统一为 Trebuchet MS（macOS 和 Windows 均自带） */
  .container-md, .container-md h1, .container-md h2, .container-md h3,
  .container-md h4, .container-md h5, .container-md h6, .container-md p,
  .container-md a, .container-md li, .container-md td, .container-md th,
  .container-md strong, .container-md em, .container-md span, .container-md div {
    font-family: 'Trebuchet MS', 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  }
  /* 正文所有非链接文字统一为深墨色（链接保持玫瑰棕） */
  .container-md, .container-md h1, .container-md h2, .container-md h3,
  .container-md h4, .container-md h5, .container-md h6, .container-md p,
  .container-md li, .container-md td, .container-md th,
  .container-md strong, .container-md em, .container-md span {
    color: #3d3238;
  }
  /* 正文所有链接统一为玫瑰棕色（覆盖主题默认蓝色） */
  .container-md a {
    color: #805762;
  }
  .container-md a:hover {
    color: #6f4d57;
  }
  /* 右侧头像 + 左侧简介布局 */
  .profile-intro {
    display: flex;
    gap: 2rem;
    align-items: flex-start;
    margin-bottom: 1.5rem;
  }
  @media (max-width: 700px) {
    .profile-intro {
      flex-direction: column;
      align-items: center;
    }
  }
  .profile-intro__photo {
    flex: 0 0 200px;
    order: 2;
  }
  .profile-intro__photo img {
    width: 100%;
    border-radius: 14px;
    border: 2px solid #ffffff;
  }
  .profile-intro__text {
    flex: 1;
    min-width: 0;
    order: 1;
  }
  /* 研究方向卡片：2×2 网格 + 左侧彩色竖条边框 */
  .research-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin-bottom: 1rem;
  }
  @media (max-width: 700px) {
    .research-grid {
      grid-template-columns: 1fr;
    }
  }
  .research-card {
    position: relative;
    display: block;
    padding: 1.2rem 1.3rem;
    border: 1px solid rgba(234, 223, 221, 0.9);
    border-left: 3px solid #d6a5aa;
    border-radius: 12px;
    background: rgba(255, 252, 250, 0.7);
    overflow: hidden;
    transition: border-color 220ms ease, box-shadow 220ms ease, transform 220ms ease;
  }
  .research-card:nth-child(1) { border-left-color: #f0d878; }
  .research-card:nth-child(2) { border-left-color: #91a390; }
  .research-card:nth-child(3) { border-left-color: #8da3b8; }
  .research-card:nth-child(4) { border-left-color: #b49bb8; }
  .research-card::after {
    position: absolute;
    top: 0;
    left: -75%;
    width: 50%;
    height: 100%;
    background: linear-gradient(105deg, transparent 0%, rgba(255, 255, 255, 0.65) 50%, transparent 100%);
    content: "";
    pointer-events: none;
    transform: skewX(-20deg);
  }
  .research-card:hover {
    transform: translateY(-3px);
    border-color: rgba(214, 165, 170, 0.5);
    box-shadow: 0 14px 32px rgba(143, 102, 112, 0.13), 0 4px 10px rgba(143, 102, 112, 0.07);
  }
  .research-card:hover::after {
    animation: research-shine 0.85s ease forwards;
  }
  @keyframes research-shine {
    0% { left: -75%; }
    100% { left: 125%; }
  }
  .research-card__title {
    font-weight: 700;
    color: #3d3238;
    margin-bottom: 0.3rem;
  }
  .research-card__links {
    color: #3d3238;
    font-size: 0.8rem;
    line-height: 1.55;
  }
  .research-card__links a {
    display: block;
    margin-bottom: 0.2rem;
    padding-left: 0.9rem;
    position: relative;
  }
  .research-card__links a::before {
    content: "\2022";
    position: absolute;
    left: 0;
    top: 0;
    color: #c07b90;
    font-size: 0.8rem;
  }
  /* publication 卡片：参考 Selected Work 布局（缩略图在左，右侧 meta/标题/作者三行，左侧粗边框） */
  .pub-card {
    display: grid;
    grid-template-columns: 11rem minmax(0, 1fr);
    grid-template-areas: "thumb meta" "thumb title" "thumb venue" "thumb authors";
    column-gap: 1rem;
    align-items: center;
    margin-bottom: 0.62rem;
    padding: 0.58rem 0.72rem;
    border: 1px solid rgba(216, 167, 173, 0.18);
    border-left: 3px solid rgba(185, 137, 146, 0.28);
    border-radius: 8px;
    background: rgba(255, 252, 250, 0.55);
    transition: border-color 220ms ease, background 220ms ease, transform 220ms ease;
  }
  @media (max-width: 700px) {
    .pub-card {
      grid-template-columns: 1fr;
      grid-template-areas: "meta" "thumb" "title" "venue" "authors";
      align-items: start;
    }
    .pub-card .pub-thumb {
      max-width: 100%;
      margin-bottom: 0.5rem;
    }
  }
  .pub-card:hover {
    border-left-color: rgba(143, 102, 112, 0.38);
    background: rgba(255, 250, 247, 0.82);
    transform: translateY(-1px);
  }
  .pub-card .pub-thumb {
    grid-area: thumb;
    width: 100%;
    aspect-ratio: 16 / 9;
    padding: 0.22rem;
    border: 1px solid rgba(216, 167, 173, 0.2);
    border-radius: 7px;
    background: rgba(255, 255, 255, 0.82);
    box-shadow: rgba(143, 102, 112, 0.07) 0 10px 24px;
    cursor: zoom-in;
    transition: border-color 180ms ease, box-shadow 180ms ease, transform 180ms ease;
  }
  .pub-card .pub-thumb:hover {
    border-color: rgba(143, 102, 112, 0.34);
    box-shadow: rgba(143, 102, 112, 0.14) 0 14px 34px;
    transform: translateY(-1px);
  }
  .pub-card .pub-thumb img {
    display: block;
    width: 100%;
    height: 100%;
    border-radius: 6px;
    object-fit: contain;
    cursor: zoom-in;
  }
  .pub-card .pub-meta {
    grid-area: meta;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.34rem;
    margin: 0 0 0.2rem;
    color: #8f6670;
    font-size: 0.68rem;
    font-weight: 720;
  }
  .pub-card .pub-tag {
    display: inline-flex;
    align-items: center;
    padding: 0.12rem 0.44rem;
    border: 1px solid rgba(185, 137, 146, 0.3);
    border-radius: 999px;
    background: rgba(216, 167, 173, 0.13);
    color: #8f6670;
    font-size: 0.62rem;
    font-weight: 780;
    line-height: 1;
  }
  .pub-card .pub-venue-badge {
    display: inline-flex;
    align-items: center;
    padding: 0.08rem 0.36rem;
    border: 1px solid rgba(185, 137, 146, 0.18);
    border-radius: 999px;
    background: rgba(255, 249, 245, 0.68);
    color: #766566;
    line-height: 1;
  }
  .pub-card .pub-title {
    grid-area: title;
    min-width: 0;
    margin: 0 0 0.15rem;
    font-size: 1.05rem;
    font-weight: 700;
    line-height: 1.25;
  }
  .pub-card .pub-title a {
    color: #805762;
    text-decoration: none;
  }
  .pub-card .pub-title a:hover {
    color: #6f4d57;
    text-decoration: underline;
  }
  .pub-card .pub-venue {
    grid-area: venue;
    min-width: 0;
    margin: 0 0 0.18rem;
    color: #3d3238;
    font-size: 0.88rem;
    font-weight: 400;
    line-height: 1.38;
  }
  .pub-card .pub-authors {
    grid-area: authors;
    min-width: 0;
    margin: 0 0 0.22rem;
    color: #3d3238;
    font-size: 0.88rem;
    line-height: 1.38;
  }
  .pub-card .pub-links {
    display: inline;
    color: #3d3238;
    font-size: 0.88rem;
    line-height: 1.38;
  }
  .pub-card .pub-links a {
    color: #8f6670;
    text-decoration: underline;
    text-underline-offset: 0.16em;
  }
  .pub-card .pub-links a:hover {
    color: #6f4d57;
  }
  /* extra_note 徽章（与年份 tag 完全同风格） */
  .pub-card .pub-note-tag {
    display: inline-flex;
    align-items: center;
    padding: 0.12rem 0.44rem;
    border: 1px solid rgba(185, 137, 146, 0.3);
    border-radius: 999px;
    background: rgba(216, 167, 173, 0.13);
    color: #8f6670;
    font-size: 0.62rem;
    font-weight: 780;
    line-height: 1;
  }
  /* Lightbox: 点击图片放大查看（毛玻璃风格） */
  .pub-lightbox {
    position: fixed;
    inset: 0;
    z-index: 9999;
    display: grid;
    place-items: center;
    padding: 1.5rem;
    background: rgba(53, 45, 49, 0.42);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    opacity: 0;
    pointer-events: none;
    transition: opacity 180ms ease;
  }
  .pub-lightbox.is-open {
    opacity: 1;
    pointer-events: auto;
  }
  .pub-lightbox__frame {
    display: grid;
    max-width: min(92vw, 1180px);
    max-height: 88vh;
    gap: 0.65rem;
    padding: 0.74rem;
    border: 1px solid rgba(234, 223, 221, 0.92);
    border-radius: 14px;
    background: rgba(255, 250, 247, 0.95);
    box-shadow: rgba(53, 45, 49, 0.28) 0 30px 90px;
    transform: translateY(8px) scale(0.985);
    transition: transform 180ms ease;
  }
  .pub-lightbox.is-open .pub-lightbox__frame {
    transform: translateY(0) scale(1);
  }
  .pub-lightbox img {
    display: block;
    max-width: calc(92vw - 1.5rem);
    max-height: calc(88vh - 4.5rem);
    border-radius: 10px;
    background: #ffffff;
    object-fit: contain;
    cursor: default;
  }
  .pub-lightbox p {
    margin: 0;
    color: #8f6670;
    font-size: 0.78rem;
    line-height: 1.35;
    text-align: center;
  }
  .pub-lightbox__close {
    position: fixed;
    top: 1rem;
    right: 1rem;
    display: grid;
    width: 2.2rem;
    height: 2.2rem;
    place-items: center;
    border: 1px solid rgba(234, 223, 221, 0.86);
    border-radius: 999px;
    background: rgba(255, 250, 247, 0.92);
    box-shadow: rgba(53, 45, 49, 0.2) 0 14px 38px;
    color: #805762;
    cursor: pointer;
    font-size: 1.25rem;
    line-height: 1;
    transition: background 180ms ease, color 180ms ease;
  }
  .pub-lightbox__close:hover {
    background: #fffaf7;
    color: #536f5a;
  }
</style>

<div class="pub-lightbox" id="pubLightbox" aria-hidden="true" onclick="if (event.target === this) closePubLightbox();">
  <button class="pub-lightbox__close" type="button" aria-label="Close image preview" onclick="closePubLightbox()">&times;</button>
  <div class="pub-lightbox__frame">
    <img id="pubLightboxImg" src="" alt="">
    <p id="pubLightboxCaption"></p>
  </div>
</div>

<script>
  function openPubLightbox(img) {
    var lb = document.getElementById('pubLightbox');
    var big = document.getElementById('pubLightboxImg');
    var cap = document.getElementById('pubLightboxCaption');
    big.src = img.src;
    big.alt = img.alt || '';
    cap.textContent = img.alt || '';
    lb.classList.add('is-open');
    lb.setAttribute('aria-hidden', 'false');
  }
  function closePubLightbox() {
    var lb = document.getElementById('pubLightbox');
    lb.classList.remove('is-open');
    lb.setAttribute('aria-hidden', 'true');
    document.getElementById('pubLightboxImg').src = '';
    document.getElementById('pubLightboxCaption').textContent = '';
  }
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { closePubLightbox(); }
  });
</script>

<!-- **Published:** -->

{% for pub in published_pubs %}
<div class="pub-card">
  <div class="pub-thumb">
    <img src="{{ pub.img }}" alt="{{ pub.title }}" onclick="openPubLightbox(this)">
  </div>
  <p class="pub-meta">
    <span class="pub-tag">{{ pub.year }}</span>
    {% if pub.extra_note %}<span class="pub-note-tag">{{ pub.extra_note }}</span>{% endif %}
  </p>
  <h3 class="pub-title">
    {% if pub.links.doi %}
      <a href="{{ pub.links.doi }}">{{ pub.title }}</a>
    {% else %}
      {{ pub.title }}
    {% endif %}
  </h3>
  <p class="pub-venue">{{ pub.venue }} <span class="pub-links">
    {% if pub.links.pdf %} [<a href="{{ pub.links.pdf }}">paper</a>]{% endif %}
    {% if pub.links.supp %} [<a href="{{ pub.links.supp }}">supplementary</a>]{% endif %}
    {% if pub.links.poster %} [<a href="{{ pub.links.poster }}">poster</a>]{% endif %}
    {% if pub.links.code %} [<a href="{{ pub.links.code }}">code</a>]{% endif %}
  </span></p>
  <p class="pub-authors">
    {% assign authors_highlighted = pub.authors | replace: "Mutong Liu", "<strong>Mutong Liu</strong>" %}
    {{ authors_highlighted }}.
  </p>
</div>
{% endfor %}

<!--**Under Review:**

{% for pub in under_review_pubs %}
<div style="display: flex; margin-bottom: 1.8rem; gap: 1rem; align-items: flex-start;">
  <div style="flex: 0 0 140px;">
    <img src="{{ pub.img }}" alt="{{ pub.title }}" style="width: 100%; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  </div>
  <div style="flex: 1;">
    {% assign authors_highlighted = pub.authors | replace: "Mutong Liu", "<strong>Mutong Liu</strong>" %}
    {{ authors_highlighted }} ({{ pub.year }}).
    {{ pub.title }}.
    <em>{{ pub.venue }}</em>.
    {% comment %} ★ 对于 under review，也可以加上相同的介绍字段（如果有的话） ★ {% endcomment %}
    {% if pub.extra_note %}
      [<u>{{ pub.extra_note }}</u>]
    {% endif %}
  </div>
</div>
{% endfor %}-->

\* Co-first author (Contributed equally).