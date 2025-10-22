# Python Template for Cloud Run

## 主な特徴
- FastAPIのサンプルアプリケーション
- Cloud Run環境では`google-cloud-logging`を自動的にセットアップ

## ローカル開発

docker composeを使った起動（ファイル同期 + ホットリロード）

```bash
docker compose up watch
```

アプリにアクセス

http://localhost:8080/

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