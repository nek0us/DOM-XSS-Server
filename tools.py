#coding=utf-8
import logging
from logging import Logger

#改成网卡内网ip
host = ('127.0.0.1', 65533)

#主用户密码
passwd = "woshizhu"

#访客密码
visitor_passwd = "zhu"

#访客可见数量(默认20条)
visitor_num = 19





logger = logging.getLogger('fib')
logger.setLevel(logging.DEBUG)
hdr = logging.StreamHandler()
hdrlog = logging.FileHandler("log.log")
fromatter = logging.Formatter('[%(asctime)s] : %(message)s')
hdr.setFormatter(fromatter)
hdrlog.setFormatter(fromatter)
logger.addHandler(hdr)
logger.addHandler(hdrlog)


cookie_log = logging.getLogger('cookie_logg')
cookie_log.setLevel(logging.DEBUG)
cookie_hdr = logging.StreamHandler()
cookie_hdrlog = logging.FileHandler("cookie.log")
cookie_fromatter = logging.Formatter('[%(asctime)s] : %(message)s')
cookie_hdr.setFormatter(cookie_fromatter)
cookie_hdrlog.setFormatter(cookie_fromatter)
cookie_log.addHandler(cookie_hdr)
cookie_log.addHandler(cookie_hdrlog)

html_up = """<!DOCTYPE html>
<html>
    <head>
        <title>给</title>
        <meta charset="utf-8">
    </head>
    <body>
        <style tpye="text/css">
            .mytable{margin:0 auto}
        </style>
        <table class="mytable" border="1">
            <tr><td>序号</td>
                <td>时间</td>
                <td>IP</td>
                <td>Cookie</td>
	<td>Referrer</td>
            </tr>
            """


html = """
               
<head>

<style>
    body{
        background: #353f42;
    }
 
    *{
        padding: 0;
        margin: 0;
    }
 
    .main {
        margin: 0 auto;
        padding-left: 25px;
        padding-right: 25px;
        padding-top: 15px;
        width: 350px;
        height: 350px;
        background: #FFFFFF;
        /*以下css用于让登录表单垂直居中在界面,可删除*/
        position: absolute;
        top: 50%;
        left: 50%;
        margin-top: -175px;
        margin-left: -175px;
    }
 
    .title {
        width: 100%;
        height: 40px;
        line-height: 40px;
    }
 
    .title span {
        font-size: 18px;
        color: #353f42;
    }
 
    .title-msg {
        width: 100%;
        height: 64px;
        line-height: 64px;
    }
 
    .title:hover{
        cursor: default	;
    }
 
    .title-msg:hover{
        cursor: default	;
    }
 
    .title-msg span {
        font-size: 12px;
        color: #707472;
    }
 
    .input-content {
        width: 100%;
        height: 120px;
    }
 
    .input-content input {
        width: 330px;
        height: 40px;
        border: 1px solid #dad9d6;
        background: #ffffff;
        padding-left: 10px;
        padding-right: 10px;
    }
 
    .enter-btn {
        width: 350px;
        height: 40px;
        color: #fff;
        background: #0bc5de;
        line-height: 40px;
        text-align: center;
        border: 0px;
    }
 
    .foor{
        width: 100%;
        height: auto;
        color: #9b9c98;
        font-size: 12px;
        margin-top: 20px;
    }
 
    .enter-btn:hover {
        cursor:pointer;
        background: #1db5c9;
    }
 
    .foor div:hover {
        cursor:pointer;
        color: #484847;
        font-weight: 600;
    }
 
    .left{
        float: left;
    }
    .right{
        float: right;
    }
 
</style>
</head>



<body>
<div class="main">
    <div class="title">
        <span>密码登录</span>
    </div>
 
    <div class="title-msg">
        <span>请输入密码</span>
    </div>
 
    <form class="login-form" action= "xss" method="get" novalidate >
        <!--输入框-->
        <div class="input-content">
            <!--autoFocus-->
            
 
            <div style="margin-top: 16px">
                <input type="password"
                       autocomplete="off" placeholder="登录密码" name="password" required maxlength="32"/>
            </div>
        </div>
 
        <!--登入按钮-->
        <div style="text-align: center">
            <button type="submit" class="enter-btn" >登录</button>
        </div>
 
        <div class="foor">
            <div class="left" onclick=alert("你是猪") ><span>忘记密码 ?</span></div>
 
            
        </div>
    </form>
 
</div>
</body>
               """