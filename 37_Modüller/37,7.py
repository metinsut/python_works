import os,sys,random,subprocess

set_os=set(dir(os))
set_sys=set(dir(sys))
set_random=set(dir(random))
set_subprocess=set(dir(subprocess))


print(set_os&set_sys&set_random&set_subprocess)




modüller=["os","sys","random"]

def kesişim_bul(modüller):
    kümeler=[set(dir(__import__(modül))) for modül in modüller]
    return set.intersection(*kümeler)
print(kesişim_bul(modüller))

__import__("subprocess")
print(modüller)
