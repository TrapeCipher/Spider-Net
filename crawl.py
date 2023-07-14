import requests
from os import name
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import concurrent.futures
import time
import os
import fade
from colorama import Fore

while True:
    def cls():
        if name =="nt":
            os.system("cls")
        else:
            os.system("clear")
    
    def crawl():
        def crawl_url(url):
            visited_urls = set()

            def helper(url):
                if url in visited_urls:
                    return

                visited_urls.add(url)

                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    soup = BeautifulSoup(response.text, 'html.parser')

                    for anchor in soup.find_all('a'):
                        href = anchor.get('href')

                        if href:
                            href = urljoin(url, href)
                            parsed_href = urlparse(href)

                            if parsed_href.scheme.startswith('http') and parsed_href.netloc not in visited_urls:
                                print(href)
                                helper(href)

                except KeyboardInterrupt:
                    print("CTRL + C Interrupted")

            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(helper, url)

        cls()
        def home():
            design = """\n                                                               
\t\t\t        ▒▒                  ▒▒                                
\t\t\t      ▒▒██▒▒              ▒▒██▒▒                              
\t\t\t      ▒▒██▒▒              ▒▒██▒▒                              
\t\t\t▒▒██▒▒▒▒██▒▒              ▒▒██▒▒▒▒██▒▒                        
\t\t\t▒▒██▒▒▒▒▒▒██▒▒  ▒▒  ▒▒  ▒▒██▒▒▒▒▒▒██▒▒                        
\t\t\t  ▒▒██▒▒▒▒██▒▒▒▒██▒▒██▒▒▒▒██▒▒▒▒██▒▒                          
\t\t\t  ▒▒██▒▒▒▒██▒▒▒▒██▒▒██▒▒▒▒██▒▒▒▒██▒▒                          
\t\t\t  ▒▒██▒▒▒▒▒▒██▒▒██████▒▒██▒▒▒▒▒▒██▒▒                          
\t\t\t    ▒▒██▒▒▒▒▒▒██████████▒▒▒▒▒▒██▒▒                            
\t\t\t      ▒▒██████████████████████▒▒                              
\t\t\t        ▒▒▒▒▒▒██████████▒▒▒▒▒▒                                
\t\t\t      ▒▒██████▒▒██████▒▒██████▒▒                              
\t\t\t    ▒▒██▒▒▒▒▒▒██████████▒▒▒▒▒▒██▒▒                            
\t\t\t  ▒▒██▒▒▒▒▒▒██████████████▒▒▒▒▒▒██▒▒                          
\t\t\t  ▒▒██▒▒▒▒██▒▒██████████▒▒██▒▒▒▒██▒▒                          
\t\t\t▒▒██▒▒▒▒██▒▒████▒▒▒▒▒▒████▒▒██▒▒▒▒██▒▒                        
\t\t\t▒▒██▒▒▒▒██▒▒██████▒▒██████▒▒██▒▒▒▒██▒▒                        
\t\t\t▒▒██▒▒▒▒██▒▒██████▒▒██████▒▒██▒▒▒▒██▒▒                        
\t\t\t  ▒▒▒▒▒▒██▒▒████▒▒▒▒▒▒████▒▒██▒▒▒▒▒▒                          
\t\t\t    ▒▒██▒▒  ▒▒██████████▒▒  ▒▒██▒▒                            
\t\t\t    ▒▒██▒▒    ▒▒██████▒▒    ▒▒██▒▒                            
\t\t\t    ▒▒██▒▒      ▒▒██▒▒      ▒▒██▒▒                            
\t\t\t     ▒▒██▒▒       ▒▒       ▒▒██▒▒                            
\t\t\t       ▒▒                    ▒▒  

\t\t\t         S P I D E R - N E T
            """
            print(fade.purplepink(design))
        home()
        main = input(f"Input URL >>>{Fore.LIGHTMAGENTA_EX} ")
        print(f"\n{Fore.LIGHTMAGENTA_EX}[ {Fore.WHITE}!{Fore.LIGHTMAGENTA_EX} ]{Fore.WHITE} Crawling Started\n")
        time.sleep(2)
        crawl_url(main)

    crawl()

