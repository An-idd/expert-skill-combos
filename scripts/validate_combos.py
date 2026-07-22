#!/usr/bin/env python3
"""校验每个已就绪的组合包：结构完整 + EXPERT.md frontmatter 合法。

就绪 = combo 目录含 EXPERT.md。未含 EXPERT.md 的目录视为建设中(WIP)，跳过不报错。
`_` 开头目录（如 _template）不校验。

用法:
    python scripts/validate_combos.py            # 校验 combos/
    python scripts/validate_combos.py --self-test # 跑内置自检
"""
import sys
import pathlib

REQUIRED_FILES = ["README.md", "EXPERT.md"]
REQUIRED_FM_KEYS = ["name", "role", "version", "targets", "pairs_with", "updated"]


def parse_frontmatter_keys(text):
    """返回 --- 围栏内的顶层 key 集合；无合法 frontmatter 返回 None。"""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    keys = set()
    for line in text[3:end].splitlines():
        line = line.strip()
        if line and not line.startswith("#") and ":" in line:
            keys.add(line.split(":", 1)[0].strip())
    return keys


def check_combo(combo_dir):
    errs = []
    for f in REQUIRED_FILES:
        if not (combo_dir / f).exists():
            errs.append(f"缺少 {f}")
    expert = combo_dir / "EXPERT.md"
    if expert.exists():
        keys = parse_frontmatter_keys(expert.read_text(encoding="utf-8"))
        if keys is None:
            errs.append("EXPERT.md 无合法 frontmatter")
        else:
            for k in REQUIRED_FM_KEYS:
                if k not in keys:
                    errs.append(f"EXPERT.md frontmatter 缺 '{k}'")
    return errs


def main(root="combos"):
    root = pathlib.Path(root)
    if not root.exists():
        print(f"找不到目录: {root}")
        return 1
    failed = False
    ready = pending = 0
    for combo in sorted(p for p in root.iterdir() if p.is_dir()):
        if combo.name.startswith("_"):
            continue
        if not (combo / "EXPERT.md").exists():
            pending += 1
            print(f"⏳ {combo.name}: 建设中 (无 EXPERT.md)，跳过")
            continue
        errs = check_combo(combo)
        if errs:
            failed = True
            print(f"❌ {combo.name}:")
            for e in errs:
                print(f"   - {e}")
        else:
            ready += 1
            print(f"✅ {combo.name}")
    print(f"\n{ready} 个就绪, {pending} 个建设中")
    return 1 if failed else 0


def self_test():
    assert parse_frontmatter_keys("---\nname: x\nrole: y\n---\nbody") == {"name", "role"}
    assert parse_frontmatter_keys("no frontmatter") is None
    assert parse_frontmatter_keys("---\nonly: one\n") is None  # 未闭合
    assert "pairs_with" in REQUIRED_FM_KEYS
    print("self-test passed")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    else:
        sys.exit(main())
