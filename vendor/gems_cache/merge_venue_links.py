# -*- coding: utf-8 -*-
"""将 paper/code 等链接合并到 venue 行内"""
import io

path = "/Users/giggliu/Downloads/PrivateInformation/Website/gigg1.github.io/aboutme.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''  <p class="pub-venue">{{ pub.venue }}</p>
  <p class="pub-authors">
    {% assign authors_highlighted = pub.authors | replace: "Mutong Liu", "<strong>Mutong Liu</strong>" %}
    {{ authors_highlighted }}.
  </p>
  <div class="pub-links">
    {% if pub.links.pdf %} [<a href="{{ pub.links.pdf }}">paper</a>]{% endif %}
    {% if pub.links.supp %} [<a href="{{ pub.links.supp }}">supplementary</a>]{% endif %}
    {% if pub.links.poster %} [<a href="{{ pub.links.poster }}">poster</a>]{% endif %}
    {% if pub.links.code %} [<a href="{{ pub.links.code }}">code</a>]{% endif %}
  </div>'''

new = '''  <p class="pub-venue">{{ pub.venue }} <span class="pub-links">
    {% if pub.links.pdf %} [<a href="{{ pub.links.pdf }}">paper</a>]{% endif %}
    {% if pub.links.supp %} [<a href="{{ pub.links.supp }}">supplementary</a>]{% endif %}
    {% if pub.links.poster %} [<a href="{{ pub.links.poster }}">poster</a>]{% endif %}
    {% if pub.links.code %} [<a href="{{ pub.links.code }}">code</a>]{% endif %}
  </span></p>
  <p class="pub-authors">
    {% assign authors_highlighted = pub.authors | replace: "Mutong Liu", "<strong>Mutong Liu</strong>" %}
    {{ authors_highlighted }}.
  </p>'''

if old in content:
    content = content.replace(old, new, 1)
    print("OK: 链接已合并到 venue 行")
else:
    print("WARN: 未匹配到目标块")

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("完成")
