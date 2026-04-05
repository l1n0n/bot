@echo off
echo ========================================
echo Деплой бота на ВМ (10.93.25.181)
echo ========================================
echo.

echo Шаг 1: Копирование файлов на сервер...
scp work.py requirements.txt .env bot.service docker-compose.yml Dockerfile docker-compose.yml operator@10.93.25.181:~/bot/
if errorlevel 1 (
    echo Ошибка копирования файлов!
    pause
    exit /b 1
)

echo.
echo Шаг 2: Установка systemd сервиса...
ssh operator@10.93.25.181 "sudo cp ~/bot/bot.service /etc/systemd/system/bot.service && sudo systemctl daemon-reload && echo 'Сервис установлен'"

echo.
echo Шаг 3: Запуск бота...
ssh operator@10.93.25.181 "sudo systemctl enable bot && sudo systemctl start bot && echo 'Бот запущен'"

echo.
echo Шаг 4: Проверка статуса...
ssh operator@10.93.25.181 "sudo systemctl status bot --no-pager"

echo.
echo ========================================
echo Готово!
echo ========================================
pause
