#!/usr/bin/env bash

set -e -o pipefail

KEYDIR=${1:-.}

error() {
  ( >&2 echo $@ )
}

LINE_VALIDATORS=()
LINE_VALIDATORS+=('key[[:space:]]+"[0-9a-f]{64}";')
LINE_VALIDATORS+=('remote[[:space:]]+((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):[0-9]+;')
LINE_VALIDATORS+=('remote[[:space:]]+(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))(:|([[:space:]]+port[[:space:]]+))[0-9]+;')
LINE_VALIDATORS+=('remote[[:space:]]+((ipv4|ipv6)[[:space:]]+)?"[0-9a-zA-Z.-]+"(:|([[:space:]]+port[[:space:]]+))[0-9]+;')

# Validate fastd key files
keycount=0
for file in "$KEYDIR"/*; do
  sed -E 's/^\s+//g;s/[[:space:]]+$//g;/^[[:space:]]*$/d' "$file" |\
  while read line; do
    valid=''
    # Simple comments are always ok
    echo "$line" | grep -q '^#.*' && continue
    for validator in "${LINE_VALIDATORS[@]}"; do
      echo "$line" | egrep -q "^${validator}([[:space:]]*#.*)?$" && {
        valid=yes
        break;
      }
    done
    if [ "$valid" != yes ]; then
      error "Key file '$file' is invalid"
      error "Offending line: '$line'"
      exit 1
    fi
  done
  keycount=$((keycount + 1))
done

echo "OK. $keycount keyfiles"
