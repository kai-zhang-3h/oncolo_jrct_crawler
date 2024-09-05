import scrapy 

input_file = open("public/jrctList.txt", "r")
input_text = input_file.read()
input_file.close
jrctList = input_text.split('\n')
urlList = list(map(lambda x:"https://jrct.niph.go.jp/latest-detail/" + x, jrctList))

class OncoloJrctSpider(scrapy.Spider):
    name = "oncolojrct"

    # The initial page for scraping
    start_urls = urlList
    print(start_urls)

    def parse(self, response):

        """
        This function parses the detail page of each jrctid

        @url https://jrct.niph.go.jp/search
        @returns items 0
        @returns requests 11
        """
        
        print("hello")