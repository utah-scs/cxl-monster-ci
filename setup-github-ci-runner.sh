#!/bin/bash

PROJDIR=/proj/sandstorm-PG0

mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux-x64-2.304.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.304.0/actions-runner-linux-x64-2.304.0.tar.gz
tar xzf ./actions-runner-linux-x64-2.304.0.tar.gz
token=$(cat $PROJDIR/.github-ci-runner-token)
./config.sh --url https://github.com/utah-scs/monster --token $token
