#!/bin/bash

django_service_name=wsgi.py
django_service_path=../DustFlight_Studio

function start_application() {
    running_welcome_info
    echo "[CONSOLE] Running => [running_welcome_info]"
    gunicorn_pip_installer
    echo "[CONSOLE] Running => [gunicorn_pip_installer]"
    export_env_path
    echo "[CONSOLE] Running => [export_env_path]"
    gunicorn_stack_container_start
    echo "[CONSOLE] Running => [gunicorn_stack_container_start]"
}

function running_welcome_info() {
    echo "####################################################################"
    echo "--------------------------------------------------------------------"
    echo "#  Welcome to running DustFlight_Studio.wsgi Powered By Gunicorn ! #"
    echo "--------------------------------------------------------------------"
    echo "####################################################################"
}

function gunicorn_pip_installer() {
    pip install gunicorn --user
    echo "[GUNICORN] Running Successfully => [pip install gunicorn --user]"
}

function export_env_path() {
    export ${django_service_path}
    echo "[EXPORT] Running Successfully => [${django_service_path}]"
}

function gunicorn_stack_container_start() {
    cd ${django_service_path}
    gunicorn ${django_service_name}
}

function main() {
    echo "======================[PROCESSING]======================"
    start_application
    echo "======================[PROCESSING]======================"
}

main
