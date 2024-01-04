#!/bin/bash
while IFS="," read -r col1 col2 col3
do
  
  echo "My Name is $col1 ,Place is $col2 and Value is $col3"
  
done < p1.csv
