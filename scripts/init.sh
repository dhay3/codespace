#!/usr/bin/env bash

function init(){
  npm install --save-dev
  npx husky init
}

function pre-commit(){
  cat <<EOF > .husky/pre-commit
gitleaks dir . --verbose
EOF
}

function commit-msg(){
  gitmoji init
}

function __main__(){
  init
  pre-commit
  commit-msg
}

__main__ "${@}"
