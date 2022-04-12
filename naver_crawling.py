def scrape_naver(soup):
    res = soup_find_all(soup, 'div', {'class':'se-section se-section-text se-l-default'})
    if res == True:
        return
    res = soup_find_all(soup, 'div', {'class':'se_sectionArea'})
    if res == True:
        return
    res = soup_find_all(soup, 'div', {'id':'postViewArea'})
    if res == True:
        return
    res = soup_find_all(soup, 'div', {'class':'se-main-container'})
    if res == True:
        return
    res = soup_find_all(soup, 'div', {'class':'se-viewer se-theme-default'})
    if res == True:
        return
    res = soup_find_all(soup, 'div', {'class':'se_component_wrap sect_dsc __se_component_area'})
    if res == False:
        여행.append('')