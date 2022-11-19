import requests
import re
import csv


url = "https://spec.org/jbb2015/results/jbb2015multijvm.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}
res = requests.get(url, headers=headers)
restext = res.text

obj1 = re.compile(r'<th class="result.metric.critical-jOPS">critical-jOPS</th>.*?<tbody>(?P<TableList>.*?)</tbody>', re.S)
obj2 = re.compile(r'<tr.*?'
                  r'<td class="test.testedBy">(?P<TesterName>.*?)</td>.*?'
                  r'<td class="product.SUT.hw.system.hw_1.name">(?P<SystemName>.*?)<br />.*?'
                  r'<td class="product.SUT.sw.jvm.jvm_1.name">(?P<JVMName>.*?)</td>.*?'
                  r'<td class="product.SUT.sw.jvm.jvm_1.version">(?P<JVMVersion>.*?)</td>.*?'
                  r'<td class="result.metric.max-jOPS">(?P<max_jOPS>.*?)</td>.*?'
                  r'<td class="result.metric.critical-jOPS">(?P<critical_jOP>.*?)</td>.*?', re.S)

result1 = obj1.finditer(restext)
f = open("Data/jbb2015-MultiJVM.csv", mode="w", newline="")
csvwriter = csv.writer(f)
csvwriter.writerow(['TestSponsor', 'SystemName', 'JVMName', 'JVMVersion', 'max-jOPS', 'critical-jOPS'])

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




