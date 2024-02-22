# Scrapy settings for bookscraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "bookscraper"

SPIDER_MODULES = ["bookscraper.spiders"]
NEWSPIDER_MODULE = "bookscraper.spiders"



# for scrapeops fake user agents, to be used in middlewares.ScrapeOpsFakeUserAgentMiddleware
"""
SCRAPEOPS_API_KEY = 'your_scrape_ops_account_api_key_for_fake_user_agents'
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = 'https://headers.scrapeops.io/v1/user-agents'
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
SCRAPEOPS_NUM_RESULTS = 50
"""



# for scrapeops fake browser headers, to be used in middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware
"""
SCRAPEOPS_API_KEY = 'your_scrape_ops_account_api_key_for_fake_browser_header'
SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT =  'http://headers.scrapeops.io/v1/browser-headers' 
SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED = True
SCRAPEOPS_NUM_RESULTS = 50
"""



# for rotating free proxies
"""
ROTATING_PROXY_LIST = [
    "103.53.110.45:10801",
    "104.255.170.66:50109",
    "45.112.125.52:4145",
    "65.21.150.198:3068",
    "124.41.240.177:52480"
]
"""



# for premium proxies, to be used in middlewares.MyProxyMiddleware
"""
PROXY_USER = 'username'
PROXY_PASSWORD = 'password'
PROXY_ENDPOINT = 'proxy.proxyprovider.com' # gate.smartproxy.com
PROXY_PORT = '8000'
"""


# for scrapeops proxy aggregator request builder
# used to give control over which thing you wants to be enabled while sending proxy requests
"""
SCRAPEOPS_API_KEY = 'your_api_key_from_scrapeops->proxy_aggregator->request_builder'
SCRAPEOPS_PROXY_ENABLED = True
SCRAPEOPS_PROXY_SETTINGS = {'country':'us'}
"""



# ROTATING_PROXY_LIST_PATH = '/path/filename.txt'



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "bookscraper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "bookscraper.middlewares.BookscraperSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   "bookscraper.middlewares.BookscraperDownloaderMiddleware":543,
   # "bookscraper.middlewares.ScrapeOpsFakeUserAgentMiddleware":400, # for scrapeops fake_user_agents
   # "bookscraper.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware":400, # for scrapeops fake_browser_headers
   # "rotating_proxies.middlewares.RotatingProxyMiddleware":610, # for rotating free proxies 
   # "rotating_proxies.middlewares.BanDetectionMiddleware":620, # for detecting free proxies being ban
   #  "bookscraper.middlewares.MyProxyMiddleware":350, # for rotating premium proxies (i.e. smartproxy.com)
   # 'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk':725, # for scrapeops_proxy_api_endpoints
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "bookscraper.pipelines.BookscraperPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"





# Notes
"""
scrapy startproject bookscraper
cd bookscraper
scrapy genspider bookspider books.toscrape.com
scrapy crawl bookspider -O clean_data.json
pip install scrapy-rotating-proxies
pip install scrapeops-scrapy-proxy-sdk
"""