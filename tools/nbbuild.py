#!/usr/bin/env python3
"""講義ノート付属 Colab ノートブックの組み立てと実行検証。

使い方（ノートブック生成側）::

    from nbbuild import build, SETUP_MD, SETUP_CODE
    build("ch03_pca.ipynb", [
        ("md",   "# 第3章 ..."),
        ("md",   SETUP_MD), ("code", SETUP_CODE),
        ("md",   "## 3.1 ..."),
        ("code", "..."),
    ])

検証側::

    python nbbuild.py colab/*.ipynb      # 全セルを実行してエラーがないか見る

Colab の既定環境（numpy / scipy / matplotlib / pandas / scikit-learn）だけで
動くことを前提にする。それ以外（POT など）を使う章は、そのノートブックの
先頭で pip install する。
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# ---------------------------------------------------------------- 共通セル

SETUP_MD = """## 準備

最初にこのセルを実行する。日本語フォントの設定（Colab には既定で入っていない）と、
以降で使うライブラリの読み込みを行う。フォントの導入に失敗した場合は
図のラベルが自動的に英語に切り替わる（`L()` 関数）。"""

SETUP_CODE = '''import subprocess, sys, warnings
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

warnings.filterwarnings("ignore", category=UserWarning)


def _setup_japanese_font():
    """日本語が出せるフォントを探し、なければ入れる。成功したら True。"""
    cands = ["IPAexGothic", "IPAGothic", "Noto Sans CJK JP", "Noto Sans JP",
             "TakaoGothic", "Yu Gothic", "Hiragino Sans"]
    have = {f.name for f in fm.fontManager.ttflist}
    for name in cands:
        if name in have:
            matplotlib.rcParams["font.family"] = name
            return True
    # Colab 想定：pip で導入する
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q",
                        "japanize-matplotlib"], check=True, timeout=180)
        import japanize_matplotlib  # noqa: F401  読み込むだけで設定される
        return True
    except Exception:
        pass
    # 予備：apt で IPA フォント
    try:
        subprocess.run("apt-get -qq -y install fonts-ipafont-gothic",
                       shell=True, check=True, timeout=300)
        fm._load_fontmanager(try_read_cache=False)
        matplotlib.rcParams["font.family"] = "IPAGothic"
        return True
    except Exception:
        return False


JP = _setup_japanese_font()


def L(ja, en):
    """日本語フォントが使えれば ja、駄目なら en を返す（図のラベル用）。"""
    return ja if JP else en


matplotlib.rcParams.update({
    "font.size": 11, "axes.titlesize": 12, "axes.labelsize": 11,
    "figure.dpi": 110, "savefig.bbox": "tight",
    "axes.grid": True, "grid.alpha": 0.25, "grid.linewidth": 0.6,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.unicode_minus": False,
})

# 講義ノートの図と同じ色
C = {"blue": "#1f4e79", "red": "#c0392b", "green": "#1e8449",
     "orange": "#d68910", "purple": "#6a4c93", "gray": "#7f8c8d"}

print("日本語フォント:", "有効" if JP else "無効（図のラベルは英語になる）")
print("numpy", np.__version__, "| matplotlib", matplotlib.__version__)'''


# ------------------------------------------------------------- 組み立て

def build(path: str, cells: list, title: str | None = None) -> str:
    """(種別, 中身) の並びから .ipynb を書き出す。種別は "md" か "code"。"""
    out = []
    for kind, text in cells:
        text = text.rstrip("\n")
        if kind == "md":
            out.append({"cell_type": "markdown", "metadata": {},
                        "source": text.splitlines(keepends=True)})
        elif kind == "code":
            out.append({"cell_type": "code", "metadata": {}, "execution_count": None,
                        "outputs": [], "source": text.splitlines(keepends=True)})
        else:
            raise ValueError(f"未知のセル種別: {kind}")
    nb = {
        "cells": out,
        "metadata": {
            "colab": {"provenance": [], "toc_visible": True,
                      **({"name": title} if title else {})},
            "kernelspec": {"name": "python3", "display_name": "Python 3"},
            "language_info": {"name": "python"},
        },
        "nbformat": 4, "nbformat_minor": 0,
    }
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
    return f"{p} : {len(out)} セル（コード {sum(1 for k, _ in cells if k == 'code')}）"


# --------------------------------------------------------------- 実行検証

def run(path: str, timeout: int = 900) -> dict:
    """ノートブックのコードセルを頭から順に実行し、エラーを拾う。

    このサンドボックスでは Jupyter カーネルが起動できない（ZMQ が
    ローカルネットワークインターフェースを開けない）ので、nbclient は使わず、
    共有の名前空間に対して exec を順に適用する。ノートブックを上から
    実行したときと同じ意味になる。

    そのかわり IPython のマジック（``!pip install`` や ``%matplotlib``）は
    実行できない。ノートブック側では代わりに次の形を使うこと::

        try:
            import ot
        except ImportError:
            subprocess.run([sys.executable, "-m", "pip", "install", "-q", "pot"], check=True)
            import ot

    これは Colab でもこの検証でも同じように動く。
    """
    import io
    import json as _json
    import traceback
    from contextlib import redirect_stdout

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    nb = _json.loads(Path(path).read_text(encoding="utf-8"))
    ns = {"__name__": "__main__"}
    errs, n_fig, n_code = [], 0, 0
    for i, cell in enumerate(nb["cells"]):
        if cell["cell_type"] != "code":
            continue
        src = "".join(cell["source"])
        n_code += 1
        if src.lstrip().startswith(("!", "%")) or "\n!" in src or "\n%" in src:
            errs.append((i, "MagicNotAllowed",
                         "IPython マジック（!pip / %matplotlib）は使わず subprocess を使うこと"))
            continue
        plt.close("all")
        buf = io.StringIO()
        try:
            with redirect_stdout(buf):
                exec(compile(src, f"{Path(path).name}:cell{i}", "exec"), ns, ns)
        except Exception as exc:
            tb = traceback.format_exc().strip().splitlines()[-1]
            errs.append((i, type(exc).__name__, tb[:200]))
        n_fig += len(plt.get_fignums())
        plt.close("all")
    return {"path": path, "cells": len(nb["cells"]), "code_cells": n_code,
            "errors": errs, "figures": n_fig}


def main(argv):
    if not argv:
        print(__doc__)
        return 0
    bad = 0
    for p in argv:
        r = run(p)
        mark = "OK " if not r["errors"] else "NG "
        print(f"{mark}{Path(p).name:<28}セル {r['cells']:>3} / 図 {r['figures']:>2}")
        for i, en, ev in r["errors"]:
            print(f"      cell {i}: {en}: {ev}")
            bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
