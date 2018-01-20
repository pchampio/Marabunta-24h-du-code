#!/bin/bash

# Of course, we need to compile python!

i=1
sp="⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
echo -n ' '
for t in {1..30}
do
	printf "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b ${sp:i++%${#sp}:1} Compiling python..."
	sleep 0.1
done

echo "Done !"

