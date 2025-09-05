---
wiki: notes # 这个跟上面的 /wiki/notes.yml 关联起来
menu_id: notes # 这个跟配置文件中的 `menubar.items.notes` 关联起来，这很重要，如果没有这个，就像普通的wiki项目一样了
---

{% okr o1 %}

2077年的小目标：完成 Volantis 6.0 并发布上线
来自2077年末的复盘：已《基本》实现目标 {% emoji tieba huaji %}

<!-- okr kr1 percent:100 -->
重构 tag-plugins 和 wiki 系统
- 当 {% mark KR %} 进度为 100% 时，标签默认显示为 {% mark color:green 已完成 %}
- 当 {% mark KR %} 未设置进度时，默认为 {% mark 0% %}
- 当 {% mark O %} 未设置进度时，则显示所有 {% mark KR %} 进度平均值

<!-- okr kr2 percent:90 status:off_track -->
完成主要页面设计稿
{% tabs align:left %}
<!-- tab 小提示1 -->
您可以在 _config.yml 文件中修改标签的颜色和文案
<!-- tab 小提示2 -->
您可以在 _config.yml 文件中增加任意的标签配置
{% endtabs %}

<!-- okr kr3 percent:-12 status:unfinished -->
完成前置准备工作（如果你知道答案，请在留言区帮帮我！🥹）
{% checkbox 在咸水和海滩之间找一亩地 %}
{% checkbox 求出圆周率后15位 %}
{% checkbox 找出宇宙的终极逻辑 %}
{% checkbox 去地狱里走两步 %}

<!-- okr kr-4 status:at_risk -->
开发、测试和发布
{% image https://res.xaox.cc/gh/cdn-x/wiki@main/stellar/icon.svg height:64px 支持嵌套插入图片等其它简单组件 ratio:512/512 %}

{% endokr %}
