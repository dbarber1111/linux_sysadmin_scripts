#!/bin/bash
killall -s SIGTERM firefox; sleep 30
firefox -P "$USER" &
firefox -P "default settings" &