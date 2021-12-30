# 说明

**我当前使用的**

书源：
`https://yun.bizha.top/d/Personal/BookSource/shareBookSource.json`

![](https://cdn.jsdelivr.net/gh/yoval/TuChuang@main/16391173781841639117378181.png)

替换源：

`https://yun.bizha.top/Personal/BookSource/replaceRule.json`

![](https://cdn.jsdelivr.net/gh/yoval/TuChuang@main/16391172548501639117254845.png)


日志

- 关闭大部分书源的`发现`。

- 将八一中文(81zwapp.com)置顶，以获得`更新日期`。

- 将起点、优书网置顶，以获得`最新章节`名称。

**代码**

阅读APP导出书源处理。

- 删除失效网站

- 删除响应时间>15s的网站

- 删除网站标题含关键词的网站。

删除标题：

['BadRequest','503','login','Attention','Error','404','Apache','Cloudflare','baidu','公益','提示','漫画','升级','安全','200','Apache','Found','Spring']