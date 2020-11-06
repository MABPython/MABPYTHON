#Wikipedia Search page
import wikipediaapi
def wiksp(str):
    while True:
        wiks=input("SPage:")
        wi=wikipediaapi.Wikipedia('en')
        wk=wi.page(wiks)
        if wk==True:
                    print("Page Exists:%s"% wk.exists())
        else:
                    print("Page Exists:%s"% wk.exists())
        wks=wk.summary[0:244]
        print("Title:",wk.title,"\nSummary:",wks,"...","\nFor more information, go to the link below.:\n",wk.fullurl,"\n------------------------------------------------------Persian----------------------------------------------------------")
        #Persian
        wikp=wikipediaapi.Wikipedia('fa')
        wkp=wikp.page(wiks)
        if wkp==True:
                    print("Page Exists:%s"% wkp.exists())
        else:
                    print("Page Exists:%s"% wkp.exists())
        wksp=wkp.summary[0:244]
        
        print("عنوان:",wkp.title,"\nتوضحات:\n",wksp,"...","\nپیوند.:\n",wkp.fullurl,"\n----------------------------------------------------------------------------------------------------------------")
wiksp("SPage:")
quit=input()