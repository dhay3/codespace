#!/usr/bin/env bash

set -xeo pipefail

function init() {
  yarn install
  npx husky init
}

function pre-commit() {
  cat << EOF > .husky/pre-commit
gitleaks git . --verbose
npx lint-staged
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
