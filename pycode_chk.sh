#!/bin/bash
echo "Warning: Make sure to have pycodestyle installed before starting the check"
read -t 5 -r -p "Do you have pycodestyle installed (y/n) - 5 sec ? " resp
if [ "$resp" = "y" ] || [ "$resp" = "" ]; then
	printf "\nStart checking:\n\n"
	find . -type f -name "*.py" -execdir pycodestyle -v {} \;
	printf "\nChecking complete :)."
else
	echo "Exiting."
fi
