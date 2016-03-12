import sys

class Transaction:
	
	def __init__(self):
		self.db = {}
		self.transactions = []

	def begin(self):
		self.transactions.append([])
	
	def recordTransaction(self, name):
		self.transactions[-1].append((name, self.db[name] if name in self.db.keys() else None))

	def set(self, name, value):
		self.recordTransaction(name)
		self.db[name] = value

	def get(self, name):
		print self.db[name] if name in self.db.keys() and self.db[name] != None else "NULL"

	def unset(self, name):
		self.recordTransaction(name)
		self.db.pop(name, None)

	def numEqualTo(self, value):
		print len([v for v in self.db.values() if v == value])

	def rollback(self):
		if len(self.transactions[-1]) > 0 :
			for oldPair in self.transactions[-1]:
				name, oldValue = oldPair
				self.db[name] = oldValue
			
		else:
			print "NO TRANSACTION"

		if len(self.transactions) > 0: self.transactions.pop()

	def commit(self):
		if any(len(transaction) > 0 for transaction in self.transactions): 
			self.transactions = []
		
		else:
			print "NO TRANSACTION"


def main():
	t = Transaction()

	while True:
		command = raw_input().strip()
		
		if len(t.transactions) == 0 and command != 'BEGIN':
			t.begin()

		parts = command.split()
		
		if parts[0] == 'BEGIN':
			t.begin()

		elif parts[0] == 'SET':
			t.set(parts[1], parts[2])
		
		elif parts[0] == 'GET':
			t.get(parts[1])
		
		elif parts[0] == 'UNSET':
			t.unset(parts[1])
		
		elif parts[0] == 'NUMEQUALTO':
			t.numEqualTo(parts[1])
	
		elif parts[0] == 'ROLLBACK':
			t.rollback()

		elif parts[0] == 'COMMIT':
			t.commit()

		elif parts[0] == 'END':
			break

if __name__ == '__main__':
	main()
		
