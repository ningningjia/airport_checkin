#!/bin/bash


while true
do
    # 启动第一个 Python 脚本
    python ./stt/stt.py >> ./stt/checkin.log 2>&1

    # 启动第二个 Python 脚本
    python ./yiyo/yiyo.py >> ./yiyo/checkin.log 2>&1

    # 等待所有子进程结束
    wait
    
    # 休眠24小时
    sleep 24h
done
