import requests
import re
import webbrowser
import peizhi
wangzhi=peizhi.wangzhi
def dlwy(zh,mm):
    url = wangzhi + "/API/changxiangyunpanPC/dl_2.php?zh" + "=" + str(zh) + "&" + "mm=" + str(mm)
    webbrowser.open_new_tab(url)


def sc(zh, mm):
    url = wangzhi + "/API/changxiangyunpanPC/wjsc_1.php?zh"+"=" +str(zh)+"&" + "mm="+str(mm)
    webbrowser.open_new_tab(url)

def scwj(id,zh,mm):
    url = wangzhi + "/API/changxiangyunpanPC/sc.php"
    data = {"zh": zh,"mm":mm,"wjid":id}
    requests.post(url=url, data=data)

def lxsc(zh,mm,wz,name):
    url = wangzhi + "/wjcz/lxsc_2.php"
    data = {"zh": zh,"mm":mm,"wangzhi":wz,"name":name}
    te=requests.post(url=url, data=data)


def gw():
    url =wangzhi
    webbrowser.open_new_tab(url)


def sp(zh,mm,yeshu):
    url = wangzhi + "/API/changxiangyunpanPC/sp.php"
    data = {"zh": zh,"mm":mm,"yeshu":yeshu}
    res = requests.post(url=url, data=data)
    res.encoding = 'utf-8'
    ym = res.text
    wjm = re.findall('<div id="wjm" style="height=20px;width=100px;">(.*?)</div>', ym)
    wz = re.findall('<a href="(.*?)" name="dizhi"', ym)
    return wjm,wz
def wd(zh,mm,yeshu):
    url = wangzhi + "/API/changxiangyunpanPC/wd.php"
    data = {"zh": zh,"mm":mm,"yeshu":yeshu}
    res = requests.post(url=url, data=data)
    res.encoding = 'utf-8'
    ym = res.text
    wjm = re.findall('<div id="wjm" style="height=20px;width=100px;">(.*?)</div>', ym)
    wz = re.findall('<a href="(.*?)" name="dizhi"', ym)
    return wjm,wz
def yy(zh,mm,yeshu):
    url = wangzhi + "/API/changxiangyunpanPC/yy.php"
    data = {"zh": zh,"mm":mm,"yeshu":yeshu}
    res = requests.post(url=url, data=data)
    res.encoding = 'utf-8'
    ym = res.text
    wjm = re.findall('<div id="wjm" style="height=20px;width=100px;">(.*?)</div>', ym)
    wz = re.findall('<a href="(.*?)" name="dizhi"', ym)
    return wjm,wz
def tp(zh,mm,yeshu):
    url = wangzhi + "/API/changxiangyunpanPC/tp.php"
    data = {"zh": zh,"mm":mm,"yeshu":yeshu}
    res = requests.post(url=url, data=data)
    res.encoding = 'utf-8'
    ym = res.text
    wjm = re.findall('<div id="wjm" style="height=20px;width=100px;">(.*?)</div>', ym)
    wz = re.findall('<a href="(.*?)" name="dizhi"', ym)
    return wjm,wz

def zyz(zh,mm,yeshu):
    url = wangzhi + "/API/changxiangyunpanPC/xs_zyz.php"
    data = {"zh": zh,"mm":mm,"yeshu":yeshu}
    res = requests.post(url=url, data=data)
    res.encoding = 'utf-8'
    ym = res.text
    wjm = re.findall('<div id="wjm" style="height=20px;width=100px;">(.*?)</div>', ym)
    wz = re.findall('<a href="(.*?)" name="dizhi"', ym)
    return wjm,wz
def zyxt(name,yeshu):
    url = wangzhi + "/API/changxiangyunpanPC/xs_zyxt.php"
    data = {"name":name,"yeshu":yeshu}
    res = requests.post(url=url, data=data)
    res.encoding = 'utf-8'
    ym = res.text
    wjm = re.findall('<div id="wjm" style="height=20px;width=100px;">(.*?)</div>', ym)
    wz = re.findall('<a href="(.*?)" name="dizhi"', ym)
    return wjm,wz

def xs(zh,mm,yeshu):
    url = wangzhi+"/API/changxiangyunpanPC/xs.php"
    data = {"zh": zh,"mm":mm,"yeshu":yeshu}
    res = requests.post(url=url, data=data)
    res.encoding = 'utf-8'
    ym = res.text
    wjm = re.findall('<div id="wjm" style="height=20px;width=100px;">(.*?)</div>', ym)
    wz = re.findall('<a href="(.*?)" name="dizhi"', ym)
    id=re.findall('《(.*?)》',ym)
    return wjm,wz,id


def dl(zh,mm):
    url = wangzhi+"/API/changxiangyunpanPC/dl.php"
    data = {"zh":zh,"mm":mm}
    res = requests.post(url=url, data=data)
    res.encoding = 'utf-8'
    ym = res.text
    dlzt = re.findall('《(.*?)》', ym)
    return dlzt

def zc(yhm,zh,mm,qrmm,sjh):
    url = wangzhi+"/API/changxiangyunpanPC/zc.php"
    zh = zh.replace("'", "yhzy").replace('"', "syhzy").replace(' ', "kgzy")
    mm = mm.replace("'", "yhzy").replace('"', "syhzy").replace(' ', "kgzy")
    qrmm = qrmm.replace("'", "yhzy").replace('"', "syhzy").replace(' ', "kgzy")
    data = {"zh":zh,"mm":mm,"yhm":yhm,"qrmm":qrmm,"sjh":sjh}
    res = requests.post(url=url, data=data)
    res.encoding = 'utf-8'
    ym = res.text
    zczt = re.findall('《(.*?)》', ym)
    return zczt
def zhgl(zh,mm,qrmm,yhm,sjh):
    url = wangzhi+"/API/changxiangyunpanPC/zhgl.php"
    data = {"zh":zh,"mm":mm,"qrmm":qrmm,"yhm":yhm,"sjh":sjh}
    res = requests.post(url=url, data=data)
    res.encoding = 'utf-8'
    ym = res.text
    zczt = re.findall('《(.*?)》', ym)
    return zczt

def jxjk(jk,wz):
    url = wangzhi + "/API/changxiangyunpanPC/vip.php?jiekou"+"=" +str(jk)+"&" + "lianjie="+str(wz)
    webbrowser.open_new_tab(url)

def lxjx(jk,wz):
    url=jk+wz
    webbrowser.open_new_tab(url)

