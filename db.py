import sys, json

class SimpleDB:
	def __init__(self, fname):
		self.index_table = dict()
		self.index_table.setdefault(-1)
		self.fname = fname
		self.fp = None
	
	def build_index(self):
		fp = open(self.fname)
		if not fp:
			sys.stderr.write('\nERROR: FAIL TO OPEN FILE [%s].\n' % (self.fname))
			return -1
		fp.seek(0)
		while 1:
			offset = fp.tell()
			line = fp.readline().strip()
			if not line: break
			[id, dummy] = line.split('\t', 1)
			self.index_table[id] = offset
		fp.close()
		return 0

	def connect(self):
		if self.is_connect(): self.close()
		try:
			self.fp = open(self.fname)
		except:
			sys.stderr.write('\nERROR: FAIL TO OPEN FILE [%s].\n' % (self.fname))
			return -1
		return 0

	def close(self):
		try:
			self.fp.close()
		except:
			sys.stderr.write('\nERROR: Fail to close file [%s].\n' % (self.fname))
			self.fp = None
			return -1
		self.fp = None
		return 0

	def is_connect(self):
		return self.fp != None

	def exist_key(self, id):
		if id in self.index_table: return True
		else: return False
	

	def read_line(self, id):
		if not self.is_connect(): 
			sys.stderr.write('\nERROR: CONNECTION NOT ESTABLISH.\n')
			return None
		if not id in self.index_table:
			sys.stderr.write('\nERROR: ID [%s] NOT EXIST.\n' % (id))
			return None
		offset = self.index_table[id]
		self.fp.seek(offset)
		line = self.fp.readline().strip()
		return line
	
	def read_json(self, id):				
		line = self.read_line(id)
		if line == None: return None
		[id, jsonStr] = line.split('\t', 1)
		try:
			jsonObj = json.loads(jsonStr, encoding = 'gbk')
		except:
			sys.stderr.write('\nERROR: FAIL TO PRASE JSON STR [%s].\n' % (jsonStr))
			return None
		return jsonObj

'''
from db import SimpleDB
db = SimpleDB('novel_index.test')
db.build_index()
db.connect()
line = db.read_line('296117440')
json = db.read_json('296117440')
db.close()
'''
