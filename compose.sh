cd docker-compose
docker compose \
    -f miniflux.yml \
    -f portainer.yml \
    -f octoprint.yml \
    up -d