import pythonping

a = pythonping.ping(target='192.168.0.1',count=1)
print(a)
print(type(a))
a = str(a)
print(a)
print(type(a))
pos1 = a.find('in ') + 3
pos2 = a.find('ms')
print(a[pos1:pos2])
