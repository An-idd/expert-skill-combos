# 💼 求职·简历面试组合包

> 一句话价值:一份 JD,把简历改到岗位匹配,再把面试题备到能应对追问。

## 效果演示

WorkBuddy 实测通过(2026-07-23):完整跑通 `jd-decode → resume-tailor → interview-prep` 三段链路——拆解岗位、定制简历(缺数字主动问、不编造,还揪出简历里年龄与入学时间线的矛盾)、生成面试题。
👉 [查看完整实测过程](https://codebuddy.work/agents/tasks/share/8B6wxPKxmI?platform=workbuddy)

## 包含内容

- `EXPERT.md`:求职简历面试专家(薄角色,负责判断与调度)
- `skills/jd-decode/`:岗位拆解——分出必须项/加分项/隐藏评估点 + ATS 关键词(含 references/jd-signals)
- `skills/resume-tailor/`:简历定制——证据前置、责任句改成果句、对齐 2026 ATS,诚实标缺口(含 references/ats-rules)
- `skills/interview-prep/`:面试准备——高频题 + STAR 框架 + 追问应对(含 references/star-questions)

## 兼容性

| WorkBuddy | QoderWork | Claude |
|---|---|---|
| ✅ 实测通过 | ➖ 未测 | ➖ 未测 |

(实测日期:2026-07-23 · 失效请提 issue)

## 安装

### 方式一:安装咒语(复制粘贴给 WorkBuddy)

````
请导入"求职简历面试专家"组合包(3 个技能,均带 references 资料库)。
仓库 raw 根地址:https://raw.githubusercontent.com/An-idd/expert-skill-combos/main/

下载以下文件,保持"技能目录 + references 子目录"结构:
- combos/job-seeker/EXPERT.md
- combos/job-seeker/skills/jd-decode/SKILL.md
- combos/job-seeker/skills/jd-decode/references/jd-signals.md
- combos/job-seeker/skills/resume-tailor/SKILL.md
- combos/job-seeker/skills/resume-tailor/references/ats-rules.md
- combos/job-seeker/skills/interview-prep/SKILL.md
- combos/job-seeker/skills/interview-prep/references/star-questions.md

安装要求:
1. 3 个技能装到技能目录并启用,references/ 放各自技能目录下(SKILL.md 会引用它们)。
2. EXPERT.md 存为自定义专家。
3. 完成后告诉我:装了什么、各技能怎么触发、专家调度顺序。

无法访问 GitHub 就告诉我,我把文件内容贴给你。
````

### 方式二:手动安装

见 [guides/install/workbuddy.md](../../guides/install/workbuddy.md)。

## 使用示例

1. `我要投这个岗位,帮我准备。JD:[...]。我的简历:[...]` → 专家依次调用 jd-decode → resume-tailor → interview-prep
2. `按这份 JD 拆一下真正要什么` → jd-decode 出必须项/加分项/隐藏点
3. `简历 OK 了,帮我准备面试题` → interview-prep 出题 + STAR 框架

## 来源与署名

求职简历面试专家由 agency-agents 的 `resume-tailor` + `recruitment-specialist` 本地化拆分而来(MIT,© AgentLand Contributors)。
