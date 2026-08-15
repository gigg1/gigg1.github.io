# -*- coding: utf-8 -*-
"""修改 aboutme.md：
1. 四部分研究方向改为 4x1 卡片布局（带边框 + 悬浮光影扫过）
2. publication 卡片粉色调淡
"""
import io

path = "/Users/giggliu/Downloads/PrivateInformation/Website/gigg1.github.io/aboutme.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

# ============ 1. 四部分研究方向 -> 4x1 卡片 ============
old_lines = [
    '* **MLs for Assessing Infectious Disease Risk and Inferring Transmission Patterns:**  ',
    '\t[Malaria Transmission Intensity Assessment (IDM\u201923)](./papers/2023-Assessing-IDM.pdf) \u00b7\u202f[TransCode for COVID\u201119 Transmission Patterns (IDP\u201923)](./papers/2023-TransCode-IDP.pdf)',
    '',
    '* **MLs for Epidemic Dynamics Prediction:**  ',
    '  [Survey on ML for Infectious Disease Risk Prediction (ACM CSUR\u201925)](./papers/2025-Machine-ACMCSUR.pdf)\u202f\u00b7\u202f[EpiDL (CIKM\u201923)](./papers/2023-Epidemiology-aware-CIKM.pdf)',
    '\t',
    '* **MLs & RLs for Infectious Disease Control:**  ',
    '\t[RLs in Infectious Disease Control (WI\u2011IAT\u201925)](./papers/2026-Empowering-WI.pdf) \u00b7\u202f[Resource Allocation for Effective Disease Control (IDP\u201922)](./papers/2022-Optimal-IDP.pdf)',
    '\t',
    '* **MARL for Learning Cooperative Behavior in Multi-agent Systems:**  ',
    '\t[Diametric Coordination Graphs for MARL (AIJ\'26)](https://www.sciencedirect.com/science/article/pii/S0004370226001293)',
    '\t',
]
old_block = "\n".join(old_lines)

new_block = '\n'.join([
    '<div class="research-card">',
    '  <div class="research-card__title">MLs for Assessing Infectious Disease Risk and Inferring Transmission Patterns</div>',
    '  <div class="research-card__links">',
    '    [Malaria Transmission Intensity Assessment (IDM\u201923)](./papers/2023-Assessing-IDM.pdf) \u00b7\u202f[TransCode for COVID\u201119 Transmission Patterns (IDP\u201923)](./papers/2023-TransCode-IDP.pdf)',
    '  </div>',
    '</div>',
    '',
    '<div class="research-card">',
    '  <div class="research-card__title">MLs for Epidemic Dynamics Prediction</div>',
    '  <div class="research-card__links">',
    '    [Survey on ML for Infectious Disease Risk Prediction (ACM CSUR\u201925)](./papers/2025-Machine-ACMCSUR.pdf)\u202f\u00b7\u202f[EpiDL (CIKM\u201923)](./papers/2023-Epidemiology-aware-CIKM.pdf)',
    '  </div>',
    '</div>',
    '',
    '<div class="research-card">',
    '  <div class="research-card__title">MLs &amp; RLs for Infectious Disease Control</div>',
    '  <div class="research-card__links">',
    '    [RLs in Infectious Disease Control (WI\u2011IAT\u201925)](./papers/2026-Empowering-WI.pdf) \u00b7\u202f[Resource Allocation for Effective Disease Control (IDP\u201922)](./papers/2022-Optimal-IDP.pdf)',
    '  </div>',
    '</div>',
    '',
    '<div class="research-card">',
    '  <div class="research-card__title">MARL for Learning Cooperative Behavior in Multi-agent Systems</div>',
    '  <div class="research-card__links">',
    "    [Diametric Coordination Graphs for MARL (AIJ'26)](https://www.sciencedirect.com/science/article/pii/S0004370226001293)",
    '  </div>',
    '</div>',
])

if old_block in content:
    content = content.replace(old_block, new_block, 1)
    print("OK: 四部分卡片替换成功")
else:
    print("WARN: 四部分块未匹配，跳过（文件可能已修改）")

# ============ 2. publication 卡片粉色调淡 ============
old_bg = "background: linear-gradient(135deg, rgba(255, 250, 247, 0.95) 0%, rgba(252, 239, 242, 0.95) 45%, rgba(247, 226, 232, 0.95) 100%);"
new_bg = "background: linear-gradient(135deg, rgba(255, 252, 252, 0.95) 0%, rgba(255, 248, 249, 0.95) 45%, rgba(253, 241, 243, 0.95) 100%);"
if old_bg in content:
    content = content.replace(old_bg, new_bg, 1)
    print("OK: publication 粉色调淡成功")
else:
    print("WARN: publication 背景未匹配")

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("完成")
