# -*- coding: utf-8 -*-
"""给 profile-intro__text 内的段落包裹 <p> 标签"""
import io

path = "/Users/giggliu/Downloads/PrivateInformation/Website/gigg1.github.io/aboutme.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''  <div class="profile-intro__text">

Hello there! I am <strong>Mutong LIU</strong> (刘牧潼), a Ph.D. candidate in the <a href="https://www.comp.hkbu.edu.hk/v1/">Department of Computer Science at Hong Kong Baptist University</a>, supervised by <a href="https://www.comp.hkbu.edu.hk/v1/?page=profile&id=csygliu">Prof. Yang LIU</a> and co-supervised by <a href="https://www.comp.hkbu.edu.hk/v1/?page=profile&id=jiming">Prof. Jiming LIU</a>.
My primary research interests inlcudes <strong>artificial intelligence, machine learning, computational epidemiology, and complex system modeling</strong>, specifically focus on developing multi-agent reinforcement learning, physical/epidemiological-informed machine learning, and spatiotemporal analysis methods.
<!--I also maintain a broad interest in methodology development of multi-agent RL and spatiotemporal analytics.-->
<!--developing and leveraging methodology in machine learning (ML) and reinforcement learning (RL) combined with epidemiological modeling to assess, predict, and control infectious diseases risk. I also maintain a broad interest in methodology development of multi-agent RL and spatiotemporal analytics.-->

<!--I believe that data-driven, spatiotemporally aware methods are key to building resilient public health systems.-->
My work aims to solve complex real-world problems such as infectious disease transmission risk assessment and prediction, adaptive intervention strategy inference, and effective cooperative behavior learning in multi-agent systems.
My research spans AI/ML methodology development and application deployment in the context of infectious disease dynamics:

  </div>'''

new = '''  <div class="profile-intro__text">

<p>Hello there! I am <strong>Mutong LIU</strong> (刘牧潼), a Ph.D. candidate in the <a href="https://www.comp.hkbu.edu.hk/v1/">Department of Computer Science at Hong Kong Baptist University</a>, supervised by <a href="https://www.comp.hkbu.edu.hk/v1/?page=profile&id=csygliu">Prof. Yang LIU</a> and co-supervised by <a href="https://www.comp.hkbu.edu.hk/v1/?page=profile&id=jiming">Prof. Jiming LIU</a>.</p>
<p>My primary research interests inlcudes <strong>artificial intelligence, machine learning, computational epidemiology, and complex system modeling</strong>, specifically focus on developing multi-agent reinforcement learning, physical/epidemiological-informed machine learning, and spatiotemporal analysis methods.</p>
<!--I also maintain a broad interest in methodology development of multi-agent RL and spatiotemporal analytics.-->
<!--developing and leveraging methodology in machine learning (ML) and reinforcement learning (RL) combined with epidemiological modeling to assess, predict, and control infectious diseases risk. I also maintain a broad interest in methodology development of multi-agent RL and spatiotemporal analytics.-->

<!--I believe that data-driven, spatiotemporally aware methods are key to building resilient public health systems.-->
<p>My work aims to solve complex real-world problems such as infectious disease transmission risk assessment and prediction, adaptive intervention strategy inference, and effective cooperative behavior learning in multi-agent systems.</p>
<p>My research spans AI/ML methodology development and application deployment in the context of infectious disease dynamics:</p>

  </div>'''

if old in content:
    content = content.replace(old, new, 1)
    print("OK: 段落已包裹 <p> 标签")
else:
    print("WARN: 未匹配到目标块")

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("完成")
