import tkinter as tk
import  tkinter.messagebox
import API,xiazai,sp,yy,tp,wd,sc,dlwy,gw,scwj,peizhi,jxjk,zyz,zyxt



def dlcg(zh,mm,yeshu):
    window = tk.Tk()
    window.title(peizhi.banben)
    window.minsize(900, 600)
    head = tk.Frame(window)
    head.place(x=0, y=0, width=200, height=600)

    def qbwd():
        wd.xs(zh,mm,0)
    def qbyy():
        yy.xs(zh,mm,0)
    def qbsp():
        sp.xs(zh,mm,0)
    def qbtp():
        tp.xs(zh,mm,0)

    def qbzyz():
        zyz.xs(zh,mm,0)
    def wjsc():
        tk.messagebox.showinfo(message='上传完成后点击刷新即可显示！')
        sc.sc(zh,mm)

    def shuaxin():
        window.destroy()
        dlcg(zh, mm,yeshu)

    def shangyiye():
        if(yeshu>0):
            window.destroy()
            dlcg(zh, mm, yeshu-1)
    def xiayiye():
        window.destroy()
        dlcg(zh, mm,yeshu+1)
    def dengluwangyeban():
        dlwy.dlwy(zh,mm)

    def lxsc():
        zhucejiemian = tk.Toplevel(window)
        zhucejiemian.minsize(400, 200)
        tk.Label(zhucejiemian, text='网址：').place(x=100, y=40)
        tk.Label(zhucejiemian, text='文件名：').place(x=100, y=80)
        srwangzhi = tk.StringVar()
        wenbenkuang1 = tk.Entry(zhucejiemian, textvariable=srwangzhi)
        wenbenkuang1.place(x=160, y=40)
        srname = tk.StringVar()
        wenbenkuang3 = tk.Entry(zhucejiemian, textvariable=srname)
        wenbenkuang3.place(x=160, y=80)
        zhucejiemian.resizable(width=False,height=False)

        def xgxx():
            wangzhi = srwangzhi.get()
            name = srname.get()
            API.lxsc(zh, mm, wangzhi,name)
            tk.messagebox.showinfo(message="您的申请已提交！")
            zhucejiemian.destroy()

        anniu1 = tk.Button(zhucejiemian, text='离线上传', command=xgxx)
        anniu1.place(x=170, y=120, width=100, height=50)
        zhucejiemian.mainloop()


    def hszyxt():
        zhucejiemian = tk.Toplevel(window)
        zhucejiemian.minsize(400, 200)
        tk.Label(zhucejiemian, text='文件名：').place(x=100, y=80)
        srname = tk.StringVar()
        wenbenkuang3 = tk.Entry(zhucejiemian, textvariable=srname)
        wenbenkuang3.place(x=160, y=80)
        zhucejiemian.resizable(width=False,height=False)

        def xgxx():
            name = srname.get()
            zhucejiemian.destroy()
            zyxt.xs(name,0)


        anniu1 = tk.Button(zhucejiemian, text='嗅探', command=xgxx)
        anniu1.place(x=170, y=120, width=100, height=50)
        zhucejiemian.mainloop()


    def zhgl():
        zhucejiemian = tk.Toplevel(window)
        zhucejiemian.minsize(400, 300)
        tk.Label(zhucejiemian, text='用户名：').place(x=100, y=40)
        tk.Label(zhucejiemian, text='新密码：').place(x=100, y=80)
        tk.Label(zhucejiemian, text='确认密码：').place(x=100, y=120)
        tk.Label(zhucejiemian, text='手机号：').place(x=100, y=160)
        zhuceyhm = tk.StringVar()
        wenbenkuang1 = tk.Entry(zhucejiemian, textvariable=zhuceyhm)
        wenbenkuang1.place(x=160, y=40)
        zhucemm = tk.StringVar()
        wenbenkuang3 = tk.Entry(zhucejiemian, textvariable=zhucemm, show='*')
        wenbenkuang3.place(x=160, y=80)
        zhuceqrmm = tk.StringVar()
        wenbenkuang4 = tk.Entry(zhucejiemian, textvariable=zhuceqrmm, show='*')
        wenbenkuang4.place(x=160, y=120)
        zhucesjh = tk.StringVar()
        wenbenkuang5 = tk.Entry(zhucejiemian, textvariable=zhucesjh)
        wenbenkuang5.place(x=160, y=160)
        zhucejiemian.resizable(width=False,height=False)

        def xgxx():
            zcyhm = zhuceyhm.get()
            zcmm = zhucemm.get().replace("'","yhzy").replace('"',"syhzy").replace(' ',"kgzy")
            zcqrmm = zhuceqrmm.get().replace("'","yhzy").replace('"',"syhzy").replace(' ',"kgzy")
            zcsjh = zhucesjh.get()
            if(zcmm!=zcqrmm):
                tk.messagebox.showinfo(message="两次密码不一致")
            else:
                xg = API.zhgl(zh, zcmm, zcqrmm, zcyhm, zcsjh)
                xgcg = xg[0]
                tk.messagebox.showinfo(message=xgcg)
                if xgcg == "修改成功！即将为您重新登录！":
                    window.destroy()
                    dlcg(zh, zcmm,yeshu)

        anniu1 = tk.Button(zhucejiemian, text='修改信息', command=xgxx)
        anniu1.place(x=170, y=230, width=100, height=50)
        zhucejiemian.mainloop()
    def guanwang():
        gw.gw()


    def yjx():
        tk.messagebox.showinfo(message='畅享云解析仅供学习交流使用，切勿用于商业用途。')
        jiexi=tk.Toplevel(window)
        jiexi.maxsize(260,85)
        jiexi.minsize(260, 85)
        tk.Label(jiexi, text='请输入您要解析的视频网址：').place(x=20, y=0)
        wz = tk.StringVar()
        wenbenkuang1 = tk.Entry(jiexi, textvariable=wz)
        wenbenkuang1.place(x=0, y=25, width=200, height=40)
        jkxz = tkinter.Menubutton(jiexi, text="选择接口", relief=tkinter.RAISED)
        jkxz.place(x=200, y=20, width=50, height=50)
        jiekou = tkinter.Menu(jkxz, tearoff=False)
        jiekou.add_command(label="接口1", command=lambda: jxjk.jxjk('1',wz.get()))
        jiekou.add_command(label="接口2", command=lambda: jxjk.jxjk('2', wz.get()))
        jiekou.add_command(label="接口3", command=lambda: jxjk.jxjk('3', wz.get()))
        jiekou.add_command(label="接口4", command=lambda: jxjk.jxjk('4', wz.get()))
        jiekou.add_command(label="接口5", command=lambda: jxjk.jxjk('5', wz.get()))
        jiekou.add_command(label="接口6", command=lambda: jxjk.jxjk('6', wz.get()))
        jiekou.add_command(label="接口7", command=lambda: jxjk.jxjk('7', wz.get()))
        jiekou.add_command(label="接口8", command=lambda: jxjk.jxjk('8', wz.get()))
        jiekou.add_command(label="接口9", command=lambda: jxjk.jxjk('9', wz.get()))
        jiekou.add_command(label="接口10", command=lambda: jxjk.jxjk('10', wz.get()))
        jiekou.add_command(label="接口11", command=lambda: jxjk.jxjk('11', wz.get()))
        jiekou.add_command(label="接口12", command=lambda: jxjk.jxjk('12', wz.get()))
        jiekou.add_command(label="接口13", command=lambda: jxjk.jxjk('13', wz.get()))
        jiekou.add_command(label="接口14", command=lambda: jxjk.jxjk('14', wz.get()))
        jiekou.add_command(label="接口15", command=lambda: jxjk.jxjk('15', wz.get()))
        jiekou.add_command(label="接口16", command=lambda: jxjk.jxjk('16', wz.get()))
        jiekou.add_command(label="接口17", command=lambda: jxjk.jxjk('17', wz.get()))
        jiekou.add_command(label="接口18", command=lambda: jxjk.jxjk('18', wz.get()))
        jiekou.add_command(label="接口19", command=lambda: jxjk.jxjk('19', wz.get()))
        jiekou.add_command(label="接口20", command=lambda: jxjk.jxjk('20', wz.get()))
        jkxz.config(menu=jiekou)
        jiekou.mainloop()

    tk.Button(head,text='视频',command=qbsp).place(x=0,y=0,height=60,width=100)
    tk.Button(head, text='音乐',command=qbyy).place(x=100, y=0, height=60, width=100)
    tk.Button(head, text='图片',command=qbtp).place(x=0, y=60, height=60, width=100)
    tk.Button(head, text='文档',command=qbwd).place(x=100, y=60, height=60, width=100)
    tk.Button(head, text='资源站', command=qbzyz).place(x=0, y=220, height=60, width=100)
    tk.Button(head, text='资源嗅探', command=hszyxt).place(x=100, y=220, height=60, width=100)
    tk.Button(head, text='上一页', command=shangyiye).place(x=0, y=120, height=100, width=100)
    tk.Button(head, text='下一页', command=xiayiye).place(x=100, y=120, height=100, width=100)
    tk.Button(head, text='账号管理', command=zhgl).place(x=0, y=280, height=60, width=200)
    tk.Button(head, text='文件上传',command=wjsc).place(x=0, y=340, height=100, width=100)
    tk.Button(head, text='离线上传',command=lxsc).place(x=100, y=340, height=100, width=100)
    tk.Button(head, text='云解析',command=yjx).place(x=0, y=440, height=60, width=200)
    tk.Button(head, text='登录网页版', command=dengluwangyeban).place(x=0, y=500, height=50, width=200)
    tk.Button(head, text='官网', command=guanwang).place(x=0, y=550, height=50, width=100)
    tk.Button(head, text='◐刷新◑', command=shuaxin).place(x=100, y=550, height=50, width=100)


    body = tk.Listbox(window, bg="white")
    body.place(x=200, y=0, width=700, height=600)
    a, b,id = API.xs(zh,mm,yeshu)
    tk.Label(body, text='文件名').place(x=230, y=0)
    tk.Label(body, text='下载').place(x=530, y=0)
    tk.Label(body, text='删除').place(x=630, y=0)

    y = 30
    for i in a:
        tk.Label(body, text=i).place(x=0, y=y, height=30, width=500)
        y = y + 35

    wjm = a
    wjdz = b

    def xiazaizb(b):
        wenjianming = '未知名'
        d=-1
        while(1):
            d+=1
            if wjdz[d] == b:
                wenjianming = wjm[d]
                break
        tk.messagebox.showinfo(message='点击确认开始文件下载，然后耐心等后即可。')
        xiazai.xz(wenjianming, b)
        tk.messagebox.showinfo(message='下载完成，文件保存在您系统的下载中')
        shuaxin()

    y = 30
    for inx, b in enumerate(b):
        tk.Button(body, text='下载', command=lambda arg=b: xiazaizb(arg)) \
            .place(x=500, y=y, height=30, width=100)
        y = y + 35


    def shanchu(id):
        scwj.scwj(id,zh,mm)
        tk.messagebox.showinfo(message='删除成功')
        shuaxin()


    y = 30
    for inx, id in enumerate(id):
        tk.Button(body, text='删除', command=lambda arg=id: shanchu(arg)) \
            .place(x=600, y=y, height=30, width=100)
        y = y + 35
    window.resizable(width=False, height=False)
    window.mainloop()
