#!/bin/bash

echo "Are you happy or sad?"
read happyOrSad
if [[ $happyOrSad == "sad" ]]
then 
	echo "How many days since you went for a walk last"
	read daysSinceWalk
	if (($daysSinceWalk>1))
	then
		echo "Go for a walk, you might feel better"
		exit
	fi
fi
echo "sorry idk how to help lol..."
