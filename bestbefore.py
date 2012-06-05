#!/usr/bin/python
'''
Spotify Best Before puzzle, found on http://www.spotify.com/nl/jobs/tech/best-before/
'''
import itertools
import datetime
import sys

def main():
	date = sys.stdin.readline().strip()
	parts = [ int(part) for part in date.split('/') ]
	dates = []
	for d in itertools.permutations(parts):
		try:
			dates.append(datetime.date(2000+(d[0]%1000),d[1],d[2]))
		except:
			pass
	if len(dates) > 0:
		dates.sort()
		print(dates[0])
	else:
		print('%s is illegal' % date)

if __name__ == '__main__':
	main()
