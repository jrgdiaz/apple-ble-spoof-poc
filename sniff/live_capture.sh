#!/bin/bash

while true; do

        #run sniff session for 30 seconds
        exec ./ble_sniff.py &
        PID=$!
        sleep 30
        echo "sending SIGINT to process $PID"
        kill -SIGINT $PID
        wait

done
