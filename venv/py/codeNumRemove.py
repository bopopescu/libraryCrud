text ="""
_init_(self):
05 wx .Frame .—init一(self, parent=None, title= "BoxSizer Example" )
06
07 self .mainPanel = wx . Panel (self )
08 self.upperPanel = wx.Panel(self.mainPanel)
09 self.leftButton = wx.Button(self.upperPanel, label="Left")
10 self.rightButton = wx.Button(self.upperPanel, labe1="Right")
11
12
13
14
15
16
17
18
19
20
21
22
self.hzBoxSizer = wx.BoxSizer(wx.HORIZONTAL) # 수평
self .hzBoxSizer.Add(self .leftButton)
self . hzBoxSizer .Add(self .rightButton )
self .upperPanel .SetSizer(self .hzBoxSizer)
self .middleButton = wx . Button(self .mainPanel , label= "Middle" )
self .lowerButton = wx . Button (self .ma inPanel , label = "Lower" )
"""

for i in range(5,22):
    text = text.replace('0'+str(i),"").replace(str(i)+'0',"").replace(str(i),"")
print(text)
