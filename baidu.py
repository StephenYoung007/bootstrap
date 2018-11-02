import requests, re
from bs4 import BeautifulSoup
source_cookies = 'BIDUPSID=FDF1136B4DC101138CF0EAD7DE12F399; PSTM=1518315484; __cfduid=d753fa05334f90f5061d5e7658da534521521088385; BAIDUID=D6CCB4C080BE8B9CD5254F9AB76F8F65:FG=1; MCITY=-289%3A; BDUSS=lWMGxaYXV-aExiOS1IbnpzdXlFSktNLW9VNnREcURXS21vcEs0ZGNBY0JUZlpiQVFBQUFBJCQAAAAAAAAAAAEAAADDRlAhzujR9DAwNzAwOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHAzlsBwM5bV0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; pgv_pvi=7309448192; uc_login_unique=5770f1c31223be20db17f6086d8d9f7a; uc_recom_mark=cmVjb21tYXJrXzI0MTA5NTgy; Hm_ct_41fc030db57d5570dd22f78997dc4a7e=306*1*24109582; TJSSID=u8ad2qupiv23a2rg24trhfv1o1; Hm_lvt_41fc030db57d5570dd22f78997dc4a7e=1541055218,1541121005; hm_usertype=0; hm_username=qzd123; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a02911334777; __cas__st__=5df7470e11b5a2f553fad2b0b2251843d6bfb93938e32ab1c637842dccfbfc76805570fd4962672d25fc3acd; __cas__id__=24109582; Hm_lpvt_41fc030db57d5570dd22f78997dc4a7e=1541121017'
# print(r.text)
keys = [i.split("=")[0] for i in source_cookies.split(";")]
values = [i.split("=")[-1] for i in source_cookies.split(";")]
cookies = {}
for i in range(len(keys)):
    cookies[keys[i]] = values[i]

# print(cookies)
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}
url = "https://tongji.baidu.com/web/24109582/homepage/index"
# url = "https://tongji.baidu.com/web/24109582/ajax/post"
# url = "https://hm.baidu.com/hm.gif?cc=0&ck=1&cl=24-bit&ds=1920x1080&vl=938&ep=%7B%22netAll%22%3A3%2C%22netDns%22%3A0%2C%22netTcp%22%3A0%2C%22srv%22%3A232%2C%22dom%22%3A706%2C%22loadEvent%22%3A1151%7D&et=87&ja=0&ln=en-us&lo=0&lt=1541121005&rnd=1030044674&si=41fc030db57d5570dd22f78997dc4a7e&su=https%3A%2F%2Fcas.baidu.com%2F%3Faction%3Dlogin&v=1.2.35&lv=2"
response = requests.post(url, headers = headers, cookies = cookies)
content = response.content.decode("unicode_escape")
# li = (content.split("qiaozhi", 1)[1]).split("tou.com", 1)[0]
# sou = "qiaozhi" + li + "tou.com"
# site_list = re.findall('www\.[a-z -]{1,}\.com', content)
# print(site_list)
# content = str(content)
# soup = BeautifulSoup(content, 'html.parser')
# # print(soup)
# # print(soup.find_all(class_ = "site-overview"))
print(content)
# print(soup.find(id="site-summary-tr_12695319"))"site-overview"
