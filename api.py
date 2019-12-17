# -*- coding: utf-8 -*-
#! /usr/bin/env python

import json
from flask import Flask
from flask import request
from flask import Response

#创建实例化请求对象
app = Flask(__name__)
 
testInfo = {}
num=0
flag=0 
# dict={'firewall': '1', 'ips': '2', 'ids': '3'}
 
@app.route("/create", methods=["post", ])
def create():

    data=request.form.get('info')
    print(data)
    str=data.split(',')
    print(str)
    
    '''
    '''
    data={"status":"Create done!"}
    resp=Response(json.dumps(data))
    resp.headers["Access-Control-Allow-Origin"] = "*"
 
    return resp

@app.route("/clear",methods=["post",])
def clear():
    data=request.form.get('info')
    print(data)
    data={"status":"Clear done!"}
    resp=Response(json.dumps(data))
    resp.headers["Access-Control-Allow-Origin"] = "*"
 
    return resp

@app.route("/update",methods=["post",])
def update():

    global num, flag
    data=request.form.get('info')
    print(data)
    str=data.split('&')
    mode=str[0]+"&"+str[1]
    flag=int(str[2])
    print(type(flag),flag)
    print(str)
    if(flag!=0):
        num=num+1
        '''
        '''
        if(mode=="firewall&ips"):
            testInfo['mode'] = '合并firewall和ips!'
        elif(mode=="firewall&ids"):
            testInfo['mode'] = '合并firewall和ids!'
        else:
            testInfo['mode'] = '合并ips和ids!'
        if(num==1):
            testInfo['status'] = 'Update start!'
        else:
            pass
        testInfo['count'] = num
        if(num==flag):
            num=0
    elif(flag==0):
        testInfo['count']=0
        testInfo['status']='该合并类型无可合并对象！'

    resp=Response(json.dumps(testInfo))
    resp.headers["Access-Control-Allow-Origin"] = "*"
     
    return resp

@app.route("/delete",methods=["post",])
def delete():
    data=request.form.get('info')
    print(data)
    data={"status":"Delete done!"}
    resp=Response(json.dumps(data))
    resp.headers["Access-Control-Allow-Origin"] = "*"
 
    return resp
 
if __name__ == '__main__':
 
    app.run(host="0.0.0.0", port=8800, )