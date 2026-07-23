# 💼 学生/科研组合包 🚧 待实测

> 一句话价值:文献到综述,把查找—精读—梳理的时间砍掉一半。

## 包含内容

- `EXPERT.md`:学生科研专家(薄角色,负责判断与调度)
- `skills/lit-search/`:文献检索——检索式 + 核心文献清单(含 search-tips)
- `skills/paper-digest/`:精读摘要——单篇结构化拆解 + 可信度评估(含 appraisal)
- `skills/review-outline/`:综述框架——主题脉络 + 研究缺口(含 review-types,PRISMA)
- `skills/academic-polish/`:学术润色——语言/逻辑/引用规范 + AIGC 风险自查(含 citation-styles、aigc-awareness)

## 兼容性

| WorkBuddy | QoderWork | Claude |
|---|---|---|
| ➖ 待实测 | ➖ 未测 | ➖ 未测 |

(实测通过后转 ✅、升级为正式 README)

## 安装

### 方式一:安装咒语(复制粘贴给 WorkBuddy)

````
请导入"学生科研专家"组合包(4 个技能,均带 references 资料库)。
仓库 raw 根地址:https://raw.githubusercontent.com/An-idd/expert-skill-combos/main/

下载以下文件,保持"技能目录 + references 子目录"结构:
- combos/student-researcher/EXPERT.md
- combos/student-researcher/skills/lit-search/SKILL.md
- combos/student-researcher/skills/lit-search/references/search-tips.md
- combos/student-researcher/skills/paper-digest/SKILL.md
- combos/student-researcher/skills/paper-digest/references/appraisal.md
- combos/student-researcher/skills/review-outline/SKILL.md
- combos/student-researcher/skills/review-outline/references/review-types.md
- combos/student-researcher/skills/academic-polish/SKILL.md
- combos/student-researcher/skills/academic-polish/references/citation-styles.md
- combos/student-researcher/skills/academic-polish/references/aigc-awareness.md

安装要求:
1. 4 个技能装到技能目录并启用,references/ 放各自技能目录下(SKILL.md 会引用它们)。
2. EXPERT.md 存为自定义专家。
3. 完成后告诉我:装了什么、各技能怎么触发、专家调度顺序。

无法访问 GitHub 就告诉我,我把文件内容贴给你。
````

### 方式二:手动安装

见 [guides/install/workbuddy.md](../../guides/install/workbuddy.md)。

## 使用示例

1. `我研究"短视频对青少年注意力的影响",帮我从文献调研到综述框架` → 专家依次调用 lit-search → paper-digest → review-outline
2. `把这篇文献拆一下,给我结构化摘要` → paper-digest
3. `帮我把这段综述润色、查引用规范和 AI 味` → academic-polish

## 来源与署名

研究流程为主,参考 agency-agents 的 `academic/*` 与 `grant-writer`(MIT,© AgentLand Contributors)。
