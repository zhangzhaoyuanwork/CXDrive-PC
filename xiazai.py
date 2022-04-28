import requests
import os
def xz(name, url):
  #path = "c:\\畅享云盘下载"
  path = os.environ['HOME']+"/下载"
  isExists = os.path.exists(path)
  if not isExists:
    os.makedirs(path)

  os.chdir(path)
  r = requests.get(url)
  with open(name, "wb") as code:
    code.write(r.content)