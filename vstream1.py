#!/usr/bin/python
'''
        derived from code by Igor Maculan 
        A Simple mjpg stream http server
'''
import cv2
import Image
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import StringIO
import time
capture=None

class CamHandler(BaseHTTPRequestHandler):
        def do_GET(self):
                if self.path.endswith('.mjpg'):
                        self.send_response(200)
                        self.send_header('Content-type','multipart/x-mixed-replace; boundary=--jpgboundary')
                        self.end_headers()
                        while True:
                                try:
                                        rc,img = capture.read()
                                        if not rc:
                                                continue
                                        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                                        jpg = Image.fromarray(imgRGB)
                                        tmpFile = StringIO.StringIO()
                                        jpg.save(tmpFile,'JPEG')
                                        self.wfile.write("--jpgboundary")
                                        self.send_header('Content-type','image/jpeg')
                                        self.send_header('Content-length',str(tmpFile.len))
                                        self.end_headers()
                                        jpg.save(self.wfile,'JPEG')
                                        time.sleep(0.05)
                                except KeyboardInterrupt:
                                        break
                        return
                if self.path.endswith('.html'):
                        self.send_response(200)
                        self.send_header('Content-type','text/html')
                        self.end_headers()
                        self.wfile.write('<html><head></head><body>')
                        self.wfile.write('<img src="http://127.0.0.1:8081/cam.mjpg"/>')
                        self.wfile.write('</body></html>')
                        return

def main():
        global capture
        capture = cv2.VideoCapture(1)
        capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 160);
        capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 120);
        capture.set(cv2.cv.CV_CAP_PROP_SATURATION,0.2);
        global img
        try:
                server = HTTPServer(('',8081),CamHandler)
                print "server started"
                server.serve_forever()
        except KeyboardInterrupt:
                capture.release()
                server.socket.close()

if __name__ == '__main__':
        main()



