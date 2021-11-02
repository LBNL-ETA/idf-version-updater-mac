#!/bin/sh
./Transition-V9-2-0-to-V9-3-0 $1
mv $1 $3
mv $2 $1
./Transition-V9-3-0-to-V9-4-0 $1
mv $2 $1
./Transition-V9-4-0-to-V9-5-0 $1
mv $2 $1