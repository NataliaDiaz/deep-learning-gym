import urllib
def download_imgs(urls_txt_file):
    """ 
    Other methods: imageScrapper Py lib or https://www.quora.com/How-do-I-download-all-images-from-a-website-using-Python 
    """
    input_file = open(urls_txt_file,'r')
    for line in input_file:
        URL= line
        IMAGE = URL.rsplit('/',1)[1]
        urllib.urlretrieve(URL, IMAGE)

download_imgs('./tiles_urls.txt')
#download_imgs('./masks_urls.txt')