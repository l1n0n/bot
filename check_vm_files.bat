@echo off
echo Проверка файлов бота на ВМ...
echo.
ssh operator@10.93.25.181 "echo '=== Файлы в ~/bot ==='; ls -la ~/bot/ 2>/dev/null || echo 'Папка ~/bot не найдена'; echo ''; echo '=== Docker установлен? ==='; docker --version 2>/dev/null || echo 'Docker не установлен'; echo ''; echo '=== Python3 установлен? ==='; python3 --version 2>/dev/null || echo 'Python3 не установлен'; echo ''; echo '=== Путь к рабочей директории ==='; pwd"
