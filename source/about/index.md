---
robots: 'index,nofollow'
menu_id: social
title: 关于
h1: ''
leftbar: [sociallist, welcome, recent]
comment_title: 来过，就留下您的脚印吧～
logo:
  subtitle: 来过，就留下您的脚印吧～
giscus:
  data-mapping: pathname
  data-term: 0
comments: true
breadcrumb: false
header: false
indent: true
---

{% banner richfan 简介 bg:https://jsd.cdn.zzko.cn/gh/richbridge/picx-images-hosting@master/logo/bg.avif avatar:https://jsd.cdn.zzko.cn/gh/richbridge/picx-images-hosting@master/logo/avatar.avif %}
{% navbar active:/about/ [友链](/friends/) [关于](/about/) %}
{% endbanner %}

<br>

{% quot icon:hashtag 关于本站 %}

本站没有任何推广和打赏链接，如果您觉得哪个作品不错，欢迎去对应的仓库点个赞，或者在对应的文章下面留言互动一下。

开源项目无任何盈利目的，只在工作闲暇时间进行维护，有相关需求请前往对应项目提 Issue 进行反馈，通过私人邮件询问开源项目问题可能得不到答复。

## 关于博客

博客的搭建和维护学了许多花里胡哨的东西😂，主要用来写写自己想写的东西（虽然现在大多是技术文章），emmm。。。有些话想到再说。

{% timeline %}

<!-- node 2018-09-19 博客诞生 -->
- 1、其实具体日子我也不记得了，当初不熟悉 Git，Commit History 被我摧毁了很多次，难以追溯具体日期🤣🤦‍♂️
- 2、基于 [Hexo](https://hexo.io/zh-cn/docs/index.html) 搭建的静态博客，最初使用的博客主题为 [yilia](https://github.com/litten/hexo-theme-yilia)，使用 [Github Pages](https://help.github.com/cn#github-pages-basics) 托管
- 3、也曾玩过 [WordPress](https://wordpress.org/support/)、[Typecho](https://github.com/typecho/typecho)（曾剁手买了个主题-[handsome](https://www.ihewro.com/archives/489/)）
- 4、现在博客使用的 Hexo 博客主题是 [xaoxuxu](https://xaoxuu.com/blog/) 大佬写的 [volantis](https://github.com/volantis-x/hexo-theme-volantis/tree/4.3.1)，曾经叫 Material-x 就开始用了

<!-- node 2018-09-29 注册顶级域名 -->
人生第一个个人域名，[shansan.top](https://shansan.top)，走 CNAME 解析到 GitHub Pages。

<!-- node 2018-12-24 启用备用域名 shan333.cn -->
将博客 [shan333.cn](https://shan333.cn) 部署到腾讯云 CVM 服务器；Web 服务器使用到了 Nginx；使用宝塔面板进行 Ops；通过 Linux 定时任务同步博客到云服务器

<!-- node 2020-01-30 引入 GitHub Actions -->
使用 [GitHub Actions](https://github.com/features/actions) 持续集成/部署 Hexo 博客到 GitHub Pages [“workflow.yml🔗”](https://github.com/yeshan333/actions-for-hexo-blog/blob/main/.github/workflows/hexo-ci.yaml)，放弃云盘单独备份，使用 Git 做版本控制（回忆）

<!-- node 2020-03-11 Hexo 主题升级 -->
主题升级至[volantis@2.0.2](https://volantis.js.org/)(原material-x主题改名了)，紧跟dalao更新步伐

<!-- node 2020-04-29 volantis@2.0.2 -> volantis@2.6.5 -->
紧跟主题更新节奏

<!-- node 2021-01-18 云服务器博客同步引入 CI/CD -->
写了个基于 rsync 协议的 GitHub Action 用于 CD 博客到 CVM 服务器，博文👉[使用 rsync-deploy-action 同步 Hexo 博客到个人服务器](https://shan333.cn/2021/01/19/hexo-blog-synchronization-with-rsync/)

<!-- node 2021-03-10 volantis@2.6.5 -> volantis@4.3.1，hexo@4.0.0 -> hexo@5.4.0 -->
紧跟主题更新节奏，用上新特性

<!-- node 2021-06-25 切换评论系统 valine -> waline -->
valine 暴出 BUG 了，囧~

<!-- node 2022-05-08 waline 升级 -->
评论系统升级~

<!-- node 2022-11-05 volantis -> v5.7.6 升级, 切换自建评论系统: [artalk](https://artalk.js.org/) -->
还是自建香，Go 写的。

<!-- node 2024-02-06 hexo -> v7.0.0 升级 -->
紧跟 Hexo 更新节奏。

<!-- node 2024-03-14 volantis -> v2.6.3 升级 v2.8.3~ -->
API 不兼容，吐了🤮，升级还是蛮难受的。

<!-- node 2024-07-23 volantis -> v2.8.3 升级 v2.8.7 -->
紧跟节奏，避免升级困难。

<!-- node 2025-07-26 博客主题由 volantis 转换为 Stellar，感谢 Claude Code 帮忙迁移 -->
更加简洁~作者是同一个人。

{% endtimeline %}

博客加入了十年之约项目嗷~相信时间的力量。

[![十年之约](https://img.foreverblog.cn/logo_en_default.png)](https://www.foreverblog.cn/about.html)

![在下真名](https://s2.ax1x.com/2019/07/02/ZJ7KAO.gif)