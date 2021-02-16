import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_page_content(request_url):
    # 得到页面内容
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html = requests.get(request_url, headers=headers, timeout=10)
    content = html.text
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    print(content)
    return soup

# 分析当前页面的投诉信息
def analysis(soup):
    # 创建DataFrame
    df = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
    # 找到完整的投诉信息框
    temp = soup.find('div', class_="tslb_b")
    # 找出所有的tr,即行
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        td_list = tr.find_all('td')
        if len(td_list) > 0:
            # id:投诉编号,brand:投诉品牌,car_model:投诉车型,desc:问题描述,problem:典型问题,datetime:投诉时间,status:投诉状态
            id, brand, car_model, type, desc, problem, datetime, status = \
                td_list[0].text, td_list[1].text, td_list[2].text, td_list[3].text, \
                td_list[4].text, td_list[5].text, td_list[6].text, td_list[7].text

            # 创建字典，数据放入字典保存到excel
            temp = {}
            temp['id'] = id
            temp['brand'] = brand
            temp['car_model'] = car_model
            temp['type'] = type
            temp['desc'] = desc
            temp['problem'] = problem
            temp['datetime'] = datetime
            temp['status'] = status
            # 将temp中的值赋值给df
            df = df.append(temp, ignore_index=True)
    return df

result = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])

## 请求URL
base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
page_num = int(input('请输入需要浏览的页数:'))
for i in range(page_num):
    #拼接当前页面的URL
    request_url = base_url + str(i+1) + '.shtml'
    #得到soup解析
    soup = get_page_content(request_url)
    #得到当前页面的DataFrame
    df = analysis(soup)
    result = result.append(df)
print(result)
result.to_excel('CarCompaint.xls',index=False)