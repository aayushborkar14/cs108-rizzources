#!/bin/bash

echo 1 5*2+1
num=5*2+1
echo 2 $num

#Two formats, $((expression)) and $[expression]
echo 3 $((5 * 2 + 1))
echo 4 $((5 * 2 + 1))
let num=5*2+1
echo 5 $num
declare -i result
result=5*2+1
echo 6 $result

#floating point needs use of bc
echo 7 $((3 / 4))
echo -n "8 "
echo "3/4" | bc -l
