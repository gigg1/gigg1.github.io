# -*- coding: utf-8 -*-
"""把 aboutme.md 中 .research-card__links 里的 Markdown 链接转成 HTML <a> 标签"""
import io
import re

path = "/Users/giggliu/Downloads/PrivateInformation/Website/gigg1.github.io/aboutme.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 把研究卡片 links 区域内的 Markdown 链接 [text](url) 转为 <a href="url">text</a>
# 只处理 research-card__links 内部的链接
def convert_links(m):
    block = m.group(0)
    # 替换 [text](url) -> <a href="url">text</a>
    block = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', block)
    return block

new_content = re.sub(
    r'(<div class="research-card__links">\s*)(.*?)(\s*</div>)',
    lambda m: m.group(1) + convert_links(m) + m.group(3),
    content,
    flags=re.DOTALL,
)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("完成：Markdown 链接已转为 HTML <a> 标签")
