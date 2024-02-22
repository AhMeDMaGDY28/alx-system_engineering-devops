#!/usr/bin/env bash
# print "Best School" 10 times
i=1
while((i<11))
do
  if((i==4))
  then
  echo "bad luck"
  fi
  elif((i==8))
  then
	echo "good luck"
	fi
   
  echo "Best School"
  ((i++))
done