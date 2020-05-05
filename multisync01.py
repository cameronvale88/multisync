#!/usr/bin/python3

import os
import subprocess
from concurrent import futures
#from time import time todo: add timing feature

def parseArgs():
	import argparse
	from sys import argv

	parser = argparse.ArgumentParser(epilog="Example: {} -s '/home/' -o '/backup/'".format(argv[0]))
	parser._optionals.title = 'OPTIONS'
	parser.add_argument('-s', '--source', help='source', required=True)
	parser.add_argument('-d', '--destination', help='destination', required=True)
	return parser.parse_args().source, parser.parse_args().destination


def test(source, destination):
	subprocess.call(['rsync', '-avz', str(source), str(destination) ])


if __name__=="__main__":
	start=time()
	executor=futures.ProcessPoolExecutor()
	source, destination = parseArgs()
	t=os.listdir(source)
	for x in t:
		src=source+x
		executor.submit(test, src, destination)
	executor.shutdown()
 

