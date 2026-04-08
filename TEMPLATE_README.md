# python-template

Google Cloud Run 向け Python プロジェクトのテンプレートです。[Copier](https://copier.readthedocs.io/) で管理しています。

## 主な特徴

- **FastAPI** によるサンプルアプリケーション
- **Cloud Run** 環境では `google-cloud-logging` を自動セットアップ（ローカルでは標準ロギングにフォールバック）
- **uv** によるパッケージ管理・高速なロックファイル生成
- **ruff** によるリント・フォーマット（全ルール有効）
- **ty** による型チェック
- **pre-commit** フックによるコード品質の自動チェック
- **pytest** + asyncio によるテスト
- GitHub Actions CI（lint / typecheck / test / Dockerfile lint）
- Dependabot による依存関係の自動更新（Docker / GitHub Actions / uv）
- Docker Compose によるローカル開発環境（ファイル同期 + ホットリロード）

## 使い方

```bash
uvx copier copy gh:ssfuno/python-template ./my-project --trust
```

対話形式で以下を入力します:

| 項目 | 説明 | デフォルト |
|---|---|---|
| `project_name` | pyproject.toml の `name` フィールド | なし |
| `description` | プロジェクトの説明 | `Add your description here` |
| `python_version` | Python バージョン | `3.13` |

生成後は `uv lock` が自動実行されます。

## テンプレートの更新を既存プロジェクトに適用

```bash
cd ./my-project
uvx copier update --trust
```

## 参考にした資料

### 全般
- https://github.com/modelcontextprotocol/python-sdk

### コンテナ
- https://docs.docker.com/reference/cli/docker/init/
- https://docs.astral.sh/uv/guides/integration/docker/
- https://future-architect.github.io/articles/20250602a/

### ロギング
- https://cloud.google.com/python/docs/reference/logging/latest/std-lib-integration
- https://blog.g-gen.co.jp/entry/structured-logging-with-cloud-run

### GitHub
- https://docs.astral.sh/uv/guides/integration/github/
- https://docs.github.com/ja/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates
