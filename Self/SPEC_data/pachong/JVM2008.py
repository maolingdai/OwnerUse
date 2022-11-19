import requests
import re
import csv


url = "https://spec.org/jvm2008/results/jvm2008.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}
res = requests.get(url, headers=headers)
restext = res.text

obj1 = re.compile(r'<th class="result_score_peak">Peak</th>.*?<tbody>(?P<TableList>.*?)</tbody>', re.S)
obj2 = re.compile(r'<tr.*?'
                  r'<td class="run_submitter">(?P<Tester>.*?)</td>.*?'
                  r'<td class="hw_model">(?P<SystemName>.*?)<br />.*?'
                  r'<td class="hw_number_of_cores">(?P<Cores>.*?)</td>.*?'
                  r'<td class="hw_number_of_chips">(?P<Chips>.*?)</td>.*?'
                  r'<td class="hw_logical_cpus">(?P<HWThreads>.*?)</td>.*?'
                  r'<td class="hw_threads_per_core">(?P<ThreadsCore>.*?)</td>.*?'
                  r'<td class="jvm_name">(?P<JVMName>.*?)</td>.*?'
                  r'<td class="jvm_version">(?P<JVMVersion>.*?)</td>.*?'
                  r'<td class="result_score_base">(?P<Base>.*?)</td>.*?'
                  r'<td class="result_score_peak">(?P<Peak>.*?)</td>.*?', re.S)

result1 = obj1.finditer(restext)
f = open("Data/jvm2018.csv", mode="w", newline="")
csvwriter = csv.writer(f)
csvwriter.writerow(['Tester', 'SystemName', 'Cores', 'Chips', 'HWthreads', 'Threads/Core', 'JVMName', 'JVMVersion', 'Base', 'Peak'])

# for i in result1:
#     print(i.group("TableList"))
for i in result1:
    result2 = i.group("TableList")
    result = obj2.finditer(result2)
    for j in result:
        dic = j.groupdict()
        csvwriter.writerow(dic.values())

res.close()
print("over")




