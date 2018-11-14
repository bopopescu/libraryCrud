
import wx
from ObjectListView import ObjectListView, ColumnDefn
import pymysql
import DB



class Results(object):
    """"""

    def __init__(self, seq, bookname, author, pub, pubyear):
        """Constructor"""
        self.seq = seq
        self.bookname = bookname
        self.author = author
        self.pub = pub
        self.pubyear = pubyear
    def getSeq(self):
        return self.seq
class OLVCheckPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        # data = getData()
        # self.data
        # for i in data:




        # self.test_data = [Results("123456789", "50158", "0065", "Patti Jones",
        #                           "111 Centennial Drive"),
        #                   Results("978561236", "90056", "7890", "Brian Wilson",
        #                           "555 Torque Maui"),
        #                   Results("456897852", "70014", "6545", "Mike Love",
        #                           "304 Cali Bvld")
        #                   ]
        # print(type(self.test_data))
        # self.test_data.append(Results("42425","@35235","23525","@3525","235525"))
        # for i in self.test_data:
        #     print(type(i))
        #     print(i)


        checkBtn = wx.Button(self, label="삭제")
        checkBtn.Bind(wx.EVT_BUTTON, self.onDelete)
        btnSizer.Add(checkBtn, 0, wx.ALL, 5)

        self.resultsOlv = ObjectListView(self,
                                         style=wx.LC_REPORT | wx.SUNKEN_BORDER)

        uncheckBtn = wx.Button(self, label="삽입")
        uncheckBtn.Bind(wx.EVT_BUTTON, self.onInsert)
        btnSizer.Add(uncheckBtn, 0, wx.ALL, 5)

        mainSizer.Add(self.resultsOlv, 1, wx.EXPAND | wx.ALL, 5)
        mainSizer.Add(btnSizer, 0, wx.CENTER | wx.ALL, 5)
        self.SetSizer(mainSizer)
        self.drawData()
        self.resultsOlv.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onTest)

    def onTest(self,e):
        print("event")

        object = self.resultsOlv.GetSelectedObject()
        print(object.getSeq())
        updateFrame = UpdateFrame(seq = object.getSeq())
        updateFrame.Show()




    def drawData(self):
        self.test_data = []
        self.DBdata = DB.getAllData()
        dblist = []
        for i in self.DBdata:
            for j in i:
                dblist.append(j)
            self.test_data.append(Results(dblist[0], dblist[1], dblist[2], dblist[3], dblist[4]))
            dblist.clear()


        self.setResults()

    def onDelete(self, event):
        """"""
        # object = self.resultsOlv.GetColumnIndexFromOrder()
        object = self.resultsOlv.GetCheckedObjects()
        # object = self.resultsOlv.GetIndexOf(self.resultsOlv.GetCheckedObjects())
        # object = self.resultsOlv.GetCheckedObjects()
        deleteSeq = []
        for obj in object:
            deleteSeq.append(obj.getSeq())

        DB.deleteData(deleteSeq)
        deleteSeq.clear()
        panel.drawData()
        panel.Refresh()
        panel.Update()
        frame.Update()
        #     print(self.resultsOlv.GetIndexOf(obj))
        # print(self.resultsOlv.GetRefData())

        # objects = self.resultsOlv.GetObjects()
        #
        # for obj in objects:
        #     self.resultsOlv.SetCheckState(obj, True)
        # self.resultsOlv.RefreshObjects(objects)

    def onInsert(self, event):
        """"""
        # frame2 = InsertFrame()
        # frame2.Show()
        print(self.resultsOlv.GetColumnCount())

    def setResults(self):
        """"""
        self.resultsOlv.SetColumns([
            ColumnDefn("도서 번호", "left", 100, "seq"),
            ColumnDefn("도서 이름", "left", 255, "bookname"),
            ColumnDefn("저자", "left", 200, "author"),
            ColumnDefn("출판사", "left", 150, "pub"),
            ColumnDefn("출판년도", "left", 200, "pubyear")
        ])
        self.resultsOlv.CreateCheckStateColumn()
        self.resultsOlv.SetObjects(self.test_data)

class secondFrame(wx.Frame):
    def __init__(self):
        title = "insert"
        wx.Frame.__init__(self, parent = None, title=title, size=(500,500))
class UpdateFrame(wx.Frame):

    def __init__(self, seq):
        super(UpdateFrame, self).__init__(parent=None, title="수정", size=(260,370))
        self.seq = seq
        self.initui()
        self.Show()

        print(seq)
        print(self.seq)

    def initui(self):
        panel = wx.Panel(self, -1)
        #
        # menubar = wx.MenuBar()
        # menu_file = wx.Menu()
        # menu_edit = wx.Menu()
        # menu_help = wx.Menu()
        # menubar.Append(menu_file, '&File')
        # menubar.Append(menu_edit, '&Edit')
        # menubar.Append(menu_help, '&Help')
        # self.SetMenuBar(menubar)

        list = DB.getOneData(self.seq)

        bookdata = list[0][0]
        self.booknameTxt = bookdata[1]
        self.authorTxt = bookdata[2]
        self.pubTxt = bookdata[3]
        self.pubdateTxt = bookdata[4]
        self.bookInfoTxt = list[1][0][0]


        wx.StaticText(panel, pos=(20,10), label ="저자")
        wx.StaticText(panel, pos=(20, 40), label="도서 이름")
        wx.StaticText(panel, pos=(20, 70), label="출판사")
        wx.StaticText(panel, pos=(20, 100), label="출판일")
        wx.StaticText(panel, pos=(20, 130), label="소개")
        # wx.StaticText(panel, pos=(20, 160), label="분류")
        # type = ["소설","기술서적"]
        # booktype = wx.ComboBox(panel, choices=type, pos=(10,190), size=(70,25))
        self.author = wx.TextCtrl(panel, pos=(90,10),size=(130,23))
        self.bookname = wx.TextCtrl(panel, pos=(90, 40), size=(130, 23))
        self.pub = wx.TextCtrl(panel, pos=(90, 70), size=(130, 23))
        self.pubdate = wx.TextCtrl(panel, pos=(90, 100), size=(130, 23))
        self.content = wx.TextCtrl(panel, pos=(90, 130), size=(130, 100))
        addBtn = wx.Button(panel, pos=(90,250), size=(80,30), label = "수정")
        self.author.SetLabelText(self.authorTxt)
        self.bookname.SetLabelText(self.booknameTxt)
        self.pub.SetLabelText(self.pubTxt)
        self.pubdate.SetLabelText(self.pubdateTxt)
        self.content.SetLabelText(self.bookInfoTxt)
        # wx.TextCtrl(panel, pos=(50, 10), size=(100, 150))
        addBtn.Bind(wx.EVT_BUTTON,self.OnBtnInserData)

    def OnBtnInserData(self,e):
        DB.updateData(self.bookname.GetValue(),self.author.GetValue(),self.pub.GetValue(),
                     self.pubdate.GetValue(),self.content.GetValue(),self.seq)
        wx.MessageBox("수정되었습니다!", "확인")
        panel.drawData()
        panel.Update()
        panel.Refresh()
        frame.Refresh()
        frame.Update()
        self.Destroy()
        pass

class InsertFrame(wx.Frame):

    def __init__(self):
        super(InsertFrame, self).__init__(parent=None, title="삽입", size=(260,370))
        self.initui()
        self.Show()

    def initui(self):
        panel = wx.Panel(self, -1)

        menubar = wx.MenuBar()
        menu_file = wx.Menu()
        menu_edit = wx.Menu()
        menu_help = wx.Menu()

        menubar.Append(menu_file, '&File')
        menubar.Append(menu_edit, '&Edit')
        menubar.Append(menu_help, '&Help')
        self.SetMenuBar(menubar)
        wx.StaticText(panel, pos=(20,10), label ="저자")
        wx.StaticText(panel, pos=(20, 40), label="도서 이름")
        wx.StaticText(panel, pos=(20, 70), label="출판사")
        wx.StaticText(panel, pos=(20, 100), label="출판일")
        wx.StaticText(panel, pos=(20, 130), label="소개")
        # wx.StaticText(panel, pos=(20, 160), label="분류")
        # type = ["소설","기술서적"]
        # booktype = wx.ComboBox(panel, choices=type, pos=(10,190), size=(70,25))
        self.author = wx.TextCtrl(panel, pos=(90,10),size=(130,23))
        self.bookname = wx.TextCtrl(panel, pos=(90, 40), size=(130, 23))
        self.pub = wx.TextCtrl(panel, pos=(90, 70), size=(130, 23))
        self.pubdate = wx.TextCtrl(panel, pos=(90, 100), size=(130, 23))
        self.content = wx.TextCtrl(panel, pos=(90, 130), size=(130, 100))
        addBtn = wx.Button(panel, pos=(90,250), size=(80,30), label = "삽입")
        # wx.TextCtrl(panel, pos=(50, 10), size=(100, 150))
        addBtn.Bind(wx.EVT_BUTTON,self.OnBtnInserData)

    def OnBtnInserData(self,e):
        DB.insertData(self.bookname.GetValue(),self.author.GetValue(),self.pub.GetValue(),
                     self.pubdate.GetValue(),self.content.GetValue())
        wx.MessageBox("입력되었습니다!", "확인")
        panel.drawData()
        panel.Update()
        panel.Refresh()
        frame.Refresh()
        frame.Update()
        self.Destroy()
        pass



class OLVCheckFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        title = "도서관리 프로그램"
        wx.Frame.__init__(self, parent=None, title=title, size=(924, 768), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        # panel = OLVCheckPanel(self)


if __name__ == "__main__":

    app = wx.App(False)
    frame = OLVCheckFrame()
    panel = OLVCheckPanel(frame)
    # frame = OLVCheckFrame()
    frame.Show()
    app.MainLoop()