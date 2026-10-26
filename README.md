# データ解析の数学 ― デモノートブック

集中講義「データ解析の数学」（井元佑介, 京都大学）の講義ノートに対応する実習用ノートブックである。主成分分析から高次元統計、カーネル法、ニューラルネットワーク、最適輸送まで、講義で扱う手法を自分の手で動かして確かめられる。

第3章以降の各章に1冊ずつ、計9冊。

| ノートブック | 対応する章 | 主な内容 |
|---|---|---|
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch03_pca.ipynb) `notebooks/ch03_pca.ipynb` | 第3章 主成分分析の理論 | 三つの定式化の一致、中心化、寄与率、白色化、確率的PCA |
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch04_pca_computation.ipynb) `notebooks/ch04_pca_computation.ipynb` | 第4章 計算技法と拡張 | 双対PCA、ランダム化SVD、オンラインPCA、欠測のEM |
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch05_highdim.ipynb) `notebooks/ch05_highdim.ipynb` | 第5章 高次元データの数理 | 次元の呪い、距離の集中、JL補題、MP則、BBP相転移、縮小推定 |
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch06_geneig.ipynb) `notebooks/ch06_geneig.ipynb` | 第6章 一般化固有値問題 | LDA、CCA、古典的MDS、スペクトラルクラスタリング |
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch07_rkhs.ipynb) `notebooks/ch07_rkhs.ipynb` | 第7章 再生核ヒルベルト空間 | 正定値カーネル、再生性、Mercer展開、MMD |
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch08_kernel_pca.ipynb) `notebooks/ch08_kernel_pca.ipynb` | 第8章 カーネルPCA | カーネルPCA、表現定理、カーネルリッジ回帰、Nyström、RFF |
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch09_svm.ipynb) `notebooks/ch09_svm.ipynb` | 第9章 サポートベクターマシン | マージン、双対問題、KKT、ソフトマージン、カーネルSVM |
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch10_neural_network.ipynb) `notebooks/ch10_neural_network.ipynb` | 第10章 万能近似定理 | 活性化関数、構成的証明、折れ目の数、誤差逆伝播 |
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch11_advanced.ipynb) `notebooks/ch11_advanced.ipynb` | 第11章 発展的話題 | NTK、二重降下、多様体学習、行列補完、最適輸送 |

各ノートブックは「目次 → 準備 → 各節（説明・コード・図）→ 演習」という構成で、説明は講義ノートの定理・式・図の番号を引いている。手元にノート（`docs/` の PDF）を開きながら進めるとよい。

---

## 動作方法

三通りある。**何も準備したくないなら A**、手元の環境に残したいなら B か C。

### A. Google Colab（推奨・インストール不要）

ブラウザだけで動く。Google アカウントがあればよい。

1. 上の表の Colab バッジを押す（ダウンロード不要でそのまま開く）
2. 先頭の「準備」セルから順に実行する

ローカルに保存した `.ipynb` を使う場合は、<https://colab.research.google.com/> を開いて
「ファイル」→「ノートブックをアップロード」からも開ける。

講義ノート（`docs/` の PDF）の各章冒頭の脚注にも同じリンクを張ってある。

リンクの作り方は単純で、GitHub の URL の `github.com` を`colab.research.google.com/github` に置き換えるだけである：

```
https://github.com/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch03_pca.ipynb
https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch03_pca.ipynb
```

### B. 自分の PC（conda を使う場合）

```bash
conda env create -f environment.yml
conda activate dam-demos
python check_environment.py          # 動作確認
jupyter lab notebooks/               # ノートブックを開く
```

### C. 自分の PC（pip と venv を使う場合）

```bash
python -m venv .venv

# 仮想環境を有効にする（環境に合わせて 1 行だけ実行）
source .venv/bin/activate            # macOS / Linux
.venv\Scripts\Activate.ps1           # Windows PowerShell
.venv\Scripts\activate.bat           # Windows コマンドプロンプト

pip install -r requirements.txt
python check_environment.py          # 動作確認
jupyter lab notebooks/
```

Python は 3.10 以上を想定している。

---

## 動作確認

`check_environment.py` を実行すると、必要なライブラリが揃っているか、日本語フォントが使えるか、実際に計算と描画ができるかを確かめて結果を表示する。

```
$ python check_environment.py
Python           3.12.11                              OK
numpy            2.5.3                                OK
...
日本語フォント     Noto Sans CJK JP                     OK
図の描画          test_plot.png に書き出した              OK
```

**日本語フォントが「なし」と出ても、ノートブックは動く。** 図のラベルが自動的に英語に切り替わるだけである（各ノートブックの `L("日本語", "English")` がその切替）。日本語で表示したい場合は

```bash
pip install japanize-matplotlib
```

を入れてから開き直すとよい（Colab では準備セルが自動で入れる）。

---

## 必要なもの

主要な依存ライブラリ（numpy, scipy, matplotlib, pandas, scikit-learn）は Colab の既定環境で利用できる。ローカル環境では以下を用意する。

- Python 3.10 以上
- numpy, scipy, matplotlib, pandas, scikit-learn
- jupyterlab（ノートブックを開くため。Colab では不要）

第11章の最適輸送の節だけ [POT](https://pythonot.github.io/) を使う。`requirements.txt` と `environment.yml` には入れてあるので、上の B か C の手順なら自動で入る。入っていない環境では、その節の POT との比較（Gromov--Wasserstein の反復解）だけを飛ばして実行する（ノートブックが `import ot` の失敗を検出して skip する。自動インストールはしない）。Colab で比較まで見たい場合は `!pip install pot` を一度実行してから開き直すとよい。

**インターネット接続はデータのダウンロードには使わない。**データは合成データか scikit-learn に同梱されているもの（`load_digits`, `load_iris`, `load_breast_cancer`, `make_moons`, `make_blobs`, `make_swiss_roll`）だけである。一度環境を作れば、あとはオフラインで動く。

GPU は不要。9冊すべて CPU で動き、1冊あたり数十秒〜数分程度である（環境による）。

---

## 表記について

ノートブックのコードでは、**データ行列は行がサンプル** $X \in \mathbb{R}^{n\times d}$ である（$n$ がサンプル数、$d$ が変数の数）。scikit-learn や pandas の `DataFrame` と同じ向きなので、`fit(X, y)` にそのまま渡せる。

いっぽう**講義ノート本文（数式）は列がサンプル** $X \in \mathbb{R}^{d\times n}$ である。$x_i$ を列ベクトルとして並べる線形代数の記法に合わせてあるためで、本文とコードでは転置の向きが逆になる。対応は次のとおり。

| 本文（列がサンプル） | コード（行がサンプル） |
|---|---|
| $\widetilde{X}$ の中心化 $\widetilde{X}=X-\bar{x}\mathbf{1}^\top$ | `Xt = X - X.mean(axis=0)` |
| 標本共分散 $\widehat\Sigma=\frac1n\widetilde{X}\widetilde{X}^\top$（$d\times d$） | `Xt.T @ Xt / n` |
| グラム行列 $\widetilde{X}^\top\widetilde{X}$（$n\times n$） | `Xt @ Xt.T` |
| 主成分スコア $Z=U_k^\top\widetilde{X}$（$k\times n$） | `Z = Xt @ U[:, :k]`（$n\times k$） |
| 第 $i$ サンプル $x_i$ | `X[i]` |
| 第 $j$ 変数 | `X[:, j]` |

共分散行列・グラム行列・カーネル行列・ラプラシアンの形と中身は規約に依らない。向きが変わるのはデータ行列とスコア行列だけである。各ノートブックの冒頭と「準備」にも同じ注記がある。

**乱数を使う例の数値は、講義ノート本文の数値と一致しないことがある。** ノートブックは $n\times d$ で乱数を生成するので割り当てが本文と変わるためで、示している現象と結論は同じである（解析的に決まる量や実データの例は一致する）。

---

## 演習について

各ノートブックの末尾に演習がある。`# TODO` を埋めて実行すると答えが出る形にしてある。

**解答例はこの配布物には含まれていない。** 授業でも扱わないので、各自で取り組むこと。行き詰まったら、その節の本文と講義ノート（`docs/` の PDF）の該当箇所に戻るとよい。演習は直前の節で使った道具だけで解けるように作ってある。

---

## 困ったときは

**図の文字が四角（□□□）になる** — 日本語フォントがない。上の「動作確認」を参照。そのままでも内容は読める（英語ラベルに切り替わらない場合は、準備セルをもう一度実行するとよい）。

**`ModuleNotFoundError`** — 環境を作り直すか、足りないものを個別に入れる。`python check_environment.py` が何が足りないかを教えてくれる。

**Colab で「セッションがクラッシュしました」** — メモリ不足である。「ランタイム」→「ランタイムを再起動」してから、先頭の準備セルを実行し直す。

**途中のセルでエラーが出る** — 上のセルを飛ばしていないか確認する。各ノートブックは上から順に実行することを前提にしている（変数を前のセルから引き継ぐ）。「ランタイム」→「すべてのセルを実行」で直ることが多い。

---

## ライセンス

- **コード**（`notebooks/` 内のコードセル、`tools/`、`check_environment.py`）: MIT License（`LICENSE`）
- **文章・図**（`notebooks/` 内の Markdown セル、`docs/` 以下の講義ノート PDF）: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)（`LICENSE-docs`）

文章・図は CC BY 4.0 に従い、著作者表示のうえで自由に利用・改変・再配布できる。コードは MIT License に従う。授業や勉強会での利用に許諾は要らない。

Copyright (c) 2026 Yusuke Imoto
