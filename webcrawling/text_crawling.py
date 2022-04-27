def soup_find_all(soup, tag, class_name):
    add=soup.find_all(tag, class_name)
    if len(add):
        content = ''.join([i.text.replace('\n','').replace('\xa0','') for i in add])
        여행['Text'].append(content)
        return True
    else:
        return False