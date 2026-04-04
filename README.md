# Telegram Bot — Деплой на ВМ

## Быстрый запуск

### Через Docker (рекомендуется)

1. Убедитесь, что Docker установлен:
   ```bash
   docker --version
   ```

2. Настройте токен в `.env`:
   ```env
   BOT_TOKEN=ваш_токен_от_BotFather
   ```

3. Запустите:
   ```bash
   docker compose up -d --build
   ```

4. Посмотреть логи:
   ```bash
   docker compose logs -f bot
   ```

5. Остановить:
   ```bash
   docker compose down
   ```

---

### Без Docker

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

2. Запустите бота:
   ```bash
   python work.py
   ```

---

### systemd сервис (для постоянного запуска без Docker)

1. Скопируйте `bot.service` в `/etc/systemd/system/`:
   ```bash
   sudo cp bot.service /etc/systemd/system/bot.service
   ```

2. Отредактируйте путь в `bot.service` (замените `/path/to/bot` на реальный).

3. Включите и запустите:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable bot
   sudo systemctl start bot
   ```

4. Проверьте статус:
   ```bash
   sudo systemctl status bot
   ```
