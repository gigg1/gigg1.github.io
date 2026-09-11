# 本地预览指南（Local Preview）

本文档说明如何在本地启动本网站的预览服务器。

---

## 1. 环境要求

| 依赖 | 版本 | 说明 |
| --- | --- | --- |
| Ruby | 3.x / 4.x | 需包含 `ruby` 命令 |
| Jekyll | 3.9.3 | **已随仓库自带**，无需单独安装 |

> 本项目的所有 Ruby gem 都已经解包放在 `vendor/gems/` 目录中，
> **不需要**执行 `bundle install`，也不需要联网下载依赖。

检查环境：

```bash
ruby -v
```

---

## 2. 一键启动

在项目根目录（即包含 `_config.yml` 的目录）执行：

```bash
cd /Users/giggliu/Downloads/PrivateInformation/Website/gigg1.github.io

GEM_HOME="$PWD/vendor/gems" \
GEM_PATH="$PWD/vendor/gems" \
JEKYLL_NO_BUNDLER_REQUIRE=true \
ruby vendor/gems/bin/jekyll serve --host 127.0.0.1 --port 4000 --livereload
```

启动成功后会看到：

```
Server address: http://127.0.0.1:4000
Server running... press ctrl-c to stop.
```

然后在浏览器打开：**<http://127.0.0.1:4000>**

---

## 3. 三个环境变量的作用（重要）

| 变量 | 作用 |
| --- | --- |
| `GEM_HOME` | 告诉 Ruby 从仓库内的 `vendor/gems` 加载 gem |
| `GEM_PATH` | 同上，确保查找路径包含本地 gem 目录 |
| `JEKYLL_NO_BUNDLER_REQUIRE` | **必须设置**。跳过 Jekyll 调用 `Bundler.setup`，避免报 `Could not find gem 'rake (~> 12.0)'` 之类的错误 |

如果不设置 `JEKYLL_NO_BUNDLER_REQUIRE=true`，会因为没有 `Gemfile.lock`（已被 `.gitignore` 忽略）而尝试联网解析依赖并失败。

---

## 4. 常用命令

```bash
# 启动并自动重新构建 + 浏览器自动刷新
... jekyll serve --livereload

# 只启动服务器，不自动刷新
... jekyll serve

# 换端口（4000 被占用时）
... jekyll serve --port 4001

# 允许局域网其他设备访问
... jekyll serve --host 0.0.0.0

# 只构建静态文件到 _site/，不启动服务器
... jekyll build

# 查看环境诊断信息
... jekyll doctor
```

### 停止服务器

在运行服务器的终端中按 `Ctrl + C`。

### 增量构建（大站点提速）

```bash
... jekyll serve --incremental
```

---

## 5. 内容修改与自动刷新

- 服务器运行期间，修改 `*.md`、`_layouts/`、`_includes/`、`assets/` 等文件会**自动重新构建**。
- 使用 `--livereload` 时，浏览器会自动刷新页面。
- 修改 `_config.yml` 后**必须重启**服务器才生效。

---

## 6. 常见问题

### 报错 `Could not find gem 'rake (~> 12.0)' in locally installed gems`

原因：没有设置 `JEKYLL_NO_BUNDLER_REQUIRE=true`。
解决：按上面第 2 节的完整命令重新执行。

### 报错 `Address already in use - bind(2) for 127.0.0.1:4000`

原因是 4000 端口被占用。查找并结束占用进程：

```bash
lsof -i :4000
kill <PID>
```

或直接换端口：`--port 4001`。

### 端口 35729 被占用（LiveReload）

关闭 `--livereload` 参数，或结束占用该端口的进程：

```bash
lsof -i :35729
```

### 页面样式/脚本没有更新

浏览器缓存导致。请硬刷新：

- macOS：`Cmd + Shift + R`

### 想用 VS Code 一键启动

可以在 VS Code 中新建任务（`Terminal → Run Task`），命令沿用第 2 节的完整命令即可。

---

## 7. 部署说明（参考）

本地预览确认无误后，提交并推送到 GitHub 即可，GitHub Pages 会自动构建发布：

```bash
git add -A
git commit -m "Update site"
git push
```

> 注意：`_site/` 是本地构建产物，已在 `.gitignore` 中忽略，无需提交。
