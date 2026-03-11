#!/bin/bash
# Simple backup script
# Usage: ./backup.sh <source_directory> <backup_directory>

SOURCE_DIR=${1:-.}
BACKUP_DIR=${2:-./backup}
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="backup_${TIMESTAMP}.tar.gz"

echo "Starting backup process..."
echo "Source: $SOURCE_DIR"
echo "Backup destination: $BACKUP_DIR"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Create tar archive
tar -czf "${BACKUP_DIR}/${BACKUP_FILE}" "$SOURCE_DIR"

if [ $? -eq 0 ]; then
    echo "Backup completed successfully!"
    echo "Backup file: ${BACKUP_DIR}/${BACKUP_FILE}"
    echo "Backup size: $(du -h "${BACKUP_DIR}/${BACKUP_FILE}" | cut -f1)"
else
    echo "Backup failed!"
    exit 1
fi

# Clean old backups (keep last 5)
cd "$BACKUP_DIR"
ls -t backup_*.tar.gz 2>/dev/null | tail -n +6 | xargs -r rm
echo "Cleaned old backups, kept last 5"

# This line contains a syntax error
if [ -z "$1" ]  # Missing 'then'
    echo "No source directory specified, using current directory"
fi
