#!/bin/sh
kill -1 `ps -ae -o comm,pid | grep "^python" | tr -s ' ' | cut -f2 -d' '`
