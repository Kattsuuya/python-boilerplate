# Python Boilerplate

このリポジトリは、Python でコマンドラインアプリケーションを作成する際のライブラリ群をまとめたボイラープレートである。

- [インストール方法](#インストール方法)
  - [Step1. uv のインストール](#step1-uv-のインストール)
  - [Step2. Python のインストール](#step2-python-のインストール)
  - [Step3. Git hooks の設定](#step3-git-hooks-の設定)
- [実行方法](#実行方法)
- [（Optional）開発者向け](#optional開発者向け)
  - [コミットメッセージのスタイル](#コミットメッセージのスタイル)
  - [よく使うタスク](#よく使うタスク)
- [プロジェクトの技術選定](#プロジェクトの技術選定)
  - [プロダクションコードに必要なライブラリ](#プロダクションコードに必要なライブラリ)
    - [設定管理](#設定管理)
    - [環境変数管理](#環境変数管理)
    - [CLI 作成](#cli-作成)
    - [ドキュメント生成](#ドキュメント生成)
    - [HTTP クライアント](#http-クライアント)
    - [データシリアライゼーション](#データシリアライゼーション)
  - [開発・CI/CD・テスト関連のツール](#開発cicdテスト関連のツール)
    - [パッケージ管理](#パッケージ管理)
    - [型チェックと静的解析](#型チェックと静的解析)
    - [テスト](#テスト)
    - [タスクランナー](#タスクランナー)
    - [コミットメッセージ管理とスタイル統一](#コミットメッセージ管理とスタイル統一)

## インストール方法

### Step1. uv のインストール

uv は Python のバージョン管理、およびパッケージ管理をするツールである。

[公式サイト](https://docs.astral.sh/uv/getting-started/installation/)に従ってインストールすること。

```bash
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# インストールできていることを確認
$ uv --version
uv 0.4.1 (823f23e22 2024-08-30)
```

### Step2. Python のインストール

本ツールは Python3.12 での動作を想定している。
下記のコマンドで Python3.12 をインストールすること。

```bash
# インストール
uv python install 3.12

# インストールできていることを確認（環境によっては `python` の代わりに `python3` や `python3.12` を使用すること）
$ python --version
Python 3.12.5
```

### Step3. Git hooks の設定

[pre-commit](https://pre-commit.com/)で簡易的なコミットの検査をしている。
下記のコマンドで設定を行うこと。

```bash
uv run pre-commit install
```

> [!NOTE]
> パッケージ管理ツール `uv` は自動的に依存ライブラリをインストールするため、インストールコマンドは不要。

## 実行方法

下記のコマンドでツールを実行する。
（初回実行時は仮想環境の構築と依存パッケージのインストールを行うため、多少時間がかかる。）

```bash
uv run main.py
```

---

## （Optional）開発者向け

### コミットメッセージのスタイル

コミットする際は必ず下記のコマンドを実行すること。
これによってコミットメッセージのスタイルを統一している。

```bash
uv run task commit
```

### よく使うタスク

タスクランナーとして [Taskipy](https://github.com/taskipy/taskipy)を採用している。
タスクの一覧は `pyproject.toml` に記述されており、下記のコマンドで確認できる。

```bash
$ uv run task --list
lint      コードスタイルを確認する
lint-fix  コードスタイルの問題を修正する
format    コードをフォーマットする
test      すべての単体テストを実行する
build-doc ドキュメントをビルドする
serve-doc ローカルサーバーでドキュメントを閲覧する
commit    コミットを作成する

# 例）コードスタイルを確認する
$ uv run task lint
```

---

## プロジェクトの技術選定

### プロダクションコードに必要なライブラリ

#### 設定管理

- **[pydantic-settings](https://docs.pydantic.dev/)**
  型安全な設定管理を提供し、環境変数や設定ファイルからの読み込みを行う

#### 環境変数管理

- **[python-dotenv](https://saurabh-kumar.com/python-dotenv/)**
  `.env`ファイルを使用して環境変数を簡単に管理する

#### CLI 作成

- **[typer](https://typer.tiangolo.com/)**
  型アノテーションを使用してシンプルに CLI アプリケーションを作成できるツール

#### ドキュメント生成

- **[mkdocs](https://www.mkdocs.org/)**
  Markdown で記述されたドキュメントを静的サイトとして生成するツール
- **[mkdocs-material](https://squidfunk.github.io/mkdocs-material/)**
  `mkdocs`のためのテーマで、視覚的に魅力的で使いやすいドキュメントを提供する
- **[mkdocstrings[python]](https://mkdocstrings.github.io/)**
  Python の Docstrings から自動的に API ドキュメントを生成する

#### HTTP クライアント

- **[httpx](https://www.python-httpx.org/)**
  非同期対応の HTTP クライアント。外部 API や Web サービスにアクセスするために使用する

#### データシリアライゼーション

- **[orjson](https://github.com/ijl/orjson)**
  高速な JSON シリアライザで、データの効率的な処理に使用する

### 開発・CI/CD・テスト関連のツール

#### パッケージ管理

- **[uv](https://docs.astral.sh/uv/)**
  Python の依存関係管理、仮想環境のセットアップ、バージョン管理を一元的に行えるツール。`pyproject.toml`をベースにプロジェクトを管理し、簡単なコマンドで依存ライブラリのインストールや更新を行える

#### 型チェックと静的解析

- **[ruff](https://docs.astral.sh/ruff/)**
  高速な Python のリンターで、コーディングスタイルの統一と静的解析を行う
- **[mypy](https://mypy-lang.org/)**
  静的な型チェックを行い、コードの品質を向上させる

#### テスト

- **[pytest](https://docs.pytest.org/en/latest/)**
  強力なテストフレームワークで、ユニットテストや統合テストに対応する

#### タスクランナー

- **[taskipy](https://github.com/illBeRoy/taskipy)**
  `pyproject.toml`を用いてタスク管理を簡単に行う

#### コミットメッセージ管理とスタイル統一

- **[pre-commit](https://pre-commit.com/)**
  Git のコミット時に自動でコードの整形やテストを実行する
- **[commitizen](https://commitizen-tools.github.io/commitizen/)**
  Conventional Commits を強制し、履歴の一貫性を維持する
