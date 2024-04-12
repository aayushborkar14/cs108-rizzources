#!/usr/bin/env bash

X=4

if [ $X -lt 7 ]; then
	echo "$X is less than 7"
fi

#exit 0

cd demo
for dir in code doc anotherdir 
do
	if [ -d "$dir" ]; then
		echo "$dir already exists"
	else
		mkdir "$dir"
	fi
done
#exit 0

echo "Please enter your age:"
read age

# Check if age is less than 18
if [ "$age" -lt 18 ]; then
    echo "You are a minor."
# Check if age is between 18 and 24
elif [ "$age" -ge 18 ] && [ "$age" -le 24 ]; then
    echo "You are a young adult."
# Check if age is between 25 and 64
elif [ "$age" -ge 25 ] && [ "$age" -le 64 ]; then
    echo "You are an adult."
# If none of the above conditions are met, assume the age is 65 or older
else
    echo "You are a senior citizen."
fi



X=10

while [ $X -ge 0 ] ; do
        let X=X-1
        echo $X
done
