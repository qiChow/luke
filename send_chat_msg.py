#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
import uuid
import time
import sys,getopt

env = ''
country = ''
chatroom = ''
number = ''
url = ''

headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Cookie": "SPC_EC=HPQL8fezX4YA+ahvzDNWZWSbXAyTjcOBRdQVi+mfevyumuzlzyVnuJZEbUqsnkYZTU3FqKnUsHsK4aRc81b5THWkGn4xv862sKnjr6yCPt4aRlgxUppT4ELrdbSQWR3/BP4Nlw9TKp4ssjBpfjeIyskter78vZ4I/vGQuh/w/Ho=",
    }
#"env:country:chatroom:number:",
def main(argv):
    global env, country, chatroom, number, url
    try:
        print("----begin----")
        opts, args = getopt.getopt(argv, "e:c:r:n:",["env=","country=","chatroom=","number="])
        #print(opts)
    except getopt.GetoptError:
        print("usage: send_chat_msg.py --env <test> --country <vn> --chatroom <SPIM-***> --number <100>")
        sys.exit(2)
    for opt,arg in opts:
        if opt in ("-e","--env"):
            env = arg
        elif opt in ("-c","--country"):
            country = arg
            if country in ("id","th"):
                url = "https://chatroom-live."+env+".shopee."+"co."+country+"/api/v1/"
            if country in ("sg","tw","ph","vn"):
                url = "https://chatroom-live." + env + ".shopee." + country + "/api/v1/"
            if country == "my":
                url = "https://chatroom-live." + env + ".shopee." + "com." + country + "/api/v1/"
            #print(url)
        elif opt in ("-r","--chatroom"):
            chatroom = arg
        elif opt in ("-n","--number"):
            number = arg
        else:
            print("usage: send_chat_msg.py --env <test> --country <vn> --chatroom <SPIM-***> --num <100>")
            sys.exit()

#加入房间
def join_room(chatroom):
    url_join = url+"chatroom/"+chatroom+"/join"
    #print(url_join)
    tmp_uuid = uuid.uuid1()
    #print(tmp_uuid)
    body = {"uuid":str(tmp_uuid),"avatar":"http://cf.shopee.tw/file/288cec57c8c78e2876c4c18a96ebbe6f"}
    response = requests.post(url_join, data=json.dumps(body), headers=headers, verify=False).json()
    print(response)

    usersig = response['data']['usersig']
    #print(usersig)
    return tmp_uuid,usersig

#读取文件中的内容，并发送弹幕消息
def send_msg(uuid,usersig):
    f = open("/Users/qi.zhou/message.txt", "r")
    for num in range(0,int(number)):
        line = f.readline()
        while line:
            line = line.strip()
            content=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" "+line
            print(content)
            url_sendMsg = url+"chatroom/"+chatroom+"/message"
            body = {"uuid": str(uuid), "usersig": usersig, "content": content}
            # print(body)
            response = requests.post(url_sendMsg, data=json.dumps(body), headers=headers, verify=False).json()
            # print(response)
            line = f.readline()
        f.seek(0)
    f.close()


if __name__ == "__main__":
    main(sys.argv[1:])
    a,b=join_room(chatroom)
    send_msg(a,b)






