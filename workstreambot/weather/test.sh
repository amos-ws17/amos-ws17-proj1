#!/bin/bash

echo " http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5012/bot/default2/execute?query=hey"
curl -X POST http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5012/bot/default5/execute?query=hey

echo "http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5012/bot/default2/execute?query=What%20will%20the%20weather%20be%20in%20Berlin?"
curl -X POST http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5012/bot/default5/execute?query=What%20will%20the%20weather%20be%20in%20Berlin?

echo "http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5012/bot/default2/execute?query=Thanks20%Bye"
curl -X POST http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5012/bot/default5/execute?query=Bye
