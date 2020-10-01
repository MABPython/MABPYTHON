#Wikipedia Search page
import wikipediaapi
input=input("SPage:")
while True:
    wi=wikipediaapi.Wikipedia('en')
    wk=wi.page(input)
    wks=wk.summary[0:244]
    #wkutf=wks.encode()
    print("Page Exists:%s"% wk.exists())
    print("Title:",wk.title,"\nSummary:",wks,"...")
    print("For more information, go to the link below.:\n",wk.fullurl)
    break
