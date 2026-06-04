#!/usr/bin/env bash

set -xeo pipefail

function init() {
  #  conda env export --no-builds | grep -v "prefix:" > environment.yml
  yarn install
  npx husky init
  conda env create -f environment.yml --prefix ./.conda
  conda activate ./.conda
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
