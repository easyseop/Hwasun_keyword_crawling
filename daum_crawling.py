from text_crawling import soup_find_all
def scrape_daum(soup):
    res = soup_find_all(soup, 'div', {'class':'tt_article_useless_p_margin contents_style'})
    if res == True:
        return
    res = soup_find_all(soup, 'div', {'class':'contents_style'})
    if res == False:
        여행.append('')