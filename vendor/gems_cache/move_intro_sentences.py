# -*- coding: utf-8 -*-
"""把两句话移出左右布局，合并成一段放在 research-grid 前"""
import io

path = "/Users/giggliu/Downloads/PrivateInformation/Website/gigg1.github.io/aboutme.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. 从 profile-intro__text 中删除那两句话
old_inside = '''<!--I believe that data-driven, spatiotemporally aware methods are key to building resilient public health systems.-->
<p>My work aims to solve complex real-world problems such as infectious disease transmission risk assessment and prediction, adaptive intervention strategy inference, and effective cooperative behavior learning in multi-agent systems.</p>
<p>My research spans AI/ML methodology development and application deployment in the context of infectious disease dynamics:</p>

  </div>
</div>

<div class="research-grid">'''

new_inside = '''<!--I believe that data-driven, spatiotemporally aware methods are key to building resilient public health systems.-->
  </div>
</div>

My work aims to solve complex real-world problems such as infectious disease transmission risk assessment and prediction, adaptive intervention strategy inference, and effective cooperative behavior learning in multi-agent systems. My research spans AI/ML methodology development and application deployment in the context of infectious disease dynamics:

<div class="research-grid">'''

if old_inside in content:
    content = content.replace(old_inside, new_inside, 1)
    print("OK: 两句话已移出并合并")
else:
    print("WARN: 未匹配到目标块")

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("完成")
