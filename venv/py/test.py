import wx
#
# app = wx.App()
#
# frame = wx.Frame(parent =None, title ='Hello')
# frame.Show()
#
# app.MainLoop()
#########################1
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="window",
                          style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        panel = wx.Panel(self)

        listBox = wx.ListBox(panel, choices=['1', 'ㅇㅇ', 'ㅇㅇㅇ'])
        app2 = wx.App()
        btnClick = wx.Button(panel, label="Click Me!")
        btnClick.Bind(wx.EVT_BUTTON, self.OnBtnClickMe)
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileNewMenu = wx.MenuItem(id=wx.ID_ANY, text="xml로 저장하기")
        fileMenu.Append(fileNewMenu)
        menuBar.Append(fileMenu, "&File")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OnNew, fileNewMenu)



    def onSet(self):
        frame = MyFrame()
        frame.SetSize(wx.Size(700, 400))
        frame.Show()

        # self.Bind(wx.EVT_CLOSE,self.OnClose)
        #
        # panel = wx.Panel(self)
        #
        #
    def OnNew(self,e):
        wx.MessageBox("OnNew() Clicked!")
    def OnBtnClickMe(self,event):
        wx.MessageBox("Clicked!", "Simple Button", wx.OK)

    def OnClose(self,event):
        print("event!")
        if wx.MessageBox("윈도우를 닫을까요?", "확인", wx.YES_NO) != wx.YES:
            event.Skip(False)
        else:
            self.Destroy()


app = wx.App(False)
frame = MyFrame()

frame.Show()
app.MainLoop()