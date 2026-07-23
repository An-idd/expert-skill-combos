# 💼 电商运营组合包 🚧 待实测

> 一句话价值:从商品优化到达人、直播、大促、私域复购,一套专家 + 技能覆盖 拉新→转化→留存 全链路。

## 包含内容

- `EXPERT.md`:电商运营专家(薄角色,负责判断与调度)
- `skills/listing-optimize/`:商品优化——标题/主图/详情/关键词,分平台(含 platform-notes,抖音全域)
- `skills/campaign-plan/`:大促策划——节奏/机制/预算/备货(含 promo-mechanics)
- `skills/live-script/`:直播脚本——话术/排品/逼单(含 live-flow)
- `skills/data-review/`:经营复盘——GMV/转化/流量结构/ROI
- `skills/influencer-bd/`:达人合作——筛选/谈判/要素材/ROI(含 influencer-checklist)
- `skills/private-domain/`:私域会员——引流承接/RFM 分层/复购(含 retention-playbook)

## 兼容性

| WorkBuddy | QoderWork | Claude |
|---|---|---|
| ➖ 待实测 | ➖ 未测 | ➖ 未测 |

(实测通过后转 ✅、升级为正式 README)

## 安装

### 方式一:安装咒语(复制粘贴给 WorkBuddy)

````
请导入"电商运营专家"组合包(6 个技能,大部分带 references 资料库)。
仓库 raw 根地址:https://raw.githubusercontent.com/An-idd/expert-skill-combos/main/

下载以下文件,保持"技能目录 + references 子目录"结构:
- combos/ecommerce/EXPERT.md
- combos/ecommerce/skills/listing-optimize/SKILL.md
- combos/ecommerce/skills/listing-optimize/references/platform-notes.md
- combos/ecommerce/skills/campaign-plan/SKILL.md
- combos/ecommerce/skills/campaign-plan/references/promo-mechanics.md
- combos/ecommerce/skills/live-script/SKILL.md
- combos/ecommerce/skills/live-script/references/live-flow.md
- combos/ecommerce/skills/data-review/SKILL.md
- combos/ecommerce/skills/influencer-bd/SKILL.md
- combos/ecommerce/skills/influencer-bd/references/influencer-checklist.md
- combos/ecommerce/skills/private-domain/SKILL.md
- combos/ecommerce/skills/private-domain/references/retention-playbook.md

安装要求:
1. 6 个技能装到技能目录并启用,references/ 放各自技能目录下(SKILL.md 会引用它们)。
2. EXPERT.md 存为自定义专家。
3. 完成后告诉我:装了什么、各技能怎么触发、专家调度顺序。

无法访问 GitHub 就告诉我,我把文件内容贴给你。
````

### 方式二:手动安装

见 [guides/install/workbuddy.md](../../guides/install/workbuddy.md)。

## 使用示例

1. `我天猫卖平价护肤,双11 快到了,从选品到大促方案规划一下` → 专家依次调用 listing-optimize → campaign-plan
2. `帮我找达人种草` → influencer-bd
3. `成交客户怎么做私域复购` → private-domain

## 来源与署名

由 agency-agents 的 `marketing-china-ecommerce-operator` / `livestream-commerce-coach` / `private-domain-operator` 本地化拆分(MIT,© AgentLand Contributors)。
