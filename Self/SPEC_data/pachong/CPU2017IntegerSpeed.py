import requests
import re
import csv

url = "https://spec.org/cpu2017/results/cint2017.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}

# 重写封装参数
param = {
    "conf": "cint2017",
    "op": "fetch",
    "field": "CACHE1"
}
res = requests.get(url=url, params=param, headers=headers)
res = res.text
# print(res.request.url)
# print(res)
# 正则表达式解析页面 获取内容
obj1 = re.compile(r'<th class="peakenergymean">Peak</th>.*?<tbody>(?P<TableList>.*?)</tbody>', re.S)
obj2 = re.compile(r'<tr.*?'
                  r'<td class="test_sponsor">(?P<test_sponsor>.*?)</td>.*?'
                  r'<td class="hw_model">(?P<hw_model>.*?)<br />.*?'
                  r'<td class="sw_parallel">(?P<sw_parallel>.*?)</td>.*?'
                  r'<td class="base_threads">(?P<base_threads>.*?)</td>.*?'
                  r'<td class="hw_ncores">(?P<hw_ncores>.*?)</td>.*?'
                  r'<td class="hw_nchips">(?P<hw_nchips>.*?)</td>.*?'
                  r'<td class="hw_nthreadspercore">(?P<hw_nthreadspercore>.*?)</td>.*?'
                  r'<td class="basemean">(?P<basemean>.*?)</td>.*?'
                  r'<td class="peakmean">(?P<peakmean>.*?)</td>.*?'
                  r'<td class="baseenergymean">(?P<baseenergymean>.*?)</td>.*?'
                  r'<td class="peakenergymean">(?P<peakenergymean>.*?)</td>.*?', re.S)

result1 = obj1.finditer(res)
# for i in result1:
#     print(i.group("TableList"))

# 把数据存入csv文件中
f = open("Data/CPU2017 Integer Speed Results.csv", mode="w", newline="")
csvwrite = csv.writer(f)
csvwrite.writerow(['TestSponsor', 'SystemName', 'Parallel', 'BaseCopies', 'EnabledCores', 'EnabledChips', 'Threads/Core', 'Base', 'Peak', 'EnergyBase', 'EnergyPeak'])

for it in result1:
    result = it.group("TableList")
    result2 = obj2.finditer(result)
    for itt in result2:
        # 把数据写入字典中
        dic = itt.groupdict()
        # dic['Baseline'] = dic['Baseline'].strip()
        csvwrite.writerow(dic.values())

print('over')

