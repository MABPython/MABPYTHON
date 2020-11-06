#Wikipedia Search page
import wikipediaapi
def wiksp(str):
    while True:
        wiks=input("جستجوی صفحه:")
        wikp=wikipediaapi.Wikipedia('fa')
        wkp=wikp.page(wiks)
        if wkp==True:
                    print("Page Exists:%s"% wkp.exists())
        else:
                    print("Page Exists:%s"% wkp.exists())
        wksp=wkp.summary[0:244]
        print("عنوان:",wkp.title,"\nتوضحات:\n",wksp,"...","\nپیوند.:\n",wkp.fullurl,"\n----------------------------------------------------------------------------------------------------------------")
wiksp("SPage:")
