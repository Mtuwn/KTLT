import os
import psutil

#psutil.getloadavg() trả về 3 giá trị tải trong vòng 1p, 5p và 15p
load1, load5, load15 = psutil.getloadavg()
# Lấy giá trị tải trung bình trong 15 phút gần nhất chia cho số cpu
cpu_usage = (load15/os.cpu_count())*100

print("The CPU usage is: ", cpu_usage)