#!/bin/bash


aws ecr get-login-password --region cn-northwest-1 | docker login --username AWS --password-stdin 477069922492.dkr.ecr.cn-northwest-1.amazonaws.com.cn

docker build -t api-test-framework .

docker tag api-test-framework:latest 477069922492.dkr.ecr.cn-northwest-1.amazonaws.com.cn/api-test-framework:latest

docker push 477069922492.dkr.ecr.cn-northwest-1.amazonaws.com.cn/api-test-framework:latest
