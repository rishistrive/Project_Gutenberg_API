#!/usr/bin/env bash

# Use this script to wait for a service to be ready.
# Usage: wait-for-it.sh host:port [-t timeout] [-- command args]
# Example: wait-for-it.sh db:5432 -- echo "DB is ready"

TIMEOUT=15
while [ "$#" -gt 0 ]; do
    case "$1" in
        -t) TIMEOUT="$2"; shift 2 ;;
        --) shift; break ;;
        *) HOST="$1"; shift ;;
    esac
done

start_ts=$(date +%s)
while true; do
    nc -z ${HOST%:*} ${HOST#*:} && break
    sleep 1
    end_ts=$(date +%s)
    if [ "$((end_ts - start_ts))" -ge "$TIMEOUT" ]; then
        echo "Timeout waiting for $HOST"
        exit 1
    fi
done

echo "$HOST is up"
exec "$@"
