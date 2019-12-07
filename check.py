import requests
with open('urls.txt', 'r') as f :
 for line in f :
   print(line, end ='@')
#try :
   r = requests.get(line)
   if r.status_code == 200:
    print('200', '@Success!')
   elif r.status_code == 301:
    print('300', '@Moved Permanently!')
   elif r.status_code == 404:
    print('404', '@Not Found!')
   elif r.status_code == 302:
    print('302', '@Object moved!')
   elif r.status_code == 403:
    print('403', '@Forbidden!')
#  print(r.status_code)
#except requests.ConnectionError:
