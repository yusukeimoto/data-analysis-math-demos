#!/usr/bin/env python3
"""README に Colab の「開く」バッジを埋め込む（授業担当者向け）。

GitHub で公開したあと、一度だけ実行する::

    python tools/set_repo.py <ユーザー名>/<リポジトリ名>
    python tools/set_repo.py imoto-lab/data-analysis-math-demos --branch main

README の表の各行に、そのノートブックを Colab で直接開くバッジが付く。
学生はクリック一つで開ける（ダウンロード不要）。

すでにバッジがある場合は貼り替える。`--remove` で外せる。
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

BADGE = ("[![Colab](https://colab.research.google.com/assets/colab-badge.svg)]"
         "(https://colab.research.google.com/github/{repo}/blob/{branch}/{path})")
ROW = re.compile(r'^\|\s*(?:\[!\[Colab\][^|]*\)\s*)?`(notebooks/[\w./-]+\.ipynb)`\s*\|', re.M)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="README に Colab バッジを埋め込む")
    ap.add_argument("repo", nargs="?", help="<ユーザー名>/<リポジトリ名>")
    ap.add_argument("--branch", default="main", help="ブランチ名（既定 main）")
    ap.add_argument("--readme", default="README.md")
    ap.add_argument("--remove", action="store_true", help="バッジを外す")
    a = ap.parse_args(argv)

    if not a.remove and not a.repo:
        ap.error("リポジトリ名を指定してください（例: imoto-lab/data-analysis-math-demos）")
    if a.repo and a.repo.count("/") != 1:
        ap.error(f"'<ユーザー名>/<リポジトリ名>' の形で指定してください: {a.repo!r}")

    p = Path(a.readme)
    if not p.exists():
        print(f"{p} が見つかりません。リポジトリの直下で実行してください。", file=sys.stderr)
        return 1
    text = p.read_text(encoding="utf-8")

    n = 0

    def sub(m):
        nonlocal n
        n += 1
        path = m.group(1)
        if a.remove:
            return f"| `{path}` |"
        badge = BADGE.format(repo=a.repo, branch=a.branch, path=path)
        return f"| {badge} `{path}` |"

    out = ROW.sub(sub, text)
    if n == 0:
        print("README の表にノートブックの行が見つかりませんでした。"
              "`notebooks/xxx.ipynb` を含む表を想定しています。", file=sys.stderr)
        return 1
    p.write_text(out, encoding="utf-8")
    if a.remove:
        print(f"{n} 件のバッジを外しました。")
    else:
        print(f"{n} 件のバッジを埋め込みました（{a.repo} / {a.branch}）。")
        print("README をブラウザで確認し、リンク先が開くことを確かめてください。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
