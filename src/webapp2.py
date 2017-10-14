#!/usr/bin/env python
# coding:utf-8

import time
import RPi.GPIO as GPIO
from webob import Request, Response
from wsgiref.simple_server import make_server
import parts

# Web画面
html = """
<form method="post">
<input type="submit" name="button" value="LED On">
<input type="submit" name="button" value="LED Off">
</br>
<input type="submit" name="button" value="Buzzer On">
<input type="submit" name="button" value="Buzzer Off">
</form>
"""

# WebAppクラス
class WebApp(object):
  def __call__(self, environ, start_response):
    global html
    global resp
    req = Request(environ)
    if req.path == '/':
      button = req.params.get('button', '')
      resp = Response(html)
      # LED Onボタン押下時の処理
      if button == 'LED On':
        led.on()
      # LED Offボタン押下時の処理
      if button == 'LED Off':
        led.off()
      # Buzzer Onボタン押下時の処理
      elif button == 'Buzzer On':
        bz.on()
      # Buzzer Offボタン押下時の処理
      elif button == 'Buzzer Off':
        bz.off()

    return resp(environ, start_response)

if __name__ == "__main__":
  application = WebApp()
  gpioset = parts.GPIOSetting()
  gpioset.start()

  led = parts.LED()
  bz = parts.Buzzer()

  # 8080番ポートを使用する
  port = 8080
  httpd = make_server('', port, application)
  print ('Serving HTTP on port %d' % port)

  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    gpioset.stop()
    print ('Key Interrupt')

