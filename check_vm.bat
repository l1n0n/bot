@echo off
echo Подключение к ВМ и проверка бота...
echo.
ssh operator@10.93.25.181 "echo '=== systemd сервис бота ==='; systemctl status bot.service 2>/dev/null || echo 'Сервис не найден'; echo ''; echo '=== Docker контейнеры ==='; docker ps -a 2>/dev/null || echo 'Docker не запущен'; echo ''; echo '=== Python процессы ==='; pgrep -a python || echo 'Python не запущен'; echo ''; echo '=== Логи бота (последние 20 строк) ==='; journalctl -u bot.service --no-pager -n 20 2>/dev/null || echo 'Логи systemd недоступны'"
