import imgkit
import argparse
from multiprocessing import Pool
import pathlib

CURRENT_DIR = pathlib.Path(__file__).parent.absolute()

parser = argparse.ArgumentParser()
parser.add_argument('-f', help='path to file containing urls')
parser.add_argument('-u', help='generate image from a single url')
parser.add_argument('-o', help='output file for single url mode')
parser.add_argument('-p', type=int, default=5, help='number of worker processes to spawn')


def generate_image(url):
    filename = f'{url}.png'
    imgkit.from_url(url, f'{CURRENT_DIR}/{filename}')

if __name__ == '__main__':
    args = parser.parse_args().__dict__
    infile = args.get('f')
    inurl = args.get('u')
    outfile = args.get('o')
    numprocs =args.get('p', 5)
    
    urls = []
    if infile:
        with open(infile, 'r') as f_in:
            urls = [u.strip() for u in f_in.readlines()]
        with Pool(min(len(urls), numprocs)) as p:
            p.map(generate_image, urls)
    else:
        if not inurl:
            raise ValueError("URL (-u) is required")
        if not outfile:
            raise ValueError("outfile (-o) is required")
        imgkit.from_url(inurl, f'{outfile}')


    
