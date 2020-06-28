import bs4, requests

def getAliexpressPrice(producturl):
    res = requests.get(producturl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('html.gr__aliexpress_com body.glo-detail-page div#root div.glodetail-wrap div.product-main div.product-main-wrap div.product-info div.product-price div.product-price-current span.product-price-value')
    print(str(elems))
    return elems[0].text.strip()    


price = getAliexpressPrice("https://www.aliexpress.com/item/32985243771.html?spm=a2g0o.tm110569.3844595020.1.249211ddNM341n&gps-id=seaZeus&scm=1007.25281.150704.0&scm_id=1007.25281.150704.0&scm-url=1007.25281.150704.0&pvid=0f8f3453-b8d9-4936-9726-dc944a2508cf")
print('The price is ' + price)
