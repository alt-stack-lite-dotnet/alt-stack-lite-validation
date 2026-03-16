# Публикация пакетов на NuGet.org

## Что нужно один раз

1. **API-ключ NuGet**
   - Зайди на [nuget.org → API Keys](https://www.nuget.org/account/apikeys).
   - **Create** → имя (например `GitHub`), **Push** (push new packages and versions). Скопируй ключ.

2. **Секрет в GitHub**
   - Репозиторий → **Settings** → **Secrets and variables** → **Actions**.
   - **New repository secret**: имя **`NUGET_API_KEY`**, значение — ключ из шага 1.

После этого пакеты будут выкладываться автоматически при пуше тега.

## Как выложить новую версию

1. Обнови версию в **`Directory.Build.props`** (например `0.2.0`).
2. Закоммить и запушь изменения.
3. Создай и запушь тег (версия без `v` или с `v` — в пакет попадёт без `v`):

   ```bash
   git tag v0.2.0
   git push origin v0.2.0
   ```

4. В **Actions** запустится workflow: сборка → тесты → pack → push на nuget.org.

Артефакт с `.nupkg` всегда сохраняется в run; на nuget.org пакеты появятся только при заданном `NUGET_API_KEY`.
