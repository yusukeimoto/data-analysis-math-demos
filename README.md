# データ解析の数学 ― デモノートブック

鹿児島大学 集中講義「データ解析の数学」（井元佑介, 京都大学）の講義ノートに対応する
実習用ノートブックである。主成分分析から高次元統計、カーネル法、ニューラルネットワーク、
最適輸送まで、講義で扱う手法を自分の手で動かして確かめられる。

第3章以降の各章に1冊ずつ、計9冊。

| ノートブック | 対応する章 | 主な内容 |
|---|---|---|
| `notebooks/ch03_pca.ipynb` | 第3章 主成分分析の理論 | 三つの定式化の一致、中心化、寄与率、白色化、確率的PCA |
| `notebooks/ch04_pca_computation.ipynb` | 第4章 計算技法と拡張 | 双対PCA、ランダム化SVD、オンラインPCA、欠測のEM |
| `notebooks/ch05_highdim.ipynb` | 第5章 高次元データの数理 | 次元の呪い、距離の集中、JL補題、MP則、BBP相転移、縮小推定 |
| `notebooks/ch06_geneig.ipynb` | 第6章 一般化固有値問題 | LDA、CCA、古典的MDS、スペクトラルクラスタリング |
| `notebooks/ch07_rkhs.ipynb` | 第7章 再生核ヒルベルト空間 | 正定値カーネル、再生性、Mercer展開、MMD |
| `notebooks/ch08_kernel_pca.ipynb` | 第8章 カーネルPCA | カーネルPCA、表現定理、カーネルリッジ回帰、Nyström、RFF |
| `notebooks/ch09_svm.ipynb` | 第9章 サポートベクターマシン | マージン、双対問題、KKT、ソフトマージン、カーネルSVM |
| `notebooks/ch10_neural_network.ipynb` | 第10章 万能近似定理 | 活性化関数、構成的証明、折れ目の数、誤差逆伝播 |
| `notebooks/ch11_advanced.ipynb` | 第11章 発展的話題 | NTK、二重降下、多様体学習、行列補完、最適輸送 |

各ノートブックは「目次 → 準備 → 各節（説明・コード・図）→ 演習 → 解答」という構成で、
説明は講義ノートの定理・式・図の番号を引いている。手元にノート
（`docs/` の PDF）を開きながら進めるとよい。

---

## 動かし方

三通りある。**何も準備したくないなら A**、手元の環境に残したいなら B か C。

### A. Google Colab（推奨・インストール不要）

ブラウザだけで動く。Google アカウントがあればよい。

1. <https://colab.research.google.com/> を開く
2. 「ファイル」→「ノートブックをアップロード」→ `notebooks/` の `.ipynb` を選ぶ
3. 先頭の「準備」セルから順に実行する

GitHub で公開されている場合は、リポジトリの URL の `github.com` の部分を
`colab.research.google.com/github` に置き換えると、ダウンロードせずに直接開ける。

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
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python check_environment.py          # 動作確認
jupyter lab notebooks/
```

Python は 3.10 以上を想定している。

---

## 動作確認

`check_environment.py` を実行すると、必要なライブラリが揃っているか、
日本語フォントが使えるか、実際に計算と描画ができるかを確かめて結果を表示する。

```
$ python check_environment.py
Python           3.12.11                              OK
numpy            2.5.3                                OK
...
日本語フォント     Noto Sans CJK JP                     OK
図の描画          test_plot.png に書き出した              OK
```

**日本語フォントが「なし」と出ても、ノートブックは動く。** 図のラベルが
自動的に英語に切り替わるだけである（各ノートブックの `L("日本語", "English")` がその切替）。
日本語で表示したい場合は

```bash
pip install japanize-matplotlib
```

を入れてから開き直すとよい（Colab では準備セルが自動で入れる）。

---

## 必要なもの

Colab の既定環境と同じ構成で動く。

- Python 3.10 以上
- numpy, scipy, matplotlib, pandas, scikit-learn
- jupyterlab（ノートブックを開くため。Colab では不要）

第11章の最適輸送の節だけ [POT](https://pythonot.github.io/) を使う。
ノートブック内のセルが自動で導入するので事前準備は要らない。
導入できない環境でも、その節以外はすべて動く。

**インターネット接続はデータのダウンロードには使わない。**
データは合成データか scikit-learn に同梱されているもの
（`load_digits`, `load_iris`, `load_breast_cancer`, `make_moons`, `make_blobs`,
`make_swiss_roll`）だけである。一度環境を作れば、あとはオフラインで動く。

GPU は不要。9冊すべて CPU で数十秒ずつで終わる。

---

## 表記について

講義ノートと同じく、**データ行列は列がサンプル** $X \in \mathbb{R}^{d\times n}$ である
（$d$ が変数の数、$n$ がサンプル数）。scikit-learn は行がサンプルなので、
受け渡しのたびに転置している。コード中にその旨のコメントがある。

---

## 演習の解答について

各ノートブックの末尾に演習があり、その下に解答のセルがある。
まず自分で `# TODO` を埋めてから解答を見ることを勧める。

配布時に解答を隠したい場合は、解答のセルを削除するか、
Colab のセルメニューから「フォーム」→「コードを非表示」にする。

---

## 困ったときは

**図の文字が四角（□□□）になる** — 日本語フォントがない。上の「動作確認」を参照。
そのままでも内容は読める（英語ラベルに切り替わらない場合は、
準備セルをもう一度実行するとよい）。

**`ModuleNotFoundError`** — 環境を作り直すか、足りないものを個別に入れる。
`python check_environment.py` が何が足りないかを教えてくれる。

**Colab で「セッションがクラッシュしました」** — メモリ不足である。
「ランタイム」→「ランタイムを再起動」してから、先頭の準備セルを実行し直す。

**途中のセルでエラーが出る** — 上のセルを飛ばしていないか確認する。
各ノートブックは上から順に実行することを前提にしている
（変数を前のセルから引き継ぐ）。「ランタイム」→「すべてのセルを実行」で直ることが多い。

---

## 授業担当者向け

- ノートブックの組み立てと検証には `tools/nbbuild.py` を使う。
  `python tools/nbbuild.py notebooks/*.ipynb` で全コードセルを順に実行し、
  エラーがないか確認できる（Jupyter カーネルを立てない方式なので、
  ノートブック内では `!pip install` などのマジックは使えない。
  導入は `subprocess` で書く）。
- GitHub で公開する場合は `python tools/set_repo.py <ユーザー名>/<リポジトリ名>` を実行すると、
  この README に各ノートブックの Colab バッジを埋め込む。学生はクリック一つで開ける。
- 講義ノート本体（PDF）は `docs/` にある。演習の解答は別冊になっており、
  この配布物には含めていない。必要なら `docs/` に置く。

## ライセンス

このリポジトリにはライセンスファイルを置いていない。公開時に追加すること。
講義資料には Creative Commons（例：CC BY 4.0）、コードには MIT などが使われることが多い。
