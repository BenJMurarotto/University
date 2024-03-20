#!/bin/bash

echo "Type a number to be added!"
read number_1
echo "Type a second number to be added!"
read number_2
sum=$((number_1 + number_2))
echo "Beep boop.... computing....."
sleep 3
echo "I believe this is the correct answer ->" $sum

