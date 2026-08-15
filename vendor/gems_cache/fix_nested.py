# -*- coding: utf-8 -*-
"""修复 aboutme.md 中 research-card__links 的嵌套重复 div"""
import io
import re

path = "/Users/giggliu/Downloads/PrivateInformation/Website/gigg1.github.io/aboutme.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 移除重复嵌套的 <div class="research-card__links"> 结构
# 当前坏结构：
#   <div class="research-card__links">
#     <div class="research-card__links">
#     <a ...>...</a>
#   </div>
#   </div>
# 修复为：
#   <div class="research-card__links">
#     <a ...>...</a>
#   </div>

# 方案：直接移除每个内层重复的 <div class="research-card__links"> 和多余的 </div>
# 用精确的字符串替换处理

def fix_block(m):
    inner = m.group(1)
    # 去掉内层开头重复的 div 标签
    inner = re.sub(r'^\s*<div class="research-card__links">\s*', '', inner)
    # 去掉内层结尾多余的 </div>（保留一个作为外层闭合）
    inner = re.sub(r'\s*</div>\s*$', '', inner)
    return '<div class="research-card__links">\n' + inner + '\n  </div>'

# 匹配整个 links div（含嵌套）
pattern = r'<div class="research-card__links">(.*?)</div>\s*</div>'
new_content = re.sub(pattern, fix_block, content, flags=re.DOTALL)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(new_content)

# 验证是否还有嵌套
with io.open(path, "r", encoding="utf-8") as f:
    check = f.read()
nested = check.count('<div class="research-card__links">')
print("research-card__links 标签出现次数:", nested)
print("期望: 4 (每个卡片一个)")
