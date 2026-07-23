# 🧩 专家 × Skill 组合包

> 别再零散装技能了。一个岗位，一套打包：**专家角色怎么想 + 技能怎么干**。
> 每个组合包都在 WorkBuddy / QoderWork / Claude 实测通过。
>
> 🚧 持续更新中,每周新增组合包。

<!-- 替换 <owner>/<repo> 后启用 star 徽章 -->
[![Stars](https://img.shields.io/github/stars/%3Cowner%3E/%3Crepo%3E?style=social)](https://github.com/%3Cowner%3E/%3Crepo%3E)

[快速开始](#怎么安装三选一) · [按岗位找组合包](#组合包目录) · [兼容矩阵](compat/matrix.md) · [English](README_EN.md)

---

## 30 秒理解这个项目

- **专家（EXPERT.md）** = 角色 prompt：定义"一个 5 年经验的岗位老手会怎么想、按什么顺序拆问题"。
- **Skill** = 执行能力：专家在某一步真正调用来干活的工具（选题调研、爆款拆解……）。
- **组合包（combo）** = 开箱即用的整套：1 个专家 + 2~4 个配套技能，专家里显式写明"何时调用哪个技能"。

零散装技能像给你一堆零件；组合包是装好的整机。

## 组合包目录

| 岗位 | 组合包 | 包含 | 兼容 | 视频演示 |
|---|---|---|---|---|
| 新媒体运营 | [media-operator](combos/media-operator) | 1 专家 + 4 技能 | ✅ WorkBuddy | — |
| 求职·简历面试 | [job-seeker](combos/job-seeker) | 1 专家 + 3 技能 | ✅ WorkBuddy | — |
| 学生/科研 | [student-researcher](combos/student-researcher) | 1 专家 + 2~4 技能 | 🚧 | — |
| 电商运营 | [ecommerce](combos/ecommerce) | 1 专家 + 2~4 技能 | 🚧 | — |
| 财务 | [accountant](combos/accountant) | 1 专家 + 2~4 技能 | 🚧 | — |

图例：✅ 已实测发布 · 🚧 建设中（结构已就位，内容实测后上线）

> 质量红线：**没实测过的东西不上仓库。** 标 🚧 的组合包只有骨架，内容会在实测通过后填入。

## 怎么安装（三选一）

1. **复制安装咒语**（推荐）：见各组合包 README 的"安装咒语"段，粘贴给你的 Agent 即可。
2. **手动安装**：见 [guides/install/](guides/install/)（WorkBuddy / QoderWork / Claude 各一份）。
3. **开发者**：`git clone` 后按对应工具目录放置组件。

## 想为一个岗位设计组合包？

- 概念：[专家和 Skill 到底什么关系](guides/expert-vs-skill.md)
- 方法论：[怎么为一个岗位设计组合包](guides/how-to-combo.md)
- 贡献：复制 [`combos/_template`](combos/_template) → 按规范填写 → 提 PR，见 [CONTRIBUTING.md](CONTRIBUTING.md)

## 许可

代码与结构 MIT；prompt 与文档内容 CC-BY-4.0（可转载，须署名）。见 [LICENSE](LICENSE)。

<!-- 私域入口：公众号"组合包更新提醒 + 完整版资料"，替换后启用 -->
