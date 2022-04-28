import tkinter as tk
import API
import xiazai,peizhi

def xs(zh,mm,yeshu):
    def shangyiye():
        if(yeshu>0):
            window.destroy()
            xs(zh, mm, yeshu-1)

    def xiayiye():
        window.destroy()
        xs(zh, mm, yeshu+1)



    window = tk.Tk()
    window.title(peizhi.banben)
    window.minsize(700, 600)

    body = tk.Listbox(window, bg="white")
    body.place(x=0, y=0, width=700, height=600)
    a, b = API.sp(zh,mm,yeshu)
    tk.Label(body, text='文件名').place(x=280, y=0)
    tk.Label(body, text='下载').place(x=630, y=0)
    tk.Button(body, text='下一页', command=xiayiye).place(x=400, y=0, height=30, width=60)
    tk.Button(body, text='上一页', command=shangyiye).place(x=150, y=0, height=30, width=60)

    y = 30
    for i in a:
        tk.Label(body, text=i).place(x=0, y=y, height=30, width=600)
        y = y + 35
    y = 30
    wjm = a
    wjdz = b





    def xiazaizb(b):
        wenjianming = '未知名'
        d = -1
        while (1):
            d += 1
            if wjdz[d] == b:
                wenjianming = wjm[d]
                break
        tk.messagebox.showinfo(message='点击确认开始文件下载，然后耐心等后即可。')
        xiazai.xz(wenjianming, b)
        tk.messagebox.showinfo(message='下载完成，文件保存在您系统的下载中')
        window.destroy()
        xs(zh, mm,yeshu)
    y = 30
    for inx, b in enumerate(b):
        tk.Button(body, text='下载', command=lambda arg=b: xiazaizb(arg)) \
            .place(x=600, y=y, height=30, width=100)
        y = y + 35
    window.resizable(width=False, height=False)
    window.mainloop()