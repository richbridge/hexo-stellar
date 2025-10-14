---
notebook: hello-world # 这是项目id，对应 /_data/notebooks/first notes.yml
menu_id: notes 
title: Hello World
subtitle: I'm coming!
tags: ["建站"]
---

<img src="./images/lunyu.jpg">

## 引入主题及组件
```git
git submodule add https://github.com/hugo-fixit/FixIt.git themes/FixIt
git submodule add https://github.com/hugo-fixit/cmpt-translate.git themes/cmpt-translate
git submodule add https://github.com/hugo-fixit/component-projects.git themes/component-projects
git submodule add https://github.com/hugo-fixit/hugo-json-feed.git themes/hugo-json-feed
git submodule add https://github.com/hugo-fixit/shortcode-mmt-netease.git themes/shortcode-mmt-netease
git submodule add https://github.com/hugo-fixit/cmpt-flyfish.git themes/cmpt-flyfish
git submodule add https://github.com/hugo-fixit/shortcode-rewards.git themes/shortcode-rewards
git submodule add https://github.com/hugo-fixit/shortcode-caniuse.git themes/shortcode-caniuse
git submodule add https://github.com/hugo-fixit/hugo-atom-feed.git themes/hugo-atom-feed
git submodule add https://github.com/hugo-fixit/cmpt-mdevtools.git themes/cmpt-mdevtools
git submodule add https://github.com/hugo-fixit/shortcode-asciinema.git themes/shortcode-asciinema
git submodule add https://github.com/hugo-fixit/shortcode-docs-bookmark.git themes/shortcode-docs-bookmark
git submodule add https://github.com/hugo-fixit/shortcode-missing-translation.git themes/shortcode-missing-translation
git submodule add https://github.com/hugo-fixit/shortcode-sponsor-log.git themes/shortcode-sponsor-log
```

## 应用主题
```toml
theme = ["FixIt", "cmpt-translate", "component-projects", "hugo-json-feed", "shortcode-mmt-netease", "cmpt-flyfish", "shortcode-rewards", "shortcode-caniuse", "hugo-atom-feed", "cmpt-mdevtools", "shortcode-asciinema", "shortcode-docs-bookmark", "shortcode-missing-translation", "shortcode-sponsor-log"]
```

## 复制静态文件
```toml
data && assets && static
```

## 更新主体
```git
git submodule update --remote --merge themes/anzhiyu
```


## 备用代码

### 添加子主题

#### solitude

```git
git submodule add -b dev https://github.com/everfu/hexo-theme-solitude.git themes/solitude
git submodule add https://github.com/richbridge/posts.git source/_posts
```

#### anzhiyu

```git
git submodule add -b dev https://github.com/anzhiyu-c/hexo-theme-anzhiyu.git themes/anzhiyu
git submodule add https://github.com/richbridge/posts.git source/_posts
```

#### fixit

```git
git submodule add https://github.com/hugo-fixit/FixIt.git themes/FixIt
git submodule add https://github.com/hugo-fixit/cmpt-translate.git themes/cmpt-translate
git submodule add https://github.com/hugo-fixit/component-projects.git themes/component-projects
git submodule add https://github.com/hugo-fixit/hugo-json-feed.git themes/hugo-json-feed
git submodule add https://github.com/hugo-fixit/shortcode-mmt-netease.git themes/shortcode-mmt-netease
git submodule add https://github.com/hugo-fixit/cmpt-flyfish.git themes/cmpt-flyfish
git submodule add https://github.com/hugo-fixit/shortcode-rewards.git themes/shortcode-rewards
git submodule add https://github.com/hugo-fixit/shortcode-caniuse.git themes/shortcode-caniuse
git submodule add https://github.com/hugo-fixit/hugo-atom-feed.git themes/hugo-atom-feed
git submodule add https://github.com/hugo-fixit/cmpt-mdevtools.git themes/cmpt-mdevtools
git submodule add https://github.com/hugo-fixit/shortcode-asciinema.git themes/shortcode-asciinema
git submodule add https://github.com/hugo-fixit/shortcode-docs-bookmark.git themes/shortcode-docs-bookmark
git submodule add https://github.com/hugo-fixit/shortcode-missing-translation.git themes/shortcode-missing-translation
git submodule add https://github.com/hugo-fixit/shortcode-sponsor-log.git themes/shortcode-sponsor-log
git submodule add https://github.com/richbridge/posts.git content/posts
```

### 更新子主题

#### solitude

```git
git submodule update --remote --merge source/_posts
git submodule update --remote --merge themes/AstraBay
git submodule update --remote --merge themes/solitude
```

#### anzhiyu

```git
git submodule update --remote --merge source/_posts
git submodule update --remote --merge themes/anzhiyu
```

#### fixit

```git
git submodule update --remote --merge content/posts
git submodule update --remote --merge themes/FixIt
```

## 添加多个仓库

git remote set-url --add origin https://github.com/richbridge/posts.git