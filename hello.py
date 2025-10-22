#!/usr/bin/python3
print('Hello world')

import psutil

# ���o CPU �ϥβv (�C���s�@��)
cpu_percent = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_percent}%")

# ���o�O�����T
mem = psutil.virtual_memory()
print(f"Total Memory: {mem.total / (1024**3):.2f} GB")
print(f"Used Memory: {mem.used / (1024**3):.2f} GB")
print(f"Memory Usage: {mem.percent}%")

# ���o�ϺШϥΪ��p (�ڥؿ�)
disk = psutil.disk_usage('/')
print(f"Total Disk Space: {disk.total / (1024**3):.2f} GB")
print(f"Used Disk Space: {disk.used / (1024**3):.2f} GB")
print(f"Disk Usage: {disk.percent}%")
