#!/bin/bash

nexttime() {
    if [[ $(date -d "now" "+%s") -ge $(date -d "$1" "+%s") ]] ; then
        date -d "tomorrow $1" "+%s"
    else
        date -d "$1" "+%s"
    fi
}

aoc_challenge_publish_time="$(nexttime '00:00 EST')"

aocdl -output "advent-of-code-{{.Year}}/Inputs/$(date -d @$aoc_challenge_publish_time +%d).txt" -wait
