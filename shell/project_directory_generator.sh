#!/bin/bash

project_directory=/nfs/WymSword_Application/Python/Django_Application/

function start_application() {
    project_directory_generator
    echo "[CONSOLE] Running Function => [project_directory_generator] Successfully"
    project_directory_chmod
    echo "[CONSOLE] Running Function => [project_directory_chmod] Successfully"
}

function project_directory_generator() {
    mkdir -p ${project_directory}
    if [ ! $? -eq 0 ]; then
        echo "[DIRECTORY] Generator ${project_directory} Invalid"
    else
        echo "[DIRECTORY] Generator ${project_directory} Successfully"
    fi
}

function project_directory_chmod() {
    chmod -R 777 ${project_directory}
    if [ ! $? -eq 0 ]; then
        echo "[DIRECTORY] Chmod Generator ${project_directory} Invalid"
    else
        echo "[DIRECTORY] Chmod Generator ${project_directory} Successfully"
    fi
}

function main() {
    echo "======================[CONSOLE]======================"
    start_application
    echo "======================[CONSOLE]======================"
}

main
