#!/bin/bash
for i in {1..1000}
do
   curl "http://ratemyyogainstructor.com/instructors/00000$i.jpg"
done