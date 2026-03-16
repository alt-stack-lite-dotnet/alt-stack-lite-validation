#!/usr/bin/env python3
"""
Pre-commit: формат (CSharpier) и сборка.
Запускается из корня репозитория.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(cmd: list[str], cwd: Path | None = None) -> int:
    return subprocess.call(cmd, cwd=cwd or ROOT, shell=(sys.platform == "win32"))


def main() -> int:
    # 1) Восстановить dotnet tools (csharpier)
    if run(["dotnet", "tool", "restore"], cwd=ROOT) != 0:
        print("run_lint: dotnet tool restore failed")
        return 1
    # 2) Форматировать C#
    if run(["dotnet", "csharpier", "."], cwd=ROOT) != 0:
        print("run_lint: dotnet csharpier failed")
        return 1
    # 3) Сборка (в т.ч. Roslynator)
    if run(["dotnet", "build", "Lite.Validation.sln", "-c", "Release", "--no-restore"], cwd=ROOT) != 0:
        print("run_lint: dotnet build failed")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
