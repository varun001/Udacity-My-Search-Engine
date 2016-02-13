
#to add index keywords and url's
def add_to_index(index,keyword,url):
    
    for entry in index:
        if(entry[0]==keyword):
            entry[1].append(url);
            return;
    index.append([keyword,[url]]);
    return index;

#to get url's corresponding to page in inedex
def lookup(index,keyword):
    for entry in index:
        if(entry[0]==keyword):
            return entry[1];
    return [];

#add all keywords in a page to index
def add_page_to_index(index,url,content):
    keywords = content.split();
    for word in keywords:
        add_to_index(index, word, url)
    return index
