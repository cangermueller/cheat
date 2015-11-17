#!/usr/bin/env bash

# cat <<- END
# test.sh [args]
  # -h|--help             Show help message
  # -i|--in_file file     Input file
# END

help="test.sh [args]\n
  -h|--help               Show help\n
  -i|--in_file in_file    Input file\n
"

while [ $# -gt 0 ]; do
  arg=$1
  case $arg in
    -h|--help)
      echo -e $help
      exit 0
      ;;
    -i|--in_file)
      shift
      in_file=$1
      ;;
    *)
      >&2 echo Unknown option!
      echo -e $help
      exit 1
      ;;
  esac
  shift
done

echo $in_file

