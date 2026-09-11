---
layout: page
title: Research
---

{% assign pubs = site.data.publications %}
{% assign published_pubs = pubs | where: "status", "published" %}

<!-- 各主题的论文 key（对应 _data/publications.yml 中的 key 字段） -->
{% assign keys_risk    = "malaria,transcode" | split: "," %}
{% assign keys_pred    = "csursurvey,epidl" | split: "," %}
{% assign keys_marl    = "dcg" | split: "," %}
{% assign keys_control = "wi,optimal" | split: "," %}

{% assign topics = "marl,risk,pred,control" | split: "," %}
{% assign titles = "MARL for Learning Cooperative Behavior in Multi-agent Systems|ML for Assessing Infectious Disease Risk and Inferring Transmission Patterns|ML for Epidemic Dynamics Prediction|ML &amp; RL for Infectious Disease Control" | split: "|" %}
{% assign descs = "Developing multi-agent reinforcement learning methods that learn effective cooperative behavior under complex and dynamic interactions.|Using machine learning to assess transmission intensity, uncover hidden transmission patterns, and identify heterogeneous risk factors from spatiotemporal surveillance data.|Forecasting epidemic dynamics with epidemiological priors and deep spatiotemporal models, including survey-level syntheses of the field.|Inferring adaptive intervention strategies and allocating limited resources for effective disease control.|" | split: "|" %}

<p class="research-intro">
My work aims to solve complex real-world problems such as infectious disease transmission risk assessment and prediction,
adaptive intervention strategy inference, and effective cooperative behavior learning in multi-agent systems.
My research spans AI/ML methodology development and application deployment in the context of infectious disease dynamics,
organized into the four topics below. Each topic lists representative publications, and the complete list is maintained on the
<a href="{{ '/aboutme' | relative_url }}">About Me</a> page.
</p>

<div class="topics">
{% for topic in topics %}
  {% assign idx = forloop.index0 %}
  {% case topic %}
    {% when "risk" %}{% assign pkeys = keys_risk %}
    {% when "pred" %}{% assign pkeys = keys_pred %}
    {% when "marl" %}{% assign pkeys = keys_marl %}
    {% when "control" %}{% assign pkeys = keys_control %}
  {% endcase %}

  <section class="topic">
    <h3 class="topic__head">{{ titles[idx] }}</h3>
    <p class="topic__desc">{{ descs[idx] }}</p>
    <div class="topic__papers">
      {% assign found = false %}
      {% for key in pkeys %}
        {% for pub in published_pubs %}
          {% if pub.key == key %}
            {% assign found = true %}
            {% include pub-card.html pub=pub level=4 %}
          {% endif %}
        {% endfor %}
      {% endfor %}
      {% unless found %}
        <p class="topic__empty">Selected publications coming soon.</p>
      {% endunless %}
    </div>
  </section>
{% endfor %}
</div>

<p class="research-note">
A complete and up-to-date publication list is available on the
<a href="{{ '/aboutme' | relative_url }}">About Me</a> page and on
<a href="https://scholar.google.com/citations?user=erU2odMAAAAJ&amp;hl=en">Google Scholar</a>.
</p>

{% include pub-lightbox.html %}
