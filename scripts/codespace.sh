#!/usr/bin/env bash

# set -x
# yarn add commitizen --dev
# npx commitizen init cz-conventional-changelog --save-dev --save-exact

set -eo pipefail

fmt_lib=scripts/lib/fmt.sh

source "${fmt_lib}"

function export() {
  local name
  if [[ -z "${CONDA_DEFAULT_ENV}" ]]; then
    lib::fmt::errorMessage "Please activate the conda environment first."
    return 1
  fi
  lib::fmt::infoMessage "Please enter the name of the conda environment: "
  read -r name
  lib::fmt::infoMessage "Exporting conda environment..."
  conda env export --no-builds | grep -v "prefix:" > environment.yml
  echo
  sed -i "s/^name: .*$/name: ${name}/" environment.yml
  lib::fmt::succeedMessage "Conda environment exported successfully."
  echo
  return 0
}

function pkg_install() {
  yarn install
  npm list
}

function husky_install() {
  npx husky init
}

function init() {
  yarn install
  npx husky init
  conda env create -f environment.yml --prefix ./.conda
  #conda activate ./.conda
}

function hook() {
  cat << EOF > .husky/pre-commit
gitleaks git . --verbose
npx lint-staged
EOF
  gitmoji init
}

function __main__() {
  case "${1}" in
    "init")
      init
      ;;
    "pre-commit")
      pre-commit
      ;;
    "commit-msg")
      commit-msg
      ;;
    "export")
      export
      ;;
  esac

}

__main__ "${@}"
