# 贡献指南

欢迎贡献组合包。这个项目的全部信用建立在"实测"两个字上，所以流程围绕实测设计。

## 贡献流程

1. 复制 [`combos/_template`](combos/_template) 为 `combos/<你的岗位>/`。
2. 按模板填写 `README.md`、`EXPERT.md`、`skills/*/SKILL.md`。
3. 至少在一个工具（WorkBuddy / QoderWork / Claude）**实测通过**，并附截图。
4. 提 PR。维护者复测通过后合并（实测权在维护者手里，这是质量护城河）。

## 规范要点

- **EXPERT.md frontmatter 必填**：`name` `role` `version` `targets` `pairs_with` `updated`。
  `pairs_with` 让"组合关系"机器可读，是未来元技能/网站自动推荐的数据基础。
- **「工作流程」一节必须显式写明**：专家在什么步骤调用什么 skill。这是"组合包"区别于"prompt 大全"的核心。
- CI 会校验每个含 `EXPERT.md` 的组合包结构完整、frontmatter 合法。未含 `EXPERT.md` 的目录视为建设中（WIP），跳过。

## 署名与第三方 skill 收录规则

- 收录第三方 skill 的前提：**有明确 License**。保留原作者署名、原仓库链接、原 License。
- 组合包内的 prompt 与文档采用 **CC-BY-4.0**：可转载可修改，但必须署名来源。
- 若你的组合包整合了他人的 skill，在 combo README 的"来源与署名"段列明。

## PR 模板（强制勾选）

- [ ] 我已在至少一个工具实测通过，并附截图。
- [ ] EXPERT.md frontmatter 完整，`pairs_with` 已填。
- [ ] 「工作流程」显式声明了何时调用哪个 skill。
- [ ] 如含第三方 skill，已保留原署名与 License。
