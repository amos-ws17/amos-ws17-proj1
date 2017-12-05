#!/bin/bash

echo " http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5032/bot/default2/execute?query=hey"
curl -X POST http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5032/bot/default10/execute?query=hey

echo "http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5032/bot/default2/execute?query=In%20Berlin?"
curl -X POST http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5032/bot/default10/execute?query=in%20berlin

echo "http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5032/bot/default1/execute?query=I20%would20%like20%to20%try20%some20%cheap20%mexican20%restaurant"
curl -X POST http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5032/bot/default10/execute?query=i20%want20%some20%cheap20%italian20%restaurant

echo "http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5032/bot/default2/execute?query=Bye"
curl -X POST http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5032/bot/default10/execute?query=Bye
