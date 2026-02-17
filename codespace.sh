#!/usr/bin/env bash

set -xeo pipefail

function init() {
  npm install --save-dev
  npx husky init
}

function pre-commit() {
  cat << EOF > .husky/pre-commit
gitleaks git . --verbose
EOF
}

function commit-msg() {
  gitmoji init
}

function __main__() {
  init
  pre-commit
  commit-msg
}

__main__ "${@}"
