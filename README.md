# Python AIエージェント開発カリキュラム

Pythonを題材にしてプログラミング経験のない人間をAIエージェント開発が可能な状態にするカリキュラムです。

[![Python CI](https://github.com/Minat065/python_subject/actions/workflows/ci.yml/badge.svg)](https://github.com/Minat065/python_subject/actions/workflows/ci.yml)

## 概要

このリポジトリは、プログラミング初心者がPythonの基礎からAIエージェント開発までを学習できるカリキュラムを提供します。

## カリキュラム構成

| レッスン | タイトル | 内容 |
|---------|---------|------|
| 01 | [Python基礎](lessons/01_python_basics/) | 変数、データ型、条件分岐、ループ |
| 02 | [関数とモジュール](lessons/02_functions_modules/) | 関数定義、引数、モジュール |
| 03 | [オブジェクト指向](lessons/03_object_oriented/) | クラス、継承、ポリモーフィズム |
| 04 | [APIの基礎](lessons/04_api_basics/) | HTTPリクエスト、JSON処理 |
| 05 | [AIエージェント入門](lessons/05_ai_agent_intro/) | LLM、プロンプト、エージェント設計 |

## 課題の進め方

1. **ブランチを作成する**
   ```bash
   git checkout -b lesson01-あなたの名前
   ```

2. **課題を実装する**
   - 各レッスンの `exercises/` ディレクトリにある課題ファイルを編集
   - `# TODO:` コメントの部分を実装

3. **プルリクエストを作成する**
   - 変更をコミットしてプッシュ
   - GitHub上でプルリクエストを作成

4. **自動テストの確認**
   - プルリクエストを作成すると自動テストが実行されます
   - すべてのテストに合格すれば課題完了！

## ローカル環境でのテスト

```bash
# 依存関係のインストール
pip install pytest ruff

# lintの実行
ruff check .

# テストの実行
pytest tests/ -v
```

## CI/CD

プルリクエスト時に以下の自動チェックが実行されます：

- **Linting**: コーディング規約のチェック（Ruff）
- **Testing**: 自動テストの実行（pytest）

## ライセンス

MIT License
