#!/bin/bash

echo "Iniciando configuracao de ambiente seguro"

sudo apt-get update -y

if: command -v python3 &> /dev/null
then
	echo "Python not found. Installing..."
	sudo apt-get install python3 -y
else
	echo "Python Already Installed."
fi


echo "Ready to run the Randon log generator"
