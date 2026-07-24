# 💼 职场办公助手组合包 🚧 待实测

> 一句话价值:会议纪要、周报汇报、职场邮件,把白领日常文书从小时级压到分钟级。

## 包含内容

- `EXPERT.md`:职场办公助手(薄角色,负责判断与调度)
- `skills/meeting-notes/`:会议纪要——转写/草记 → 结论 + 待办清单(含 notes-rules)
- `skills/report-writer/`:周报/汇报——结论先行、成效量化(含 report-structures)
- `skills/email-writer/`:职场邮件——分场景、主题直给、明确行动(含 email-scenarios)

## 兼容性

| WorkBuddy | QoderWork | Claude |
|---|---|---|
| ➖ 待实测 | ➖ 未测 | ➖ 未测 |

(实测通过后转 ✅、升级为正式 README)

## 安装

### 方式一:安装咒语(复制粘贴给 WorkBuddy)

````
请导入"职场办公助手"组合包(3 个技能,均带 references 资料库)。
仓库 raw 根地址:https://raw.githubusercontent.com/An-idd/expert-skill-combos/main/

下载以下文件,保持"技能目录 + references 子目录"结构:
- combos/office-assistant/EXPERT.md
- combos/office-assistant/skills/meeting-notes/SKILL.md
- combos/office-assistant/skills/meeting-notes/references/notes-rules.md
- combos/office-assistant/skills/report-writer/SKILL.md
- combos/office-assistant/skills/report-writer/references/report-structures.md
- combos/office-assistant/skills/email-writer/SKILL.md
- combos/office-assistant/skills/email-writer/references/email-scenarios.md

安装要求:
1. 3 个技能装到技能目录并启用,references/ 放各自技能目录下(SKILL.md 会引用它们)。
2. EXPERT.md 存为自定义专家。
3. 完成后告诉我:装了什么、各技能怎么触发、专家调度顺序。

无法访问 GitHub 就告诉我,我把文件内容贴给你。
````

### 方式二:手动安装

见 [guides/install/workbuddy.md](../../guides/install/workbuddy.md)。

## 使用示例

1. `这段会议录音转写帮我整理成纪要` → meeting-notes 出结论 + 待办
2. `把我这周做的这些事写成周报` → report-writer
3. `帮我写封邮件跟供应商催一下报价` → email-writer

## 来源与署名

由 agency-agents 的 `meeting-notes-specialist` / `executive-summary-generator` / `email-strategist` 本地化拆分(MIT,© AgentLand Contributors)。
