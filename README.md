# Git Basics Lab Project

## Описание
Этот проект создан в рамках лабораторной работы по Git. Содержит примеры Python кода и скриптов.

## Файлы в проекте:
- `backup.sh` - скрипт для создания резервных копий
- `app.py` - главное приложение
- `utils.py` - вспомогательные функции
- `config.py` - конфигурация приложения
- `feature_x.py` - реализация функционала X
- `feature_y.py` - реализация функционала Y
- `.gitignore` - список игнорируемых файлов
- `README.md` - этот файл

## Использование
```bash
# Запуск главного приложения
python3 app.py

# Запуск отдельных функций
python3 utils.py
python3 config.py
python3 feature_x.py
python3 feature_y.py

# Использование скрипта бэкапа
./backup.sh /path/to/source /path/to/backup


## 8. Обнови backup.sh (финальная версия):

```bash
cat > backup.sh << 'EOF'
#!/bin/bash
# Simple backup script
# Usage: ./backup.sh <source_directory> <backup_directory> [compression_level]

SOURCE_DIR=${1:-.}
BACKUP_DIR=${2:-./backup}
COMPRESSION_LEVEL=${3:-6}
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="backup_${TIMESTAMP}.tar.gz"

echo "========================================="
echo "Backup Script v1.0"
echo "========================================="
echo "Source: $SOURCE_DIR"
echo "Backup destination: $BACKUP_DIR"
echo "Compression level: $COMPRESSION_LEVEL"
echo "Timestamp: $TIMESTAMP"
echo "========================================="

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Create tar archive with specified compression level
echo "Creating archive..."
tar -czf "${BACKUP_DIR}/${BACKUP_FILE}" --directory="$SOURCE_DIR" .

if [ $? -eq 0 ]; then
    echo "✓ Backup completed successfully!"
    echo "Backup file: ${BACKUP_DIR}/${BACKUP_FILE}"
    echo "Backup size: $(du -h "${BACKUP_DIR}/${BACKUP_FILE}" | cut -f1)"
else
    echo "✗ Backup failed!"
    exit 1
fi

# Clean old backups (keep last 5)
echo "Cleaning old backups..."
cd "$BACKUP_DIR"
ls -t backup_*.tar.gz 2>/dev/null | tail -n +6 | xargs -r rm
echo "✓ Kept last 5 backups"

# Summary
echo "========================================="
echo "Backup completed at $(date)"
echo "========================================="

# Optional email notification (commented out by default)
# send_notification() {
#     echo "Backup completed at $(date)" | mail -s "Backup Status: $BACKUP_FILE" griggirs@gmail.com
# }
# send_notification
