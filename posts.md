---
layout: page
title: Posts
---

<style>
  /* 帖子列表卡片化（与首页风格一致） */
  .posts-list {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  .posts-list .post-preview article {
    position: relative;
    padding: 1.3rem 1.4rem;
    border: 1px solid rgba(234, 223, 221, 0.9);
    border-left: 3px solid #d6a5aa;
    border-radius: 14px;
    background: rgba(255, 252, 250, 0.7);
    box-shadow: 0 4px 14px rgba(143, 102, 112, 0.06);
    overflow: hidden;
    transition: border-color 220ms ease, box-shadow 220ms ease, transform 220ms ease;
    margin-bottom: 1rem;
  }
  .posts-list .post-preview article:hover {
    transform: translateY(-3px);
    border-color: rgba(214, 165, 170, 0.5);
    box-shadow: 0 12px 28px rgba(143, 102, 112, 0.13);
  }
  .posts-list .post-preview .post-title {
    font-size: 1.15rem;
    font-weight: 800;
  }
  .posts-list .post-preview .post-title a {
    color: #3d3238;
    text-decoration: none;
  }
  .posts-list .post-preview .post-title a:hover {
    color: #805762;
    text-decoration: none;
  }
  .posts-list .post-preview .post-meta {
    color: #8f6670;
    font-size: 0.8rem;
    font-weight: 600;
  }
  .posts-list .post-preview .post-entry {
    color: #6f666a;
    font-size: 0.92rem;
  }
  .posts-list .post-preview .post-read-more {
    color: #805762;
    text-decoration: underline;
    text-underline-offset: 0.16em;
  }
  .posts-list .post-preview .blog-tags a {
    color: #805762;
  }
</style>

{% assign posts = site.posts %}

<ul class="posts-list" role="list">
  {% for post in posts %}
  <li class="post-preview">
    <article>
      <a href="{{ post.url | absolute_url }}">
        <h2 class="post-title">{{ post.title | strip_html }}</h2>
        {% if post.subtitle %}
          <h3 class="post-subtitle">{{ post.subtitle | strip_html }}</h3>
        {% endif %}
      </a>
      <p class="post-meta">
        {% assign date_format = site.date_format | default: "%B %-d, %Y" %}
        Posted on {{ post.date | date: date_format }}
      </p>
      <div class="post-entry">
        {% assign excerpt_length = site.excerpt_length | default: 50 %}
        {{ post.excerpt | strip_html | truncatewords: excerpt_length }}
        {% assign excerpt_word_count = post.excerpt | number_of_words %}
        {% if post.content != post.excerpt or excerpt_word_count > excerpt_length %}
          <a href="{{ post.url | absolute_url }}" class="post-read-more">[Read&nbsp;More]</a>
        {% endif %}
      </div>
      {% if post.tags.size > 0 %}
      <div class="blog-tags">
        <span>Tags:</span>
        {% for tag in post.tags %}
          <a href="{{ '/tags' | absolute_url }}#{{- tag -}}">{{- tag -}}</a>
        {% endfor %}
      </div>
      {% endif %}
    </article>
  </li>
  {% endfor %}
</ul>
