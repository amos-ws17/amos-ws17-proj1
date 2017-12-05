#!/bin/bash

echo " http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5022/bot/default2/execute?query=hey"
curl -X POST http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5022/bot/default2/execute?query=hey

echo "http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5012/bot/default2/execute?query=can20%you20%recommend20%me20%a20%monument20%in20%berlin?"
curl -X POST http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5022/bot/default2/execute?query=can20%you20%recommend20%me20%a20%monument20%in20%berlin?

curl -X POST http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5022/bot/default2/execute?query=Berlin

echo "http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5012/bot/default1/execute?query=Bye"
curl -X POST http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5022/bot/default2/execute?query=Bye
