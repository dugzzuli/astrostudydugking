#!/bin/bash

# 遍历备份目录下的所有子目录
for dir in /home/mpilot/1m6/backup_reception_0330/*/
do
    # 获取目录名（如“20221216”）
    dirname=${dir%*/}
    dirname=${dirname##*/}

    # 创建接收目录（如果不存在）
    if [ ! -d "/home/mpilot/1m6/reception/$dirname" ]
    then
        mkdir "/home/mpilot/1m6/reception/$dirname"
        echo "创建目录：/home/mpilot/1m6/reception/$dirname"
    fi

    # 检查是否存在cal目录，如果存在则复制到接收目录下
    if [ -d "${dir}cal" ]
    then
        cp -r "${dir}cal" "/home/mpilot/1m6/reception/$dirname/"
        echo "复制成功：${dir}cal => /home/mpilot/1m6/reception/$dirname/"
    else
        echo "错误：$dir 中不存在cal目录"
    fi
done