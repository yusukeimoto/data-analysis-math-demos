#!/usr/bin/env python3
"""実習ノートブックが動く環境かどうかを確かめる。

    python check_environment.py

必要なライブラリの有無とバージョン、日本語フォントが使えるか、
実際に計算と描画ができるかを順に確かめて結果を表示する。
足りないものがあれば入れ方を案内する。
"""
from __future__ import annotations

import importlib
import platform
import sys

OK, NG, WARN = "OK", "なし", "注意"
# (import 名, 表示名, 最低バージョン, 必須か)
NEEDED = [
    ("numpy", "numpy", (1, 24), True),
    ("scipy", "scipy", (1, 10), True),
    ("matplotlib", "matplotlib", (3, 6), True),
    ("pandas", "pandas", (1, 5), True),
    ("sklearn", "scikit-learn", (1, 2), True),
    ("jupyterlab", "jupyterlab", None, False),
    ("ot", "POT（第11章の最適輸送のみ）", None, False),
    ("japanize_matplotlib", "japanize-matplotlib（日本語フォント）", None, False),
]


def _width(s):
    """全角を2桁として数えた表示幅。"""
    import unicodedata
    return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in s)


def _pad(s, w):
    return s + " " * max(w - _width(s), 1)


def _row(name, detail, status):
    print("  " + _pad(name, 34) + _pad(detail, 38) + status)


def _ver_tuple(s):
    out = []
    for part in s.split(".")[:2]:
        digits = "".join(c for c in part if c.isdigit())
        out.append(int(digits) if digits else 0)
    return tuple(out)


def main() -> int:
    print("=" * 72)
    print("  データ解析の数学 ― デモノートブック  環境チェック")
    print("=" * 72)

    problems, notes = [], []

    print("\n[1] Python")
    pv = sys.version_info
    ok = (pv.major, pv.minor) >= (3, 10)
    _row("Python", platform.python_version(), OK if ok else NG)
    if not ok:
        problems.append("Python 3.10 以上が必要です。新しい Python を入れてください。")
    _row("実行環境", f"{platform.system()} {platform.machine()}", "")

    print("\n[2] ライブラリ")
    missing_required, missing_optional = [], []
    for mod, disp, minver, required in NEEDED:
        try:
            m = importlib.import_module(mod)
        except Exception:
            _row(disp, "見つからない", NG if required else "任意")
            (missing_required if required else missing_optional).append(mod)
            continue
        v = getattr(m, "__version__", "?")
        status = OK
        if minver and v != "?" and _ver_tuple(v) < minver:
            status = WARN
            notes.append(f"{disp} が古い（{v}）。{'.'.join(map(str, minver))} 以上を勧めます。")
        _row(disp, v, status)

    if missing_required:
        pkgs = " ".join({"sklearn": "scikit-learn"}.get(m, m) for m in missing_required)
        problems.append(f"必須のライブラリが足りません:  pip install {pkgs}")

    print("\n[3] 日本語フォント")
    jp_name = None
    try:
        import matplotlib.font_manager as fm
        have = {f.name for f in fm.fontManager.ttflist}
        for cand in ["IPAexGothic", "IPAGothic", "Noto Sans CJK JP", "Noto Sans JP",
                     "TakaoGothic", "Yu Gothic", "Hiragino Sans", "MS Gothic"]:
            if cand in have:
                jp_name = cand
                break
    except Exception:
        pass
    if jp_name:
        _row("日本語フォント", jp_name, OK)
    elif "japanize_matplotlib" not in missing_optional:
        _row("日本語フォント", "japanize-matplotlib で補う", OK)
    else:
        _row("日本語フォント", "見つからない", "任意")
        notes.append("日本語フォントがありません。図のラベルは自動的に英語になります"
                     "（内容は読めます）。日本語で出したい場合は "
                     "pip install japanize-matplotlib を実行してください。")

    print("\n[4] 計算と描画")
    if missing_required:
        _row("動作テスト", "ライブラリが足りないため省略", "—")
    else:
        try:
            import numpy as np
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
            from sklearn.datasets import load_digits

            rng = np.random.default_rng(0)
            X = np.diag([2.0, 0.5]) @ rng.standard_normal((2, 300))   # 列がサンプル
            Xc = X - X.mean(axis=1, keepdims=True)
            w, V = np.linalg.eigh(Xc @ Xc.T / X.shape[1])
            _row("PCA の固有値", f"{w[::-1].round(3).tolist()}（理論値 4, 0.25 付近）", OK)

            d = load_digits()
            _row("同梱データ", f"load_digits: {d.data.shape[0]} 枚 × {d.data.shape[1]} 画素", OK)

            # 見つけたフォントを実際に適用して、日本語が出るところまで確かめる
            if jp_name:
                matplotlib.rcParams["font.family"] = jp_name
            elif "japanize_matplotlib" not in missing_optional:
                import japanize_matplotlib  # noqa: F401
            title = "テスト（日本語）" if (jp_name or "japanize_matplotlib" not in missing_optional) \
                else "test (ASCII fallback)"
            fig, ax = plt.subplots(figsize=(4, 3))
            ax.scatter(X[0], X[1], s=6)
            ax.set_title(title)
            ax.set_xlabel("$x_1$")
            import warnings
            with warnings.catch_warnings(record=True) as caught:
                warnings.simplefilter("always")
                fig.savefig("test_plot.png", dpi=80, bbox_inches="tight")
            plt.close(fig)
            tofu = [w for w in caught if "missing from font" in str(w.message)]
            if tofu:
                _row("図の描画", "書き出したが日本語が欠けた", WARN)
                notes.append("図に日本語を描こうとすると文字が欠けます（□ になります）。"
                             "pip install japanize-matplotlib を実行してください。")
            else:
                _row("図の描画", f"test_plot.png に書き出した（{title}）", OK)
        except Exception as exc:
            _row("動作テスト", f"{type(exc).__name__}: {exc}"[:34], NG)
            problems.append(f"動作テストで失敗しました: {type(exc).__name__}: {exc}")

    print("\n" + "=" * 72)
    if problems:
        print("  対応が必要です")
        for p in problems:
            print(f"   * {p}")
    else:
        print("  準備できています。jupyter lab notebooks/ でノートブックを開いてください。")
    for n in notes:
        print(f"   （注）{n}")
    print("=" * 72)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
