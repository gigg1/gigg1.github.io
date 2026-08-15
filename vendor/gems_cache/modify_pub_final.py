# -*- coding: utf-8 -*-
"""调整 publication 卡片：
1. venue 颜色与作者一致 + 加粗
2. extra_note 移到 meta 行作为 tag
3. paper/code/supp 恢复为方括号链接形式
"""
import io

path = "/Users/giggliu/Downloads/PrivateInformation/Website/gigg1.github.io/aboutme.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

# ============ 1. CSS: venue 颜色与作者一致 + 加粗 ============
old_venue = '''  .pub-card .pub-venue {
    grid-area: venue;
    min-width: 0;
    margin: 0 0 0.18rem;
    color: #8f6670;
    font-size: 0.68rem;
    font-weight: 600;
    line-height: 1.35;
  }'''
new_venue = '''  .pub-card .pub-venue {
    grid-area: venue;
    min-width: 0;
    margin: 0 0 0.18rem;
    color: #6f666a;
    font-size: 0.78rem;
    font-weight: 700;
    line-height: 1.38;
  }'''
if old_venue in content:
    content = content.replace(old_venue, new_venue, 1)
    print("OK: venue 样式已更新")
else:
    print("WARN: venue 样式未匹配")

# ============ 2. CSS: pub-links 恢复为普通文本链接 ============
old_links_css = '''  .pub-card .pub-links {
    grid-area: links;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.3rem;
    min-width: 0;
  }
  .pub-card .pub-link-tag {
    display: inline-flex;
    align-items: center;
    padding: 0.12rem 0.44rem;
    border: 1px solid rgba(185, 137, 146, 0.3);
    border-radius: 999px;
    background: rgba(216, 167, 173, 0.13);
    color: #8f6670;
    font-size: 0.58rem;
    font-weight: 780;
    line-height: 1;
    text-decoration: none;
    transition: background 180ms ease, border-color 180ms ease, color 180ms ease;
  }
  .pub-card .pub-link-tag:hover {
    background: rgba(216, 167, 173, 0.24);
    border-color: rgba(185, 137, 146, 0.5);
    color: #6f4d57;
  }'''
new_links_css = '''  .pub-card .pub-links {
    grid-area: links;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.15rem;
    min-width: 0;
    color: #6f666a;
    font-size: 0.78rem;
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
  /* extra_note 徽章（与年份 tag 同风格） */
  .pub-card .pub-note-tag {
    display: inline-flex;
    align-items: center;
    padding: 0.08rem 0.36rem;
    border: 1px solid rgba(185, 137, 146, 0.3);
    border-radius: 999px;
    background: rgba(216, 167, 173, 0.13);
    color: #8f6670;
    font-size: 0.58rem;
    font-weight: 780;
    line-height: 1.15;
  }'''
if old_links_css in content:
    content = content.replace(old_links_css, new_links_css, 1)
    print("OK: pub-links 样式已更新")
else:
    print("WARN: pub-links 样式未匹配")

# ============ 3. HTML 循环体：extra_note 移到 meta 行，链接恢复方括号形式 ============
old_loop = '''  <p class="pub-meta">
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
  </div>'''

new_loop = '''  <p class="pub-meta">
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
  <p class="pub-venue">{{ pub.venue }}</p>
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

if old_loop in content:
    content = content.replace(old_loop, new_loop, 1)
    print("OK: 循环体已更新")
else:
    print("WARN: 循环体未匹配")

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("完成")
