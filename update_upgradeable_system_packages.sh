#!/bin/bash

# Automate system package updates

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get autoremove -y