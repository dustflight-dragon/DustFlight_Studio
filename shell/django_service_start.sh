#!/bin/bash

django_service_path=../

function start_application() {
    django_service_start
    echo "[CONSOLE] Running => [django_service_start]"
}

function export_env_path() {
    export ${django_service_path}
    echo "[EXPORT] Running Successfully => [${django_service_path}]"
}

function django_service_start() {
    cd ${django_service_path}
    python manager.py runserver 127.0.0.1:9001
}

function main() {
    echo "======================[PROCESSING]======================"
    start_application
    echo "======================[PROCESSING]======================"
}

main
