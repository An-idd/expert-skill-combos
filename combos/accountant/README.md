# 💼 财务组合包 🚧 待实测

> 一句话价值:把重复的账务整理、对账、结账、报表交给专家 + 技能协作。

> ⚠️ 财务是高风险域:所有技能都不做假账,税率/科目以最新会计准则和税法为准,复杂业务提示找持证会计师/税务师。

## 包含内容

- `EXPERT.md`:财务记账专家(薄角色,负责判断与调度)
- `skills/bookkeeping/`:记账做账——科目/分录/凭证 + 数电票规范 + 小微优惠(含 common-entries、invoice-tax-2026)
- `skills/reconcile/`:对账——银行/往来/科目余额对账查差异(含 reconcile-checklist)
- `skills/month-close/`:月末结账——计提/结转/试算平衡(含 close-checklist)
- `skills/statement-report/`:报表编制——资产负债表/利润表 + 勾稽校验(含 statement-notes)

## 兼容性

| WorkBuddy | QoderWork | Claude |
|---|---|---|
| ➖ 待实测 | ➖ 未测 | ➖ 未测 |

(实测通过后转 ✅、升级为正式 README)

## 安装

### 方式一:安装咒语(复制粘贴给 WorkBuddy)

````
请导入"财务记账专家"组合包(4 个技能,均带 references 资料库)。
仓库 raw 根地址:https://raw.githubusercontent.com/An-idd/expert-skill-combos/main/

下载以下文件,保持"技能目录 + references 子目录"结构:
- combos/accountant/EXPERT.md
- combos/accountant/skills/bookkeeping/SKILL.md
- combos/accountant/skills/bookkeeping/references/common-entries.md
- combos/accountant/skills/bookkeeping/references/invoice-tax-2026.md
- combos/accountant/skills/reconcile/SKILL.md
- combos/accountant/skills/reconcile/references/reconcile-checklist.md
- combos/accountant/skills/month-close/SKILL.md
- combos/accountant/skills/month-close/references/close-checklist.md
- combos/accountant/skills/statement-report/SKILL.md
- combos/accountant/skills/statement-report/references/statement-notes.md

安装要求:
1. 4 个技能装到技能目录并启用,references/ 放各自技能目录下(SKILL.md 会引用它们)。
2. EXPERT.md 存为自定义专家。
3. 完成后告诉我:装了什么、各技能怎么触发、专家调度顺序。

无法访问 GitHub 就告诉我,我把文件内容贴给你。
````

### 方式二:手动安装

见 [guides/install/workbuddy.md](../../guides/install/workbuddy.md)。

## 使用示例

1. `这个月这几笔业务(进货/卖货/房租/工资)帮我做账并出月末报表` → 专家依次调用 bookkeeping → reconcile → month-close → statement-report
2. `帮我对一下银行和往来的账` → reconcile
3. `帮我走一遍月末结账` → month-close

## 来源与署名

由 agency-agents 的 `finance-bookkeeper-controller` 本地化到中小企业账务场景(MIT,© AgentLand Contributors)。
