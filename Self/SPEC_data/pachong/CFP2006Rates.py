import requests
import re
import csv

url = "https://spec.org/cpu2006/results/rfp2006.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}
res = requests.get(url, headers=headers, stream=True)
restext = res.text

obj1 = re.compile('<th class="peakmean">Peak</th>.*?<tbody>(?P<TableList>.*?)</tbody>', re.S)
obj2 = re.compile('<tr.*?'
                  '<td class="test_sponsor">(?P<TestSponsor>.*?)</td>.*?'
                  '<td class="hw_model">(?P<SystemName>.*?)<br />.*?'
                  '<td class="base_copies">(?P<BaseCopies>.*?)</td>.*?'
                  '<td class="hw_ncores">(?P<EnCores>.*?)</td>.*?'
                  '<td class="hw_nchips">(?P<EnChips>.*?)</td>.*?'
                  '<td class="hw_ncoresperchip">(?P<Cores>.*?)</td>.*?'
                  '<td class="hw_nthreadspercore">(?P<Threads>.*?)</td>.*?'
                  '<td class="basemean">(?P<Base>.*?)</td>.*?'
                  '<td class="peakmean">(?P<Peak>.*?)</td>.*?', re.S)
result1 = obj1.finditer(restext)

f = open("Data/CFP2006Rates.csv", mode="w", newline="")

csvwriter = csv.writer(f)
csvwriter.writerow(['TestSponsor', 'SystemName', 'BaseCopies', 'EnabledCores', 'EnabledChips', 'Cores/Chips', 'Threads/Core', 'Base', 'Peak'])

for i in result1:
    result2 = i.group("TableList")
    result = obj2.finditer(result2)
    for j in result:
        dic = j.groupdict()
        csvwriter.writerow(dic.values())

res.close()
print("over")

