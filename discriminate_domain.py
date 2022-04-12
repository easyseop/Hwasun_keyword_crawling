def determine_domain(fake_link, fake_soup):
    flag = True
    if 'naver' in fake_link:
        link = ''.join(['https://blog.naver.com', fake_soup.iframe['src']])
        domain = 'naver'
        return flag, link, domain
    elif 'daum' in fake_link:
        link = fake_link
        domain = 'daum'
        return flag, link, domain
    else:
        flag = False
        link = None
        domain = None
        return flag, link, domain