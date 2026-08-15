# -*- coding: utf-8 -*-
"""删除 research-card__links 中链接之间的 · 分隔符"""
import io

path = "/Users/giggliu/Downloads/PrivateInformation/Website/gigg1.github.io/aboutme.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 删除链接之间的 " · " 分隔符（在 </a> 和下一个 <a 之间）
# 处理形式: </a> · <a ...> -> </a>\n<a ...> (配合 block 显示每行一个)
content = content.replace('</a>\u2009\u00b7\u202f<a', '</a>\n<a')
content = content.replace('</a> \u00b7\u202f<a', '</a>\n<a')
content = content.replace('</a>\u202f\u00b7\u202f<a', '</a>\n<a')
content = content.replace('</a> \u00b7 <a', '</a>\n<a')

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("完成：分隔符已处理")
