kod_çözücüler = ['UTF-8', 'cp1254', 'latin-1', 'ASCII']

harf = 'İ'

for kç in kod_çözücüler:
    try:
        print("'{}' karakteri {} ile {} olarak "
              "ve {} sayısıyla temsil edilir.".format(harf, kç,
                                                      harf.encode(kç),
                                                      ord(harf)))
    except UnicodeEncodeError:
        print("'{}' karakteri {} ile temsil edilemez!".format(harf, kç))