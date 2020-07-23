#!/bin/bash

project_name=DustFlight_Studio
config_file_path=../Supervisor/supervisor_app.conf

function start_application() {
    supervisor_stack_option_connect
    echo "[CONSOLE] Running Function => [supervisor_stack_option_connect]"
    supervisor_stack_service_running
    echo "[CONSOLE] Running Function => [supervisor_stack_service_running]"
}

function supervisor_stack_option_connect() {
    supervisord -c ${config_file_path}
    echo "[CONSOLE] Optional File Connection Successfully! "
}

function supervisor_stack_service_running() {
    supervisorctl start ${project_name}
    echo "[CONSOLE] Supervisor Stack Service Running Successfully! "
}

function main() {
    echo "======================[PROCESSING]======================"
    start_application
    echo "======================[PROCESSING]======================"
}

main
