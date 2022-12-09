# shellcheck disable=SC2034
# shellcheck disable=SC2006
SOURCE=`dirname "$0"`

. "$SOURCE"/../.env

BACKUP_FOLDER="$SOURCE"/../src/backups

if [ ! -d "$BACKUP_FOLDER" ]; then
  # shellcheck disable=SC2086
  mkdir $BACKUP_FOLDER
fi

case "$1" in
  --do-backup)
    # shellcheck disable=SC2046
    docker exec -t test-api pg_dumpall -c -U postgres | gzip > "$BACKUP_FOLDER"/backup.sql.gz
    ;;
  --do-reload)
    gunzip < "$BACKUP_FOLDER"/backup.sql.gz | docker exec -i test-api psql -U "$POSTGRES_USER" -d "$POSTGRES_NAME"
    ;;
esac
