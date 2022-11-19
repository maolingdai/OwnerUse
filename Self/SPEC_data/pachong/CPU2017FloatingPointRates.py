import requests
import re
import csv


url = "https://spec.org/cpu2017/results/rfp2017.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}

res = requests.get(url=url, headers=headers)
restext = res.text
obj1 = re.compile(r'<th class="peakenergymean">Peak</th>.*?<tbody>(?P<TableList>.*?)</tbody>', re.S)
obj2 = re.compile(r'<tr.*?'
                  r'<td class="test_sponsor">(?P<test_sponsor>.*?)</td>.*?'
                  r'<td class="hw_model">(?P<hw_model>.*?)<br />.*?'
                  r'<td class="base_copies">(?P<base_copies>.*?)</td>.*?'
                  r'<td class="hw_ncores">(?P<hw_ncores>.*?)</td>.*?'
                  r'<td class="hw_nchips">(?P<hw_nchips>.*?)</td>.*?'
                  r'<td class="hw_nthreadspercore">(?P<hw_nthreadspercore>.*?)</td>.*?'
                  r'<td class="basemean">(?P<basemean>.*?)</td>.*?'
                  r'<td class="peakmean">(?P<peakmean>.*?)</td>.*?'
                  r'<td class="baseenergymean">(?P<baseenergymean>.*?)</td>.*?'
                  r'<td class="peakenergymean">(?P<peakenergymean>.*?)</td>.*?', re.S)

result1 = obj1.finditer(restext)
f = open("Data/CPU2017 Floating Point Rates.csv", mode="w", newline="")
csvwrite = csv.writer(f)
csvwrite.writerow(['TestSponsor', 'SystemName', 'BaseCopies', 'EnabledCores', 'EnabledChips', 'Threads/Core', 'Base', 'Peak', 'EnergyBase','EnergyPeak'])

for i in result1:
    result2 = i.group('TableList')
    # print(i.group('TableList'))
    result = obj2.finditer(result2)
    for j in result:
        dic = j.groupdict()
        csvwrite.writerow(dic.values())

res.close()
print("over")

