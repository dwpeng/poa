import argparse
import logging
import os

from src.poa.graph import Graph
from src.poa.seq import read_file

ROOT = os.path.dirname(__file__)

def green(msg):
    return "\033[32m%s\033[0m" % str(msg)

def red(msg):
    return "\033[31m%s\033[0m" % str(msg)


name = green('[POA]')

logging.basicConfig(
    level=logging.INFO,
    format= name + " * [%(asctime)s - %(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def make_args():
    args = argparse.ArgumentParser()
    args.add_argument('file', help='需要比对的文件名')
    args.add_argument('--file_type', default='fasta', help='序列文件类型')
    args.add_argument('--load', '-l', help='加载一个garph文件到内存')
    args.add_argument('--dump', '-d', help='保存一个garph到文件', default='data.graph')
    args.add_argument('--to_html', help='将图保存为html文件，进行可视化', default='index.html')
    args.add_argument('--real_time', '-r', action='store_true', help='实时更新html文件', )
    return args.parse_args()


if __name__ == '__main__':
    args = make_args()
    if not os.path.exists(args.file):
        logging.error(red('文件不存在 %s' % args.file))
        exit(1)

    html_path = args.to_html or 'index.html'
    sequence, alignment = read_file(args.file, args.file_type)
    g = Graph()
    count = 0
    if args.load:
        g.load(args.load)
        logging.info(green('加载图: %s' % args.load))
    else:
        g.init_graph_by_seq(sequence[0])
        count = 2
        logging.info(green('POA图初始化完成，初始化序列为：%s' % sequence[0].label))
        sequence = sequence[1:]
    try:
        for index, seq in enumerate(sequence):
            g.add_seq_to_align(alignment(g, seq))
            logging.info(green('比对完成第%d条序列: %s' % (index+count, seq.label)))
            if args.real_time:
                g.to_html(open('index.html', 'w'))
                g.dump('data.graph')
    except RuntimeError as e:
        logging.error(red('POA图存在环， 收集POA信息'))
        logging.info(red('HTML文件保存到 %s' % os.path.abspath('index.html')))
        logging.info(red('POA图保存到 %s' % os.path.abspath('data.graph')))
        exit(1)

    # if args.to_html:
    #     g.to_html(open(args.to_html, 'w'))
    #     logging.info(green('HTML文件保存到 %s' % os.path.abspath(args.to_html)))
    # if args.dump:
    #     g.dump(args.dump)
    #     logging.info(green('POA图保存到 %s' % os.path.abspath(args.dump)))
    g.to_msa(open('msa.txt', 'w'))
