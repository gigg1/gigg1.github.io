# -*- coding: utf-8 -*-
"""调整 publication 循环体：venue 移到 title 下方，链接做成 tag"""
import io

path = "/Users/giggliu/Downloads/PrivateInformation/Website/gigg1.github.io/aboutme.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''{% for pub in published_pubs %}
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

new = '''{% for pub in published_pubs %}
<div class="pub-card">
  <div class="pub-thumb">
    <img src="{{ pub.img }}" alt="{{ pub.title }}" onclick="openPubLightbox(this)">
  </div>
  <p class="pub-meta">
    <span class="pub-tag">{{ pub.year }}</span>
  </p>
  <h3 class="pub-title">
    {% if pub.links.doi %}
      <a href="{{ pub.links.doi }}">{{ pub.title }}</a>
    {% else %}
      {{ pub.title }}
    {% endif %}
  </h3>
  <p class="pub-venue">{{ pub.venue }}</p>
  <p class="pub-authors">
    {% assign authors_highlighted = pub.authors | replace: "Mutong Liu", "<strong>Mutong Liu</strong>" %}
    {{ authors_highlighted }}.
  </p>
  <div class="pub-links">
    {% if pub.links.pdf %}<a class="pub-link-tag" href="{{ pub.links.pdf }}">paper</a>{% endif %}
    {% if pub.links.supp %}<a class="pub-link-tag" href="{{ pub.links.supp }}">supplementary</a>{% endif %}
    {% if pub.links.poster %}<a class="pub-link-tag" href="{{ pub.links.poster }}">poster</a>{% endif %}
    {% if pub.links.code %}<a class="pub-link-tag" href="{{ pub.links.code }}">code</a>{% endif %}
    {% if pub.extra_note %}<span class="pub-link-tag pub-note-tag">{{ pub.extra_note }}</span>{% endif %}
  </div>
</div>
{% endfor %}'''

if old in content:
    content = content.replace(old, new, 1)
    print("OK: publication 循环体已更新（venue 在标题下，链接做成 tag）")
else:
    print("WARN: 循环体未精确匹配")

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("完成")
