import requests


class TiebaSpider(object):
    """贴吧爬虫"""
    def __init__(self, name, page):
        self.name = name
        self.page = page
        self.headers = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}

    def get_url_list(self):
        """构建爬取url列表"""
        url_list = []
        for i in range(self.page):
            url = 'https://tieba.baidu.com/f?kw=' + self.name + '&ie=utf-8&pn={}'.format(i*50)
            url.format(i*50)
            print(url)
            url_list.append(url)
        return url_list

    def save_html(self, html, page_num):
        """保存html"""
        # 构建文件名
        file_name = self.name+'吧第'+str(page_num)+'页.html'
        print(file_name)
        with open(file_name, 'w') as f:
            f.write(html)
            
    def run(self):
        # 构建url列表
        url_list = self.get_url_list()
        # 循环发送请求
        for url in url_list:
            response = requests.get(url, headers=self.headers)
            html = response.content.decode()
            page_num = url_list.index(url)+1
            print(page_num)
            # 开文件保存内容
            self.save_html(html, page_num)


if __name__ == '__main__':
    tieba_spider = TiebaSpider('李毅', 10)
    tieba_spider.run()