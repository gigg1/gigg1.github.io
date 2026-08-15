# -*- coding: utf-8 -*-
"""把 research-card 里的相对路径 ./papers/ 改成根路径 /papers/"""
import io

path = "/Users/giggliu/Downloads/PrivateInformation/Website/gigg1.github.io/aboutme.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 只替换 research-card 内 href="./papers/ 为 href="/papers/
content = content.replace('href="./papers/', 'href="/papers/')

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("完成：papers 链接已改为根路径")
