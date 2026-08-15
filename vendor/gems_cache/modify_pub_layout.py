# -*- coding: utf-8 -*-
"""把 publication 循环体改为 Selected Work 布局"""
import io

path = "/Users/giggliu/Downloads/PrivateInformation/Website/gigg1.github.io/aboutme.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''{% for pub in published_pubs %}
<div class="pub-card">
  <div class="pub-thumb">
    <img src="{{ pub.img }}" alt="{{ pub.title }}" onclick="openPubLightbox(this)">
  </div>
  <div class="pub-info">
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
{% endfor %}'''

new = '''{% for pub in published_pubs %}
<div class="pub-card">
  <div class="pub-thumb">
    <img src="{{ pub.img }}" alt="{{ pub.title }}" onclick="openPubLightbox(this)">
  </div>
  <p class="pub-meta">
    <span class="pub-tag">{{ pub.year }}</span>
    <span class="pub-venue-badge">{{ pub.venue }}</span>
  </p>
  <h3 class="pub-title">
    {% if pub.links.doi %}
      <a href="{{ pub.links.doi }}">{{ pub.title }}</a>
    {% else %}
      {{ pub.title }}
    {% endif %}
  </h3>
  <p class="pub-authors">
    {% assign authors_highlighted = pub.authors | replace: "Mutong Liu", "<strong>Mutong Liu</strong>" %}
    {{ authors_highlighted }}.
    {% if pub.links.pdf %} [<a href="{{ pub.links.pdf }}">paper</a>]{% endif %}
    {% if pub.links.supp %} [<a href="{{ pub.links.supp }}">supplementary</a>]{% endif %}
    {% if pub.links.poster %} [<a href="{{ pub.links.poster }}">poster</a>]{% endif %}
    {% if pub.links.code %} [<a href="{{ pub.links.code }}">code</a>]{% endif %}
    {% if pub.extra_note %} [<u>{{ pub.extra_note }}</u>]{% endif %}
  </p>
</div>
{% endfor %}'''

if old in content:
    content = content.replace(old, new, 1)
    print("OK: publication 循环体已改为 Selected Work 布局")
else:
    print("WARN: 循环体未精确匹配")

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("完成")
