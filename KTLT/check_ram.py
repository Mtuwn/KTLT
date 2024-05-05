import psutil

print('Ram memory % used: ',psutil.virtual_memory().percent)
print('Ram used (GB): ', psutil.virtual_memory().used/ (1024 ** 3))