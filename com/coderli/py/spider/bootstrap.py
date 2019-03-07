from com.coderli.py.spider.crawler.httpspider import HttpSpider

httpspider = HttpSpider()
html_str = httpspider.do_request("http://tieba.baidu.com/f?kw=java&ie=utf-8");
print(html_str)