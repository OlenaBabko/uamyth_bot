#!/bin/bash


if [ -z "${CI_REGISTRY_USER}" ]; then
    local_analysis_script="$(dirname ${0})/.pyconf/analysis/analysis.sh"
    if [ ! -f "${local_analysis_script}" ]; then
        echo "pyconf project was not found, please run 'git clone ssh://git@gitlab.maklai.dev:8999/pytools/pyconf.git .pyconf' and try again"
        exit 1
    fi
    echo "Running default analysis..."
    bash -c "${local_analysis_script}"
else
    GITLAB_URL="https://${CI_REGISTRY_USER}:${CI_BUILD_TOKEN}@gitlab.maklai.dev"
    echo "Running default analysis..."
    curl --sSL ${GITLAB_URL}/pytools/pyconf/-/raw/master/analysis/analysis.sh | bash -s -- ${GITLAB_URL}
fi
