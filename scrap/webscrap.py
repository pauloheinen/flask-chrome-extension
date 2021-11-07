# SELENIUM
from selenium import webdriver
import os


# FOR HEROKU USE THIS
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

'''
# FOR LOCALHOST USE THIS
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('--disable-extensions')
options.add_argument('--profile-directory=Default')
options.add_argument("--incognito")
options.add_argument("--disable-plugins-discovery")
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
'''

# ENGINES LIST
DUCK = "https://duckduckgo.com/?q={0}"
ASK = "https://www.ask.com/web?q={0}"
GOOGLE = "https://www.google.com/search?q={0}"
YANDEX = "https://yandex.com/search/?text={0}"
YAHOO = "https://search.yahoo.com/search;_ylt=A0geKei5QEZhFKAAL1xDDWVH;_ylc=X1MDMTE5NzgwNDg2NwRfcgMyBGZyAwRmcjIDcDpzLHY6c2ZwLG06c2ItdG9wBGdwcmlkAzJVOExwOFkuU1ZXUG4uazRvTDZHZUEEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzgxBHF1ZXJ5A0h1bmdyaWElMjBIaXAlMjBIb3AlMjAtJTIwQW1vciUyMGUlMjBGJUMzJUE5JTIwKE9mZmljaWFsJTIwTXVzaWMlMjBWaWRlbyklMjAlMjNDaGVpcm9Eb01hdG8lMjAobXAzY3V0Lm5ldCkubXAzBHRfc3RtcAMxNjMxOTk0MDQ2?p={0}&fr=sfp&fr2=p%3As%2Cv%3Asfp%2Cm%3Asb-top&iscqry="
ENGINESLIST = [YANDEX, ASK, YAHOO, DUCK, GOOGLE]


class Scrap:

    def __init__(self):
        self.driver = driver
        self.engineslist = ENGINESLIST

    def startBroser(self, item):

        q = "spotify track " + item
        q.replace(' ', '')
        key = 'https://open.spotify.com/track/'

        try:
            return self.Browser(q, self.engineslist[0], key, item)
        except ValueError:
            return ValueError.args

    def Browser(self, query, engine, key, item):

        self.driver.get(engine.format(query))  # starts the chrome and searches the query
        tags = self.driver.find_elements_by_xpath("//a[@href]")  # find <a </a>
        tagcounter = 0

        # filtering information
        for tag in tags:  # for every tag in tags[]
            tagcounter += 1
            tag = tag.get_attribute("href")  # i want only href in <a </a>

            if tag.startswith(key):  # if the url start with the key that i want
                self.driver.get(tag)
                actualurl = self.driver.current_url
                track = actualurl.replace('https://open.spotify.com/track/', '')
                return track

            elif len(tags) == tagcounter:  # if it is at the end of tags[] then
                if (self.engineslist.index(engine) + 1) >= len(self.engineslist):  # if hasn't ended the search engines[]
                    return None

                else:
                    self.Browser(query, self.engineslist[self.engineslist.index(engine) + 1], key,
                                 item)  # uses another search engine
