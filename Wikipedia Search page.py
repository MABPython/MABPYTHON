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
        print("Title:",wk.title,"\nSummary:",wks,"...","\nFor more information, go to the link below.:\n",wk.fullurl)
        print("----------------------------------------------------------------------------------------------------------------")
wiksp("SPage:")
quit=input()