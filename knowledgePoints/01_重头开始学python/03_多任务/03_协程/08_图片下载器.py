import gevent
from gevent import monkey
import urllib.request


monkey.patch_all()

def downloader(url):
    req = urllib.request.urlopen(url)

    with open('2.jpg', 'wb') as f:
        f.write(req.read())


def main():
    gevent.joinall([
        gevent.spawn(downloader, "https://sta-op.douyucdn.cn/dy-listicon/3501a1acdafb276089d4b1dffda54c70.png?x-oss-process=image/format,webp/quality,q_70"),    #启动两个协程
        gevent.spawn(downloader, "https://sta-op.douyucdn.cn/dy-listicon/f118481a9050754749ca8e7567d06deb.png?x-oss-process=image/format,webp/quality,q_70")
    ])


if __name__ == '__main__':
    main()