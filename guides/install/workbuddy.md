# WorkBuddy 安装指南

## 方式一：安装咒语（推荐）

把下面这段复制给你的 WorkBuddy Agent（`<owner>/<repo>`、`<combo>` 换成实际值）：

```
请帮我安装一个技能组合包：
1. 从 https://raw.githubusercontent.com/<owner>/<repo>/main/combos/<combo>/
   下载 EXPERT.md 和 skills/ 目录下的所有技能
2. 将技能安装到我的 WorkBuddy 技能目录并在配置中启用
3. 将 EXPERT.md 的内容保存为我的自定义角色备用
4. 完成后告诉我：装了什么、怎么触发使用
如果网络无法访问 GitHub，请告诉我，我会提供文件内容。
```

## 方式二：手动安装

1. WorkBuddy 技能目录路径：`<TODO：填实测路径>`
2. 把 `combos/<combo>/skills/` 下每个技能目录拷进去。
3. 在 `settings.json` 中启用：`<TODO：填实测字段>`
4. 把 `EXPERT.md` 内容保存为自定义角色。

## 实测记录

> 每套咒语发布前实测 ≥5 次，记录成功率与失败场景。

| 日期 | 咒语版本 | 成功/次数 | 失败场景 |
|---|---|---|---|
| 2026-0x-xx | v1 | x/5 | — |
