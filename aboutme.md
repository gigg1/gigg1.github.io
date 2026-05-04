---
layout: page
title: About me
<!-- subtitle: This is a page to show my basic information :> -->
---

Hello there! I am **Mutong LIU** (刘牧潼), a Ph.D. candidate in the [Department of Computer Science at Hong Kong Baptist University](https://www.comp.hkbu.edu.hk/v1/), supervised by [Prof. Yang LIU](https://www.comp.hkbu.edu.hk/v1/?page=profile&id=csygliu) and co-supervised by [Prof. Jiming LIU](https://www.comp.hkbu.edu.hk/v1/?page=profile&id=jiming).
My primary research interests inlcudes **artificial intelligence, machine learning, computational epidemiology, and complex system modeling**, specifically focus on developing multi-agent reinforcement learning, physical/epidemiological-informed machine learning, and spatiotemporal analysis methods.
<!--I also maintain a broad interest in methodology development of multi-agent RL and spatiotemporal analytics.-->
<!--developing and leveraging methodology in machine learning (ML) and reinforcement learning (RL) combined with epidemiological modeling to assess, predict, and control infectious diseases risk. I also maintain a broad interest in methodology development of multi-agent RL and spatiotemporal analytics.-->

<!--I believe that data-driven, spatiotemporally aware methods are key to building resilient public health systems.-->
My work aims to solve complex real-world problems such as infectious disease transmission risk assessment and prediction, adaptive intervention strategy inference, and effective cooperative behavior learning in multi-agent systems.
My research spans AI/ML methodology development and application deployment in the context of infectious disease dynamics:

* **MLs for Assessing Infectious Disease Risk and Inferring Transmission Patterns:**  
	[Malaria Transmission Intensity Assessment (IDM’23)](./papers/2023-Assessing-IDM.pdf) · [TransCode for COVID‑19 Transmission Patterns (IDP’23)](./papers/2023-TransCode-IDP.pdf)

* **MLs for Epidemic Dynamics Prediction:**  
  [Survey on ML for Infectious Disease Risk Prediction (ACM CSUR’25)](./papers/2025-Machine-ACMCSUR.pdf) · [EpiDL (CIKM’23)](./papers/2023-Epidemiology-aware-CIKM.pdf)
	
* **MLs & RLs for Infectious Disease Control:**  
	[RLs in Infectious Disease Control (WI‑IAT’25)](./papers/2026-Empowering-WI.pdf) · [Resource Allocation for Effective Disease Control (IDP’22)](./papers/2022-Optimal-IDP.pdf)
	
* **MARL for Learning Cooperative Behavior in Multi-agent Systems:**  
	Probing Diametric Coordination Graphs for Multi-Agent Reinforcement Learning [Under Review]
	
<!--	effective coordination in cooperative Multi-agent RL-->


<!--* **Application/Deployment for Public Health:**  
   · -->
  
<!--[Influential Spreaders (Frontiers’22)](./papers/2022-Identifying-Frontiers.pdf)-->

<!--with Complex Network-->


<!--If you are interested in my research work or any other aspects, you can reach me via my email address (<a href="mailto:gigg0@icloud.com">gigg0@icloud.com</a> or  <a href="mailto:csmtliu@comp.hkbu.edu.hk">csmtliu@comp.hkbu.edu.hk</a>).-->

------
Email address: <a href="mailto:csmtliu@comp.hkbu.edu.hk">csmtliu@comp.hkbu.edu.hk</a> (Academic)  ·  <a href="mailto:gigg0@icloud.com">gigg0@icloud.com</a> (Personal)

------



### Research Interests

- Machine Learning, Reinforcement Learning, Spatiotemporal Analytics, Epidemic Prediction, Infectious Disease Modeling and Control

------



### Education and Academic Qualification

| Period                | Degree                                                       | Major               |
| --------------------- | ------------------------------------------------------------ | ------------------- |
| Jan.2021 - Present    | PhD Candidate in Computer Science, **Hong Kong Baptist University**, Hong Kong, China | Computer Science    |
| Sept.2016 - Jul. 2020 | B.E. in Network Engineering, **Southwest University**, Chongqing, China | Network Engineering |
| Sept.2015 - Jul. 2016 | Student in Plant Protection Faculty, **Southwest University**, Chongqing, China | Plant Protection    |

------
### Publications ([Google Scholar](https://scholar.google.com/citations?user=erU2odMAAAAJ&hl=en))

{% assign pubs = site.data.publications %}

{% comment %} 分组：Published 和 Under Review {% endcomment %}
{% assign published_pubs = pubs | where: "status", "published" %}
{% assign under_review_pubs = pubs | where: "status", "under_review" %}

**Published:**

{% for pub in published_pubs %}
<div style="display: flex; margin-bottom: 1.8rem; gap: 1rem; align-items: flex-start;">
  <div style="flex: 0 0 140px;">
    <img src="{{ pub.img }}" alt="{{ pub.title }}" style="width: 100%; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
  </div>
  <div style="flex: 1;">
    {% assign authors_highlighted = pub.authors | replace: "Mutong Liu", "<strong>Mutong Liu</strong>" %}
    {{ authors_highlighted }} ({{ pub.year }}).
    {% if pub.links.doi %}
      <a href="{{ pub.links.doi }}">{{ pub.title }}</a>.
    {% else %}
      {{ pub.title }}.
    {% endif %}
    <em>{{ pub.venue }}</em>.
    {% if pub.links.pdf %}
      [<a href="{{ pub.links.pdf }}">paper</a>]
    {% endif %}
    {% if pub.links.supp %}
      [<a href="{{ pub.links.supp }}">supplementary</a>]
    {% endif %}
    {% if pub.links.poster %}
      [<a href="{{ pub.links.poster }}">poster</a>]
    {% endif %}
    {% if pub.links.code %}
      [<a href="{{ pub.links.code }}">code</a>]
    {% endif %}
    {% comment %} ★ 在链接末尾添加自定义介绍（例如：“(CIKM '23 接收率20%)”） ★ {% endcomment %}
    {% if pub.extra_note %}
      [<u>{{ pub.extra_note }}</u>]
    {% endif %}
  </div>
</div>
{% endfor %}

**Under Review:**

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
{% endfor %}

\* Co-first author (Contributed equally).