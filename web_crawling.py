from xml.etree.ElementInclude import DEFAULT_MAX_INCLUSION_DEPTH
from discriminate_domain import determine_domain
from naver_crawling import scrape_naver
from daum_crawling import scrape_daum

def web_scraping(count):
    for num in tqdm(range(1, count+1), total=count, desc='scraping', leave=True, ncols=100, ascii=True):
        site=browser.find_element_by_css_selector(f'#sp_blog_{num} > div > div > a')
        
        Title=site.text
        URL=site.get_attribute('href').strip()
        
        fake_link =site.get_attribute('href')
        fake_html =ur.urlopen(fake_link)
        fake_soup = bs(fake_html.read(),'html.parser')

        flag, link, domain = determine_domain(fake_link, fake_soup)
        if flag == False:
            continue

        여행['Title'].append(Title)
        여행['URL'].append(URL)
        soup = bs(ur.urlopen(link).read(),'html.parser')

        if domain == 'naver':
            scrape_naver(soup)
        elif domain == 'daum':
            scrape_daum(soup)
        else:
            pass