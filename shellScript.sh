#!/bin/bash
ps aux --sort=-pcpu | head -10 > process.txt
for i in {1..10}
do
	mkdir "dir$i"
	awk "NR==$i " process.txt > dir$i/file$i
done
rm "process.txt"