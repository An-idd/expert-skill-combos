# 💼 销售/BD 组合包 🚧 待实测

> 一句话价值:客户开发到方案成交,把 B2B 销售全流程提效。

## 包含内容

- `EXPERT.md`:销售 BD 专家(薄角色,负责判断与调度)
- `skills/lead-outreach/`:客户开发——ICP + 信号驱动 + 触达序列 + 个性化破冰(含 outreach-playbook)
- `skills/needs-discovery/`:需求挖掘——SPIN 提问 + 通话结构(含 spin-guide)
- `skills/proposal-close/`:方案/成交——方案对痛点 + AECR 异议处理 + 跟进逼单(含 deal-tactics)

## 兼容性

| WorkBuddy | QoderWork | Claude |
|---|---|---|
| ➖ 待实测 | ➖ 未测 | ➖ 未测 |

(实测通过后转 ✅、升级为正式 README)

## 安装

### 方式一:安装咒语(复制粘贴给 WorkBuddy)

````
请导入"销售 BD 专家"组合包(3 个技能,均带 references 资料库)。
仓库 raw 根地址:https://raw.githubusercontent.com/An-idd/expert-skill-combos/main/

下载以下文件,保持"技能目录 + references 子目录"结构:
- combos/sales/EXPERT.md
- combos/sales/skills/lead-outreach/SKILL.md
- combos/sales/skills/lead-outreach/references/outreach-playbook.md
- combos/sales/skills/needs-discovery/SKILL.md
- combos/sales/skills/needs-discovery/references/spin-guide.md
- combos/sales/skills/proposal-close/SKILL.md
- combos/sales/skills/proposal-close/references/deal-tactics.md

安装要求:
1. 3 个技能装到技能目录并启用,references/ 放各自技能目录下(SKILL.md 会引用它们)。
2. EXPERT.md 存为自定义专家。
3. 完成后告诉我:装了什么、各技能怎么触发、专家调度顺序。

无法访问 GitHub 就告诉我,我把文件内容贴给你。
````

### 方式二:手动安装

见 [guides/install/workbuddy.md](../../guides/install/workbuddy.md)。

## 使用示例

1. `帮我给这类客户设计一套开发触达序列` → lead-outreach
2. `明天要见客户,帮我设计一套挖需求的提问` → needs-discovery
3. `客户说太贵了,帮我处理这个异议并推进` → proposal-close

## 来源与署名

由 agency-agents 的 `sales-outbound-strategist` / `sales-discovery-coach` / `sales-proposal-strategist` / `sales-deal-strategist` 本地化拆分(MIT,© AgentLand Contributors)。
