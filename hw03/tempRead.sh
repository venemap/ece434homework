#!/bin/sh
temp=`i2cget -y 2 0x4a 0` # take in temp from i2c
temp=$(($temp *1)) #convert to decimal
temp=`echo "scale=3; 
var1 = ($temp * 1.8) + 32;
var1 " \
| bc` #convert celsius to farenheit


echo Temperature is $temp degrees farenheit