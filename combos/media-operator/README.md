# 💼 新媒体运营组合包

> 一句话价值:从选题到发布,把 4 小时的内容流程压到 40 分钟。

## 效果演示

> 待补:1-2 张 WorkBuddy 实测截图 / 15 秒 GIF(真实运行结果),放 `assets/` 下引用。

## 包含内容

- `EXPERT.md`:小红书运营专家(薄角色,负责判断与调度)
- `skills/topic-research/`:选题调研——出本周热点 + 带优先级的选题清单
- `skills/content-decode/`:爆款拆解——逆向同赛道爆款,出可复用模板
- `skills/script-writer/`:脚本生成——出标题/正文/话题标签/封面文案

## 兼容性

| WorkBuddy | QoderWork | Claude |
|---|---|---|
| ✅ 实测通过 | ➖ 未测 | ➖ 未测 |

(实测日期:2026-07-23 · 失效请提 issue)

## 安装

### 方式一:安装咒语(复制粘贴给 WorkBuddy)

````
请帮我导入一个"专家 + 技能"组合包,按下面步骤:

1. 下载这 4 个文件:
   - 专家角色:https://raw.githubusercontent.com/An-idd/expert-skill-combos/main/combos/media-operator/EXPERT.md
   - 技能1 选题调研:https://raw.githubusercontent.com/An-idd/expert-skill-combos/main/combos/media-operator/skills/topic-research/SKILL.md
   - 技能2 爆款拆解:https://raw.githubusercontent.com/An-idd/expert-skill-combos/main/combos/media-operator/skills/content-decode/SKILL.md
   - 技能3 脚本生成:https://raw.githubusercontent.com/An-idd/expert-skill-combos/main/combos/media-operator/skills/script-writer/SKILL.md
2. 把 3 个技能安装到我的 WorkBuddy 技能目录并启用。
3. 把 EXPERT.md 的内容保存为我的自定义角色/专家。
4. 完成后告诉我:装了什么、各自怎么触发、专家会在什么步骤调用哪个技能。

如果你无法访问 GitHub,请告诉我,我会直接把 4 个文件的内容粘贴给你。
````

### 方式二:手动安装

见 [guides/install/workbuddy.md](../../guides/install/workbuddy.md)。

## 使用示例

1. `帮我给平价护肤号做这周的选题` → 专家调用 `topic-research`,出选题清单
2. `把这 5 条爆款拆一下,给我能套的模板` → 专家调用 `content-decode`,出可复用模板
3. `按这个选题和模板写一篇` → 专家调用 `script-writer`,出成稿

## 来源与署名

小红书运营专家由 agency-agents 的 `marketing-xiaohongshu-specialist` 本地化拆分而来(MIT,© AgentLand Contributors)。
