#!/usr/bin/env bash

set -e
shopt -s extglob

function is_debug {
  local args=$@
  if [[ $args == "d" ]]; then
    echo 1
  else
    echo 0
  fi
}

function log {
  (>&2 echo "$@")
}

check=1
debug=$(is_debug $1)
function run {
  local cmd="$@"
  log
  log "#################################"
  log $cmd
  log "#################################"
  if [[ $debug -ne 1 ]]; then
    eval $cmd
    if [ $check -ne 0 -a $? -ne 0 ]; then
      log "Command failed!"
      exit 1
    fi
  fi
}
