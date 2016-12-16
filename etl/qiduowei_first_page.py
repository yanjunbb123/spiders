from  BeautifulSoup import BeautifulSoup

def get_link_code(read):
    soup = BeautifulSoup(read)
    urlparameter = str(soup('div')[70].a)
    target = urlparameter.split()[2]
    link = target[6:len(target)-1]
    return link