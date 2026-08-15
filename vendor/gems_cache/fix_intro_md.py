# -*- coding: utf-8 -*-
"""把 profile-intro__text 内的 Markdown 语法（加粗、链接）转为 HTML 标签"""
import io
import re

path = "/Users/giggliu/Downloads/PrivateInformation/Website/gigg1.github.io/aboutme.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 定位 profile-intro__text 内的内容
start = content.index('<div class="profile-intro__text">')
end = content.index('  </div>\n</div>\n\n<div class="research-grid">')
block = content[start:end]

# 1. 链接 [text](url) -> <a href="url">text</a>
block = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', block)

# 2. 加粗 **text** -> <strong>text</strong>
block = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', block)

content = content[:start] + block + content[end:]

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("完成：简介 Markdown 已转为 HTML")
