# 首页备用版本说明

此目录存放**不在站点发布**的备用页面文件，已通过 `_config.yml` 的 `exclude` 排除。

## `index-light.html` — 浅色版首页（2026-09 之前的版本）

星空版首页启用前的原版，白底 + 玫瑰粉配色，含照片封面图 `cover-img: /assets/img/IMG_4538.jpg`。

### 如何切换回浅色版

```bash
# 1. 备份当前星空版（可选）
cp index.html backups/index-starry.html

# 2. 换回浅色版
cp backups/index-light.html index.html

# 3. 重启预览服务器（改的是页面文件，一般会自动重建）
```

### 两版差异对照

| | 浅色版 | 星空版（当前） |
| --- | --- | --- |
| 页面背景 | 白色 `#FFFFFF` | 深色夜空 `#0a0910` |
| 星空背景 | 无 | 有（`assets/css/starry.css`） |
| 欢迎面板 | 白粉渐变实底 | 深色毛玻璃 `rgba(12,11,18,0.62)` |
| 文字颜色 | 黑色 | 粉色 `#f6d9e0` |
| 封面图 | 有（照片） | 无（会遮住星空） |
| front matter | `cover-img: ...` | `body-class: starry` |

### 注意

- 若切换回浅色版，`assets/css/starry.css` 仍会被全局加载（在 `_config.yml` 的 `site-css` 中），
  但因为浅色版没有 `body-class: starry`，星空样式不会生效，无副作用。
- 404 页独立使用星空样式（`body-class: starry page-404`），与本目录无关，切换首页版本不影响它。
