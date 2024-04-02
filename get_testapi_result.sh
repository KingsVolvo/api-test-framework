#!/bin/bash

host_dir=${1:-/var/logs}

# 获取容器 ID
containerid=$(docker ps -a | grep run-api-test-img | awk 'NR==1 {print $1}')

# 打印容器 ID
echo $containerid
docker cp $containerid:/app/test-reports/ ${host_dir}
