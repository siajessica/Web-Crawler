from crawler import Crawler
from args import get_args
import csv

if __name__ == '__main__':
    args = get_args()
    crawler = Crawler()
    contents = crawler.crawl(args.start_date, args.end_date)
    with open(args.output, 'w') as f:
        f.write('date,title,content\n')
        for date, title, content in contents:
            title = title.replace('\n', ' ').replace('\r', '')
            title = title.replace('\"', '\"\"')
            content = ''.join(content.split())
            content = ''.join(content)
            content = content.replace('\n', ' ').replace('\r', '')
            content = content.replace('\"', '\"\"')
            out_str = f'{str(date)},"{title}","{content}"\n'
            f.write(out_str)
