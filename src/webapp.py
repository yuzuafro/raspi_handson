#!/usr/bin/env python
# coding:utf-8

import time
import RPi.GPIO as GPIO
from webob import Request, Response
from wsgiref.simple_server import make_server
import led_on, sound_buzzer

# Web画面
html = """
<form method="post">
<input type="submit" name="button" value="LED">
<input type="submit" name="button" value="Buzzer">
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
      # LEDボタン押下時の処理
      if button == 'LED':
        led_on.led_on()
      # Buzzerボタン押下時の処理
      elif button == 'Buzzer':
        sound_buzzer.buzzer()

    return resp(environ, start_response)

if __name__ == "__main__":
  application = WebApp()

  # 8080番ポートを使用する
  port = 8080
  httpd = make_server('', port, application)
  print 'Serving HTTP on port %d' % port

  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    print 'Key Interrupt'

