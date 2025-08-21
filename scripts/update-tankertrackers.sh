#!/bin/sh

echo "# TankerTrackers blacklisted vessels" > ../src/sanctions/tankertrackers.imo

curl https://tankertrackers.com/api/sanctioned/v1 | jq -r '.data[] | [.imo, (.sanctions | keys | join(" ")) ] | @csv' | tr '"' ' ' | tr ',' ' ' | sort >> ../src/sanctions/tankertrackers.imo