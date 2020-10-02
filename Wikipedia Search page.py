#Wikipedia Search page
import wikipediaapi
def wiksp(str):
    wiks=input("SPage:")
    wi=wikipediaapi.Wikipedia('en')
    wk=wi.page(wiks)
    wks=wk.summary[0:244]
    print("Page Exists:%s"% wk.exists())
    print("Title:",wk.title,"\nSummary:",wks,"...")
    print("For more information, go to the link below.:\n",wk.fullurl)
wiksp("SPage:")
