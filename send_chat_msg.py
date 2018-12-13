#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
import uuid
import time
import sys,getopt,random
import threading
import linecache
from multiprocessing import Pool

env = ''
country = ''
path = ''
chatroom = ''
number = ''
url = ''
roomid=''
line_num=0


headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Cookie": "",
    }

lock = threading.RLock()

def main(argv):
    global env, country, path, roomid, number, url, url_room
    try:
        print("----begin----")
        opts, args = getopt.getopt(argv, "e:c:p:r:n:",["env=","country=","path=","roomid=","number="])
        #print(opts)
    except getopt.GetoptError:
        print("usage: send_chat_msg.py --env <test> --country <vn> --path <Path> --roomid <SPIM-***> --number <100>")
        sys.exit(2)
    #print(len(opts))
    if len(opts) != 5:
        print("usage: send_chat_msg.py --env <test> --country <vn> --path <Path> --roomid <SPIM-***> --number <100>")
        sys.exit()
    for opt,arg in opts:
        if opt in ("-e","--env"):
            env = arg
        elif opt in ("-c","--country"):
            country = arg
            if country in ("id","th"):
                url = "https://chatroom-live."+env+".shopee."+"co."+country+"/api/v1/"
                url_room = "https://live."+env+".shopee."+"co."+country+"/api/v1/"
            if country in ("sg","tw","ph","vn"):
                url = "https://chatroom-live." + env + ".shopee." + country + "/api/v1/"
                url_room = "https://live." + env + ".shopee." + country + "/api/v1/"
            if country == "my":
                url = "https://chatroom-live." + env + ".shopee." + "com." + country + "/api/v1/"
                url_room = "https://live." + env + ".shopee." + "com." + country + "/api/v1/"
            #print(url)
        elif opt in ("-p","--path"):
            path=arg
        elif opt in ("-r","--roomid"):
            roomid = arg
        elif opt in ("-n","--number"):
            number = arg
        else:
            print("usage: send_chat_msg.py --env <test> --country <vn> --path <Path> --roomid <SPIM-***> --number <100>")
            sys.exit()


#加入房间，发送弹幕消息
def send_msg(roomid,headers):
    #lock.acquire()

    #######eventid关联的roomid获取房间号######
    url_roomid = url_room + "room/" + roomid + "/group"
    print(url_roomid)
    response = requests.get(url_roomid, verify=False).json()
    if response['err_msg'] != "success":
        print(headers['Cookie']+" 获取房间号失败!!!")
        print(response)
        #exit(2)

    print(response['data']['chat_room'])
    chatroom = response['data']['chat_room']

    #######加入房间#########################
    url_join = url + "chatroom/" + chatroom + "/join"
    print(url_join)
    tmp_uuid = uuid.uuid1()
    # print(tmp_uuid)
    body = {"uuid": str(tmp_uuid), "avatar": "http://cf.shopee.tw/file/288cec57c8c78e2876c4c18a96ebbe6f"}
    response = requests.post(url_join, data=json.dumps(body), headers=headers, verify=False).json()
    #print(response)
    if response['msg'] != "success":
        print(headers['Cookie']+" 加入房间失败!!!")
        print(response)
        #exit(2)


    usersig = response['data']['usersig']
    # print(usersig)

    #######开始读取消息发送消息###########
    #path为绝对路径
    message_path=path+"/message.txt"
    f = open(message_path, "rb")
    data = f.read().decode('utf-8')
    f.close()

    n=data.count('\n')
    #print("总行数",n)

    for num in range(0,int(number)):
        i = random.randint(1, n)
        print("i======"+str(i))
        line = linecache.getline('/Users/qi.zhou/message.txt', i).strip()
        #print("line====================="+line)
        content = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + " " + line
        url_sendMsg = url + "chatroom/" + chatroom + "/message"
        print("url_sendMsg="+url_sendMsg)
        body = {"uuid": str(tmp_uuid), "usersig": usersig, "content": content}
        print(body)
        response = requests.post(url_sendMsg, data=json.dumps(body), headers=headers, verify=False).json()
        if response['msg'] != "success":
            print(headers['Cookie']+" uuid="+str(tmp_uuid)+" 发送消息失败：")
            print(response)
        time.sleep(0.5)

    #######退出用户####################
    url_exit = url + "chatroom/" + chatroom + "/exit"
    body = {"uuid": str(tmp_uuid), "usersig": usersig}
    response = requests.post(url_exit, data=json.dumps(body), headers=headers, verify=False).json()
    if response['msg'] != "success":
        print(headers['Cookie']++" uuid="+str(tmp_uuid)+" 退出房间失败：")
        print(response)

    #lock.release()

if __name__ == "__main__":
    main(sys.argv[1:])

    pool = Pool(processes=2)

    cookie_path = path + "/cookie.txt"
    f = open(cookie_path, "r")

    """
    #多进程
    line=f.readline()
    while line:
        headers= dict()
        headers["Content-Type"]= "application/json; charset=UTF-8"
        headers["Cookie"]=line.strip()
        print(headers)
        result = pool.apply_async(send_msg,(roomid,headers))
        line=f.readline()
    pool.close()
    pool.join()
    if result.successful():
        print("successful")
    """

    #多线程
    line = f.readline()
    while line:
        headers = dict()
        headers["Content-Type"] = "application/json; charset=UTF-8"
        headers["Cookie"] = line.strip()
        #print(headers)
        t = threading.Thread(target=send_msg, args=(roomid,headers))
        t.start()
        line = f.readline()
    t.join()

    print("----End----")






