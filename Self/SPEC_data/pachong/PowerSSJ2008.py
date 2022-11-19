import requests
import re
import csv

url = "https://spec.org/power_ssj2008/results/power_ssj2008.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}

res = requests.get(url=url, headers=headers)
restext = res.text
obj1 = re.compile(r'<th class="submetric_power_10">avg. watts<br />@ active idle</th>.*?<tbody>(?P<TableList>.*?)</tbody>', re.S)
obj2 = re.compile(r'<tr.*?'
                  r'<td class="wkld_ssj_global_config_hw_vendor">(?P<TestSponsor>.*?)<.*?'
                  r'<td class="wkld_ssj_global_config_hw_model">(?P<SystemEnclosure>.*?)<br />.*?'
                  r'<td class="hwnodes">(?P<Nodes>.*?)</td>.*?'
                  r'<td class="wkld_ssj_global_config_sw_jvm_vendor">(?P<JVMVendor>.*?)</td>.*?'
                  r'<td class="wkld_ssj_global_config_hw_cpu">(?P<CPUDescription>.*?)</td>.*?'
                  r'<td class="wkld_ssj_global_config_hw_cpu_mhz">(?P<MHz>.*?)</td>.*?'
                  r'<td class="aggregate_config_cpu_chips">(?P<Chips>.*?)</td>.*?'
                  r'<td class="aggregate_config_cpu_cores">(?P<Cores>.*?)</td>.*?'
                  r'<td class="hwtotalthreads">(?P<totalthreads>.*?)</td>.*?'
                  r'<td class="aggregate_config_memory_gb">(?P<totalmemory>.*?)</td>.*?'
                  r'<td class="submetric_ssjops_0">(?P<ssjops>.*?)</td>.*?'
                  r'<td class="submetric_power_0">(?P<watts1>.*?)</td>.*?'
                  r'<td class="submetric_power_10">(?P<watts2>.*?)</td>.*?'
                  r'<td class="metric_performance_power_ratio">(?P<overall>.*?)</td>.*?', re.S)

result1 = obj1.finditer(restext)
f = open("Data/power_ssj2008.csv", mode="w", newline="", encoding='UTF-8')
csvwrite = csv.writer(f)
csvwrite.writerow(['Tester', 'SystemName', 'Nodes', 'JVMVendor', 'CPUDescription', 'MHz', 'Chips', 'Cores', 'TotalThreads', 'TotalMemory', 'SSJ', 'AVG', 'AVGidle', 'Overall'])


for i in result1:
    result2 = i.group('TableList')
    # print(i.group('TableList'))
    result = obj2.finditer(result2)
    for j in result:
        dic = j.groupdict()
        csvwrite.writerow(dic.values())

res.close()
print("over")
