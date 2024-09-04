import scrapy 

cnt = 1

f = open('jrctList.txt', 'w')
f.close()

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
    'reg_plobrem_1': '',
    'reg_plobrem_type': '0',
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
    '_Token[fields]': '85b82d159548ddfa06dcbce4e3559c4e6fb57d79%3A',
    '_Token[unlocked]': 'button_type',
}

class OncoloJrctSpider(scrapy.Spider):
    name = "oncolojrct"

    # The initial page for scraping
    start_urls = ["https://jrct.niph.go.jp/search"]

    def parse(self, response):

        """
        This function parses a sample response. Some contracts are mingled
        with this docstring.

        @url https://jrct.niph.go.jp/search?searched=1&page=1
        @returns items 0
        @returns requests 11
        """

        # Get all the jrct id in the current page

        # jsonRaw = response.xpath('.//tbody')[0].xpath('.//td')[0].xpath('.//text()').get()

        # urllist = list(map(lambda x:x['url'], json.loads(jsonRaw)))

        return [
            scrapy.FormRequest(
                url="https://jrct.niph.go.jp/search",
                headers=headers,
                formdata=data,
                callback=self.parse_content,
            )
        ]
    
    def parse_content(self, response):
        jrctRaw = list(map(lambda x:x.xpath('.//td')[0].xpath('.//text()').get(), response.xpath('.//tbody')[0].xpath('.//tr')))
        jrctList = list(map(lambda x:x.split("\n                            ")[1].split(' ')[0], jrctRaw))
        print(jrctList)
        f = open('jrctList.txt', 'a')
        for jrct in jrctList:
            f.write(jrct+'\n')
        f.close()

        totalItems = int(response.xpath(".//div[@class='alert alert-dismissible fade show d-flex align-items-center alert-success']/div/text()").get().split("件")[0])

        totalPages = totalItems // 50+ (120 % 50 > 0)
        print(totalPages)
        
        global cnt
        cnt += 1

        if (cnt <= totalPages):
            yield response.follow("https://jrct.niph.go.jp/search?searched=1&page=" + str(cnt), self.parse_content)
