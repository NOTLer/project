class Matrica:
	def __init__(self, matr):
		self.matr = matr

	def len(self):
		return len(self.matr)

	def __add__(self, matr2):
		if type(matr2) == list:
			for i in range(len(self.matr)):
				for j in range(len(self.matr)):
					self.matr[i][j] += matr2[i][j]
			return self.matr

		else:
			for i in range(len(self.matr)):
				for j in range(len(self.matr)):
					self.matr[i][j] += matr2.matr[i][j]
			return self.matr		



m1 = Matrica([[1,2],[3,4]])
m2 = Matrica([[10, 11],[11, 11]])
print(m1+[[4,5],[6,7]])
print(m1+m2)