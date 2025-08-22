#!/bin/sh

echo "# [TankerTrackers.com](https://tankertrackers.com/report/sanctioned) Officially Blacklisted Tankers" > ../src/sanctions/tankertrackers.imo

curl https://tankertrackers.com/api/sanctioned/v1 \
    | jq -r '.data[] | [.imo, (.sanctions | keys | join(" ")) ] | @csv' \
    | tr '"' ' ' | tr ',' ' ' \
    | sort >> ../src/sanctions/tankertrackers.imo