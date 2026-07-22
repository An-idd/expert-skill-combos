# Claude 安装指南

## 方式一：安装咒语（推荐）

复制给你的 Claude（Claude Code / 桌面端 Skill）（`<owner>/<repo>`、`<combo>` 换成实际值）：

```
请帮我安装一个技能组合包：
1. 从 https://raw.githubusercontent.com/<owner>/<repo>/main/combos/<combo>/
   下载 EXPERT.md 和 skills/ 目录下的所有技能
2. 将每个 skill 放到我的 Claude skills 目录并启用
3. 将 EXPERT.md 的内容保存为我的自定义角色 / CLAUDE.md 片段备用
4. 完成后告诉我：装了什么、怎么触发使用
如果网络无法访问 GitHub，请告诉我，我会提供文件内容。
```

## 方式二：手动安装

1. Claude skills 目录：`~/.claude/skills/`（Claude Code）或 `<TODO：桌面端路径>`
2. 把每个技能目录拷进去，确保含 `SKILL.md`。
3. `EXPERT.md` 内容可存为项目 `CLAUDE.md` 片段或自定义角色。

## 实测记录

| 日期 | 咒语版本 | 成功/次数 | 失败场景 |
|---|---|---|---|
| 2026-0x-xx | v1 | x/5 | — |
