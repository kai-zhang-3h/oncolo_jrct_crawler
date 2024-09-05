import scrapy 

cnt = 1

itemsPerPage = 50

totalPages = 0

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://jrct.niph.go.jp',
    'Connection': 'keep-alive',
    'Referer': 'https://jrct.niph.go.jp/search',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'TE': 'Trailers',

}

data = {
    'demo_1': '',
    'others': '1',
    'reg_plobrem_1': '肺がん',
    'reg_plobrem_type': '0',
    'reg_recruitment[]': '2',
    'reg_region': '',
    'reg_address': '',
    'reg_medical_affilication_name': '',
    'reg_title_1': '',
    'reg_title_type': '0',
    'reg_research_num': '',
    'reg_inclusion_criteria_1': '',
    'reg_inclusion_criteria_type': '0',
    'reg_medical_product_1': '',
    'reg_medical_product_type': '0',
    'reg_inter_contents_1': '',
    'reg_inter_contents_type': '0',
    'reg_com_name_1': '',
    'reg_com_name_type': '0',
    'button_type': 'confReg',
}

class OncoloJrctIdSpider(scrapy.Spider):
    name = "oncolojrctid"

    # The initial page for scraping
    start_urls = ["https://jrct.niph.go.jp/search"]

    def parse(self, response):

        """
        This function parses the content page with all the jrct ids output to a .txt file

        @url https://jrct.niph.go.jp/search
        @returns items 0
        @returns requests 11
        """

        f = open('public/jrctList.txt', 'w')
        f.close()

        return [
            scrapy.FormRequest(
                url="https://jrct.niph.go.jp/search",
                headers=headers,
                formdata=data,
                callback=self.after_post,
            )
        ]
    
    def after_post(self, response):

        self.get_total_pages(response)
        
        count = self.parse_content_page(response)

        if (count != -1):
            yield response.follow("https://jrct.niph.go.jp/search?searched=1&page=" + str(count), self.parse_content)

    def parse_content(self, response):

        count = self.parse_content_page(response)

        if (count != -1):
            yield response.follow("https://jrct.niph.go.jp/search?searched=1&page=" + str(count), self.parse_content)

    def parse_content_page(self, response):

        global totalPages
        global cnt
        
        cnt += 1

        jrctRaw = list(map(lambda x:x.xpath('.//td')[0].xpath('.//text()').get(), response.xpath('.//tbody')[0].xpath('.//tr')))
        jrctList = list(map(lambda x:x.split("\n                            ")[1].split(' ')[0], jrctRaw))

        print(jrctList)
        
        f = open('public/jrctList.txt', 'a')
        f.write('\n'.join(jrctList))
        f.close()

        if (cnt <= totalPages):
            return cnt
        else:
            return -1
        
    def get_total_pages(self, response):
        
        global itemsPerPage
        global totalPages

        totalItems = int(response.xpath(".//div[@class='alert alert-dismissible fade show d-flex align-items-center alert-success']/div/text()").get().split("件")[0])

        totalPages = totalItems // itemsPerPage + (totalItems % itemsPerPage > 0)
        
        print(totalPages)