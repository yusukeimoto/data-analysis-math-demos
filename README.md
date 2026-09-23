# データ解析の数学 — デモノートブック

主成分分析、高次元統計、カーネル法、ニューラルネットワーク、最適輸送などを、Pythonによる数値実験を通して学ぶための教材です。数式と計算結果を対応させながら、パラメータを変えたときの振る舞いを確かめられます。

集中講義「データ解析の数学」の講義ノートに対応しています。講義の受講者に加え、データ解析の数学を学びたい方の自習も想定しています。

**下の章名または「Open in Colab」ボタンをクリックすると、Google Colabでノートブックを開けます。PCへのPythonのインストールは不要です。**

## デモ一覧

講義ノートの第3章から第11章に対応する、全9冊のノートブックです。

| 対応する章（クリックでColabを開く） | 主な内容 | 実行 |
|---|---|---|
| [第3章 主成分分析の理論](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch03_pca.ipynb) | 三つの定式化の一致、中心化、寄与率、白色化、確率的PCA | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch03_pca.ipynb) |
| [第4章 計算技法と拡張](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch04_pca_computation.ipynb) | 双対PCA、ランダム化SVD、オンラインPCA、欠測のEM | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch04_pca_computation.ipynb) |
| [第5章 高次元データの数理](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch05_highdim.ipynb) | 次元の呪い、距離の集中、JL補題、MP則、BBP相転移、縮小推定 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch05_highdim.ipynb) |
| [第6章 一般化固有値問題](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch06_geneig.ipynb) | LDA、CCA、古典的MDS、スペクトラルクラスタリング | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch06_geneig.ipynb) |
| [第7章 再生核ヒルベルト空間](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch07_rkhs.ipynb) | 正定値カーネル、再生性、Mercer展開、MMD | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch07_rkhs.ipynb) |
| [第8章 カーネルPCA](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch08_kernel_pca.ipynb) | カーネルPCA、表現定理、カーネルリッジ回帰、Nyström、RFF | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch08_kernel_pca.ipynb) |
| [第9章 サポートベクターマシン](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch09_svm.ipynb) | マージン、双対問題、KKT、ソフトマージン、カーネルSVM | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch09_svm.ipynb) |
| [第10章 万能近似定理](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch10_neural_network.ipynb) | 活性化関数、構成的証明、折れ目の数、誤差逆伝播 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch10_neural_network.ipynb) |
| [第11章 発展的話題](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch11_advanced.ipynb) | NTK、二重降下、多様体学習、行列補完、最適輸送 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yusukeimoto/data-analysis-math-demos/blob/main/notebooks/ch11_advanced.ipynb) |

コードだけを閲覧したい場合は、[notebooksフォルダ](https://github.com/yusukeimoto/data-analysis-math-demos/tree/main/notebooks)をご覧ください。講義ノートは[docsフォルダ](https://github.com/yusukeimoto/data-analysis-math-demos/tree/main/docs)にあります。

## Google Colabで始める

1. 上の一覧から学びたい章を開きます。
2. Googleアカウントでログインし、ランタイムに接続します。
3. 先頭の「準備」セルから、上から順に実行します。セル左側の実行ボタン、または `Shift + Enter` で実行できます。
4. コードやパラメータを変えて、結果を比較してみてください。

編集内容を保存する場合は、Colabの「ファイル」から「ドライブにコピーを保存」を選んでください。自分のコピーを編集しても、GitHub上の元のノートブックは変更されません。

GPUは不要です。実行時間は章の内容や計算環境によって異なります。初回は、追加ライブラリや日本語フォントの準備に時間がかかる場合があります。

## 教材の使い方

各ノートブックは、目次、準備、解説と数値実験、演習、解答で構成されています。講義ノートの定理・式・図の番号を参照しながら進めてください。

演習は、まず自分で `# TODO` の箇所を埋め、その後で末尾の解答と比較することを勧めます。

### データ行列の表記

講義ノートに合わせ、データ行列は **列がサンプル** となる
$X \in \mathbb{R}^{d\times n}$ とします。$d$ は変数の数、$n$ はサンプル数です。
scikit-learnは行をサンプルとして扱うため、必要に応じて転置して受け渡します。

## 自分のPCで実行する

Python 3.10以上を想定しています。まずリポジトリを取得し、そのフォルダに移動してください。

```bash
git clone https://github.com/yusukeimoto/data-analysis-math-demos.git
cd data-analysis-math-demos
```

Gitを使わない場合は、GitHubの「Code」→「Download ZIP」からダウンロードし、展開したフォルダをターミナルで開いてください。

### condaを使う場合

```bash
conda env create -f environment.yml
conda activate dam-demos
python check_environment.py
jupyter lab notebooks/
```

### pipとvenvを使う場合

仮想環境を作成します。

```bash
python -m venv .venv
```

macOS / Linuxでは、次のコマンドで有効化します。

```bash
source .venv/bin/activate
```

Windowsのコマンドプロンプトでは、次のコマンドを使います。

```bat
.venv\Scripts\activate.bat
```

続いて、必要なライブラリをインストールします。

```bash
python -m pip install -r requirements.txt
python check_environment.py
jupyter lab notebooks/
```

### 使用ライブラリとデータ

主にNumPy、SciPy、Matplotlib、pandas、scikit-learnを使用します。ローカルでノートブックを開くためにJupyterLab、日本語表示のためにjapanize-matplotlibを利用します。第11章の一部では[Python Optimal Transport（POT）](https://pythonot.github.io/)を使用します。

デモには合成データやscikit-learn同梱のデータを用います。別途データセットをダウンロードする必要はありません。Colabの利用や、ライブラリ・フォントのインストールにはインターネット接続が必要です。

## 困ったときは

| 症状 | 対処方法 |
|---|---|
| 図の日本語が四角で表示される | 先頭の準備セルを実行し直してください。日本語フォントを利用できない場合、図のラベルは英語に切り替わります。ローカルでは `python -m pip install japanize-matplotlib` で導入できます。 |
| `ModuleNotFoundError` が出る | 使用中の環境に必要なライブラリがあるか確認してください。ローカルでは `python check_environment.py` で確認できます。 |
| 途中のセルで変数が未定義になる | 前のセルで定義した変数を使います。先頭から順に実行し直してください。 |
| Colabのセッションが切れる・クラッシュする | メモリ不足やセッションの制限などが考えられます。再接続またはランタイムを再起動し、準備セルから実行し直してください。必要に応じてデータ数や反復回数を減らしてください。 |

不具合や誤記を見つけた場合は、[GitHub Issues](https://github.com/yusukeimoto/data-analysis-math-demos/issues)でお知らせください。対象のノートブック、実行環境（Colab / ローカル）、エラーメッセージを添えていただくと確認しやすくなります。

## 授業での利用について

各ノートブックには演習の解答が含まれます。解答を見せずに配布したい場合は、配布用コピーから該当セルを削除してください。セルの折りたたみやコードの非表示だけでは、解答へのアクセスを防げません。

## ライセンス

現時点では、このリポジトリにコード・教材の再利用条件を定めるライセンスは設定されていません。再配布や改変版の公開などを希望する場合は、著者にご確認ください。外部ライブラリや第三者のデータ・引用資料には、それぞれのライセンス・利用条件が適用されます。
