from xml.etree.ElementTree import Element,dump,SubElement,ElementTree
from lxml import etree
import xml.dom.minidom
import DB

class XMLVar():
    def __init__(self):
        self.book = Element('book')
        self.seq = Element('seq')
        self.bookname = Element('bookname')
        self.author = Element('author')
        self.pub = Element('pub')
        self.pubyear = Element('pubyear')
        self.bookinfo = Element('bookinfo')
        self.book = Element('book')

class XML():
    def makeXmlFile(self, path):

        list = DB.getAllData()
        list2 = DB.getDetailDataALL()
        # print(list)
        # print(list2)
        xml = Element("xml")
        # youtube = Element('youtube')
        # youtube.text = videoId

        varList =[]
        for i in range(0, len(list)):
            varList.append(XMLVar())



        # xml.append(youtube)
        # book = Element('book')
        # seq = Element('seq')
        # bookname = Element('bookname')
        # author = Element('author')
        # pub = Element('pub')
        # pubyear = Element('pubyear')
        # bookinfo = Element('bookinfo')

        # for i in list:
            # print(i)
            # print(i[1])
        z = 0

        for i,j in zip(list,list2):
            varList[z].seq.text = str(i[0])
            varList[z].bookname.text=str(i[1])
            varList[z].author.text=str(i[2])
            varList[z].pub.text=str(i[3])
            varList[z].pubyear.text=str(i[4])
            varList[z].bookinfo.text=str(j[0])
            varList[z].book.append(varList[z].seq)
            varList[z].book.append(varList[z].bookname)
            varList[z].book.append(varList[z].author)
            varList[z].book.append(varList[z].pub)
            varList[z].book.append(varList[z].pubyear)
            varList[z].book.append(varList[z].bookinfo)
            xml.append(varList[z].book)
            z= z+1
            # print(i[0],i[1],i[2],i[3],i[4],j[0])


            #
            # seq.text = str(i[0])
            # bookname.text=str(i[1])
            # author.text=str(i[2])
            # pub.text=str(i[3])
            # pubyear.text=str(i[4])
            # bookinfo.text=str(j[0])
            # book.append(seq)
            # book.append(bookname)
            # book.append(author)
            # book.append(pub)
            # book.append(pubyear)
            # book.append(bookinfo)
            # xml.append(book)



            # seq.clear()
            # bookname.clear()
            # author.clear()
            # pub.clear()
            # pubyear.clear()
            # bookinfo.clear()
            # book.clear()



        # src = Element('src')
        # src.text = img.get_attribute("src")
        # xml.append(src)

        ElementTree(xml).write(path)
        # ElementTree(xml).write(collectionDirectoryPath+driver.find_element_by_css_selector(".season_tit").text.replace("Fall/Winter","FW").replace("Spring/Summer","SS").replace("Ready To Wear","")+".xml")
    # time.sleep(0.2)
