import psutil, datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        cpu_util = psutil.cpu_percent(interval=1, percpu=True)
        mem = psutil.virtual_memory()
        THRESHOLD = 100 * 1024 * 1024  # 100MB
        message = """<html lang="en"><body><table style=width:50%><th>Welcome to the server health monitor!</th><tr bgcolor="yellow"><td>Boot Time</td><td>"""
        message += str(boot_time)+"""</td></tr><tr><td bgcolor="GreenYellow">CPU UTILIATION</td><td><table style=width:100%>"""
        i=1
        for cpu in cpu_util:
                    message += """<tr><td bgcolor="NavajoWhite">CPU {core}</td><td bgcolor="pink">{util} %</td></tr>""".format(core=i,util=cpu)
                    i+=1
        message += """</table></td></tr><tr bgcolor="#skyblue"><td>AVAILABLE MEMORY</td><td>"""
        message=message+str(mem.available)+"""</td></tr><tr bgcolor="Honeydew"><td>used_memory</td><td>"""
        message=message+str(mem.used)+"""</td></tr><tr id="used_percentage" bgcolor="#6FE5F5"><td>used_percentage</td>"""
        if (mem.percent<50):
            message+="""<td>"""
        else:
            message+="""<td bgcolor="red">"""
        message=message+str(mem.percent)+"""</td></tr></table></body></html>"""
        self.wfile.write(bytes(message,'utf-8'))
        return
httpd = HTTPServer(('', 8000), MyHTTPRequestHandler)
print("Serving on port 8000...")
httpd.serve_forever()
