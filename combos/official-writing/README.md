# 💼 公文/材料写作组合包 🚧 待实测

> 一句话价值:领导交办到成稿校对,把写材料的 4 小时压到 40 分钟。

## 包含内容

- `EXPERT.md`:公文材料写作专家(薄角色,负责判断与调度)
- `skills/doc-framework/`:文种判断 + 谋篇提纲(含 wenzhong-library 文种框架库)
- `skills/doc-draft/`:按提纲和素材成稿,合公文语体(含 style-phrases 语体库)
- `skills/doc-polish/`:格式/用语/逻辑/错字校对(含 proofread-checklist)

## 兼容性

| WorkBuddy | QoderWork | Claude |
|---|---|---|
| ➖ 待实测 | ➖ 未测 | ➖ 未测 |

(实测通过后转 ✅、升级为正式 README)

## 安装

### 方式一:安装咒语(复制粘贴给 WorkBuddy)

````
请导入"公文材料写作专家"组合包(3 个技能,均带 references 资料库)。
仓库 raw 根地址:https://raw.githubusercontent.com/An-idd/expert-skill-combos/main/

下载以下文件,保持"技能目录 + references 子目录"结构:
- combos/official-writing/EXPERT.md
- combos/official-writing/skills/doc-framework/SKILL.md
- combos/official-writing/skills/doc-framework/references/wenzhong-library.md
- combos/official-writing/skills/doc-draft/SKILL.md
- combos/official-writing/skills/doc-draft/references/style-phrases.md
- combos/official-writing/skills/doc-polish/SKILL.md
- combos/official-writing/skills/doc-polish/references/proofread-checklist.md

安装要求:
1. 3 个技能装到技能目录并启用,references/ 放各自技能目录下(SKILL.md 会引用它们)。
2. EXPERT.md 存为自定义专家。
3. 完成后告诉我:装了什么、各技能怎么触发、专家调度顺序。

无法访问 GitHub 就告诉我,我把文件内容贴给你。
````

### 方式二:手动安装

见 [guides/install/workbuddy.md](../../guides/install/workbuddy.md)。

## 使用示例

1. `帮我写一份关于开展安全生产检查的通知` → 专家依次调用 doc-framework → doc-draft → doc-polish
2. `这个总结帮我搭个框架` → doc-framework
3. `这份初稿帮我校对格式和用语` → doc-polish

## 来源与署名

基于公文写作工作流调研本地化自建(方法论参考 agency-agents 的 `specialized-document-generator`,MIT,© AgentLand Contributors)。
