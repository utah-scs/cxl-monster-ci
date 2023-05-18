#!/bin/bash

set -e

REPO=https://github.com/utah-scs/monster
TOKEN_FILE=/proj/sandstorm-PG0/.github-ci-runner-token

cd /local
mkdir actions-runner
chmod 770 actions-runner
cd actions-runner
curl -o actions-runner-linux-x64-2.304.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.304.0/actions-runner-linux-x64-2.304.0.tar.gz
tar xzf ./actions-runner-linux-x64-2.304.0.tar.gz

token=$(cat $TOKEN_FILE)
./config.sh --url https://github.com/utah-scs/monster --token $token --unattended
sudo ./svc.sh install
sudo ./svc.sh start

