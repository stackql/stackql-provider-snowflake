PROVIDER_REGISTRY_ROOT_DIR="$(pwd)"
REG='{"url": "file://'${PROVIDER_REGISTRY_ROOT_DIR}/providers'", "localDocRoot": "'${PROVIDER_REGISTRY_ROOT_DIR}/providers'", "verifyConfig": {"nopVerify": true}}'

# start server if not running
echo "checking if server is running"
if [ -z "$(ps | grep stackql)" ]; then
    echo "starting server with registry: $REG"
    nohup ./stackql -v --registry="${REG}" --pgsrv.port=5444 srv &
    sleep 5
else
    echo "server is already running"
fi