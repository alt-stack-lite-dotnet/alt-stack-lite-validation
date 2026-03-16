#!/usr/bin/env bash
# Установка зависимостей: mise (Python + .NET), venv, pre-commit, dotnet tools.
# Запуск из корня репо: ./install.sh

set -e
cd "$(git rev-parse --show-toplevel 2>/dev/null || echo .)"

echo "==> Lite.Validation: установка зависимостей"

if ! command -v mise &>/dev/null; then
  echo "mise не найден. Установите: https://mise.jdx.dev/getting-started.html"
  echo "  curl https://mise.run | sh"
  exit 1
fi

echo "==> mise install (Python + .NET)"
mise install

echo "==> Python venv и pre-commit"
if [[ ! -d .venv ]]; then
  python3 -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate
pip install -q -r requirements.txt
pre-commit install --install-hooks
pre-commit install --hook-type pre-push --install-hooks
echo "Pre-commit: pre-commit и pre-push хуки установлены."

echo "==> dotnet tool restore"
dotnet tool restore

echo ""
echo "Готово. Активируйте venv: source .venv/bin/activate"
