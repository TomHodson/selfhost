cd /home/tom/

miniflux_python_env/bin/python selfhost/scripts/miniflux_backup.py
docker exec postgres pg_dump -U miniflux -Fc miniflux > selfhost/backups/miniflux_backup.db
rclone copy --max-age 24h --no-traverse /home/tom/selfhost/backups gdrive:Applications/Selfhosted_backups