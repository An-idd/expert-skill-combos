# 💼 教师/教学组合包 🚧 待实测

> 一句话价值:备课、命题、做课件,从几小时压到几十分钟。

## 包含内容

- `EXPERT.md`:教师教学专家(薄角色,负责判断与调度)
- `skills/lesson-plan/`:教案——三维目标、重难点、教学环节(含 teaching-design 设计框架)
- `skills/quiz-maker/`:命题——按知识点/难度出题 + 答案解析(含 item-design,布鲁姆认知层次)
- `skills/courseware-outline/`:课件大纲——PPT 结构 + 导向性信息(含 slide-principles)

## 兼容性

| WorkBuddy | QoderWork | Claude |
|---|---|---|
| ➖ 待实测 | ➖ 未测 | ➖ 未测 |

(实测通过后转 ✅、升级为正式 README)

## 安装

### 方式一:安装咒语(复制粘贴给 WorkBuddy)

````
请导入"教师教学专家"组合包(3 个技能,均带 references 资料库)。
仓库 raw 根地址:https://raw.githubusercontent.com/An-idd/expert-skill-combos/main/

下载以下文件,保持"技能目录 + references 子目录"结构:
- combos/teacher/EXPERT.md
- combos/teacher/skills/lesson-plan/SKILL.md
- combos/teacher/skills/lesson-plan/references/teaching-design.md
- combos/teacher/skills/quiz-maker/SKILL.md
- combos/teacher/skills/quiz-maker/references/item-design.md
- combos/teacher/skills/courseware-outline/SKILL.md
- combos/teacher/skills/courseware-outline/references/slide-principles.md

安装要求:
1. 3 个技能装到技能目录并启用,references/ 放各自技能目录下(SKILL.md 会引用它们)。
2. EXPERT.md 存为自定义专家。
3. 完成后告诉我:装了什么、各技能怎么触发、专家调度顺序。

无法访问 GitHub 就告诉我,我把文件内容贴给你。
````

### 方式二:手动安装

见 [guides/install/workbuddy.md](../../guides/install/workbuddy.md)。

## 使用示例

1. `帮我备人教版七年级数学"一元一次方程"这节课` → 专家依次调用 lesson-plan → courseware-outline
2. `按这几个知识点出一份单元测,带答案解析` → quiz-maker
3. `这个教案帮我做成课件大纲` → courseware-outline

## 来源与署名

基于教师备课工作流调研本地化自建(方法论参考 agency-agents 的 `corporate-training-designer` 与 `academic/*`,MIT,© AgentLand Contributors)。
