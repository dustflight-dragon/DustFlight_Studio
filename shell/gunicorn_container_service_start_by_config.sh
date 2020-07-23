#!/bin/bash

config_file_path=../Gunicorn/config.py
django_application_path=../DustFlight_Studio/wsgi.py
django_service_path=../

function start_application() {
    running_welcome_info
    echo "[CONSOLE] Running => [running_welcome_info]"
    pip_env_installer
    echo "[CONSOLE] Running => [pip_env_installer]"
    export_env_path
    echo "[CONSOLE] Running => [export_env_path]"
    gunicorn_stack_service_container_running
    echo "[CONSOLE] Running => [gunicorn_stack_service_container_running]"
}

function running_welcome_info() {
    echo "#################################################################"
    echo "#                                                               #"
    echo "#  Wlecome to running DustFlight_Studio.wsgi Powered By Gunicorn ! #"
    echo "#                                                               #"
    echo "#################################################################"
}

function pip_env_installer() {
    pip install gunicorn --user
    pip install greenlet --user
    pip install eventlet --user
    pip install gevent --user
}

function export_env_path() {
    export ${django_service_path}
    echo "[EXPORT] Running Successfully => [${django_service_path}]"
}

function gunicorn_stack_service_container_running() {
    # gunicorn --workers=4 --bind=127.0.0.1:8000 --worker-class=eventlet ${django_application_path}
    cd ${django_service_path}
    gunicorn --config=${config_file_path} --worker-class=eventlet ${django_application_path}
    echo "[GUNICORN] Running Successfully => [Gunicorn Engine Running]"
}

function main() {
    echo "======================[PROCESSING]======================"
    start_application
    echo "======================[PROCESSING]======================"
}

main
