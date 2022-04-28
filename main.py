import tkinter as tk
import  tkinter.messagebox
import dlcg,jxjk,API,peizhi
window = tk.Tk()
window.title(peizhi.banben)
window.minsize(400,300)
tk.Label(window, text='账户：').place(x=100,y=100)
tk.Label(window, text='密码：').place(x=100, y=140)

zhanghao = tk.StringVar()
wenbenkuang1 = tk.Entry(window, textvariable=zhanghao)
wenbenkuang1.place(x=160, y=100)
mima = tk.StringVar()
wenbenkuang2 = tk.Entry(window, textvariable=mima, show='*')
wenbenkuang2.place(x=160, y=140)
def denglu():
    zh = zhanghao.get().replace("'","yhzy").replace('"',"syhzy").replace(' ',"kgzy")
    mm=mima.get().replace("'","yhzy").replace('"',"syhzy").replace(' ',"kgzy")
    zt=API.dl(zh,mm)
    dlzt=zt[0]
    if dlzt!="登陆成功":
        tk.messagebox.showerror(message=dlzt)
    else:
        window.destroy()
        dlcg.dlcg(zh,mm,0)


def zhuce():
    zhucejiemian = tk.Toplevel(window)
    zhucejiemian.minsize(400, 300)
    tk.Label(zhucejiemian, text='用户名：').place(x=100, y=40)
    tk.Label(zhucejiemian, text='账户：').place(x=100, y=80)
    tk.Label(zhucejiemian, text='密码：').place(x=100, y=120)
    tk.Label(zhucejiemian, text='确认密码：').place(x=100, y=160)
    tk.Label(zhucejiemian, text='手机号：').place(x=100, y=200)
    zhuceyhm = tk.StringVar()
    wenbenkuang1 = tk.Entry(zhucejiemian, textvariable=zhuceyhm)
    wenbenkuang1.place(x=160, y=40)
    zhucezh = tk.StringVar()
    wenbenkuang2 = tk.Entry(zhucejiemian, textvariable=zhucezh)
    wenbenkuang2.place(x=160, y=80)
    zhucemm = tk.StringVar()
    wenbenkuang3 = tk.Entry(zhucejiemian, textvariable=zhucemm, show='*')
    wenbenkuang3.place(x=160, y=120)
    zhuceqrmm = tk.StringVar()
    wenbenkuang4 = tk.Entry(zhucejiemian, textvariable=zhuceqrmm, show='*')
    wenbenkuang4.place(x=160, y=160)
    zhucesjh = tk.StringVar()
    wenbenkuang5 = tk.Entry(zhucejiemian, textvariable=zhucesjh)
    wenbenkuang5.place(x=160, y=200)
    def zhucecz():
        zcyhm = zhuceyhm.get()
        zczh = zhucezh.get()
        zcmm = zhucemm.get()
        zcqrmm = zhuceqrmm.get()
        zcsjh = zhucesjh.get()
        zc = API.zc(zcyhm, zczh, zcmm, zcqrmm, zcsjh)
        zczt = zc[0]
        tk.messagebox.showinfo(message=zczt)
    anniu1 = tk.Button(zhucejiemian, text='注册', command=zhucecz)
    anniu1.place(x=170, y=230, width=100, height=50)
    zhucejiemian.mainloop()


def tuichu():
    window.destroy()


anniu1 = tk.Button(window,text='登录',command=denglu)
anniu1.place(x=120,y=200)

anniu2 = tk.Button(window,text='注册',command=zhuce)
anniu2.place(x=190,y=200)

anniu3 = tk.Button(window,text='退出',command=tuichu)
anniu3.place(x=260,y=200)





window.resizable(width=False,height=False)
window.mainloop()
