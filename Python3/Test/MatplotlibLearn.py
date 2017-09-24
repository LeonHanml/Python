import re
pattern = re.compile('||show::goodsstore::[1-9]\d*::\d::[a-z]+||')
str = u'||show::goodsstore::91963::0::wap||dd'
print(pattern)
print(pattern.search(str))