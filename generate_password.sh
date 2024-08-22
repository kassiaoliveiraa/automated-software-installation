#!/bin/bash
charset='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
password=""
for i in {1..14}; do
  rand=$(( RANDOM % ${#charset} ))
  password="${password}${charset:$rand:1}"
done
echo "$password" > password.txt