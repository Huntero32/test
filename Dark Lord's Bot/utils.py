from time import sleep, strftime
from datetime import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests, random, string
try:
	from faker import Faker
except Exception:
	print("Run \"pip install Faker\" using the correct pip path and you should be fine.")
	import sys; sys.exit(1)
	
fake = Faker()

def string_to_dict(headers):
	headers_dict = {}
	for line in headers.split("\n"):
		if not line: continue
		line = line.strip()
		key, *values = line.split(" ")
		key = key[:-1]
		if not (key and values): continue
		headers_dict[key] = " ".join(values)
	return headers_dict

def get_time():
    return "[" + strftime("%m/%d %H:%M:%S") + "]"

def dump(r):
	with open("dump.html", "w") as f:
		f.write(str(r))

def clean(text):
	return ''.join([i if ord(i) < 128 else ' ' for i in text])


class ThreadManager(object):
	"""docstring for ThreadManager"""
	def __init__(self, MAX_THREADS = 30, MESSAGES = False, TIME = True):
		super(ThreadManager, self).__init__()
		self.MAX_THREADS = MAX_THREADS
		self.MESSAGES = MESSAGES
		self.TIME = TIME
		self.threads = []

	def load(self, thread):
		self.threads.append(thread)

	def clear(self):
		self.threads = []

	def start(self):
		start_time = datetime.now()
		THREAD_COUNT = 0
		count = 0

		for t in self.threads:
			t.daemon = True
			t.start()
			# print(threading.active_count())
			THREAD_COUNT += 1
			if THREAD_COUNT >= self.MAX_THREADS:
				if self.MESSAGES:
					print("Waiting for a thread to end.")
				self.threads[count].join()
				if self.MESSAGES:
					print("Starting a new thread now.")
				count += 1
				THREAD_COUNT -= 1

		if self.MESSAGES:
			print("Waiting for all threads to end.")
		
		for t in self.threads:
			t.join()

		if self.TIME:
			print(datetime.now() - start_time)	

def get_user_agent():
	return fake.user_agent()

def get_random_name():
	return "{}{}{}{}{}{}{}{}{}{}{}".format (random.choice(("XX","xX","xx","bingo","Grace","olivia","mya","mya_","teverse","JayByte_","Gsmer_","DaV1D","ssm","iCyber","iCyb3r","James_","Jerry","ozpin","rwby","j3rry","Hunter","Bob","Smokey0","Sloss","dArK","dArK2","dArK3","dArK4","dArK5","LAz0r","TEvErs3","B0t","Vortex","VOrtEx","V0rTeX","JOSE","CARL","CLARENCE","Tempi","Reaper","ML","ML_","ReApEr","Fr3d","Fr3d_","TERRENCE","GameProtect",)),random.choice(string.ascii_letters), random.choice(string.ascii_letters), random.choice(string.ascii_letters),random.choice(string.ascii_letters),random.choice(string.ascii_letters),random.choice(string.ascii_letters),random.choice(string.ascii_letters),random.choice(string.ascii_letters), random.choice(("XX","xX","xx","Hunter","Bob","Smokey0","Sloss","dArK","dArK2","dArK3","dArK4","dArK5","_",)), random.randint(1, 100))

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
