from urllib import request, parse
import json

def fetchjoke():
    showapi_appid="34086"  #替换此值
    showapi_sign="f06cfbbfccb14ef2bdede36f279e0458"  #替换此值
    url="http://route.showapi.com/341-1"
    send_data = parse.urlencode([
    ('showapi_appid', showapi_appid)
    ,('showapi_sign', showapi_sign)
                    ,('time', "")
                    ,('page', "")
                    ,('maxResult', "")
     
  ])
 
    req = request.Request(url)
    with request.urlopen(req, data=send_data.encode('utf-8')) as f:
        str_res= f.read().decode('utf-8')
        json_res=json.loads(str_res)
        a = 1
        joketitle = []
        jokecontext = []
        jokeall = ""
        for i in json_res['showapi_res_body']["contentlist"]:
            joketitle.append(i["title"])
            jokecontext.append(i["text"])
            jokeall = jokeall + '标题 : ' + i["title"] + '\n'
            jokeall = jokeall + '内容 : \n' + i["text"] + '\n\n'
            a+=1
            break
        
        return(jokeall)
