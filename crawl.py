from crawl_package import getter;
import crawl_package


def crawl_web(seed, max_depth):
    tocrawl = [seed]
    crawled = []
    depth=0
    next_depth=[]
    while tocrawl and depth<=max_depth:
        page = tocrawl.pop()
        if page not in crawled:
            getter.union(next_depth, getter.get_all_links(crawl_package.get_page(page)))
            crawled.append(page)
        if not tocrawl:
            tocrawl,next_depth = next_depth,tocrawl
            depth=depth+1
            
    return crawled
    
