#!/usr/bin/env python3

class CUNYSchool:
	def __init__ (self, initname, initundergrad, initgrad):
		self.name = initname
		self.undergrad = initundergrad
		self.grad = initgrad
	
	def GetName(self):
		return self.name
	
	def GetUndergrad(self):
		return self.undergrad
	
	def GetGrad(self):
		return self.grad
	
	def SetName(self, newN):
		self.name = newN
	
	def SetUndergrad(self, newUG):
		self.undergrad = newUG
	
	def SetGrad(self, newG):
		self.grad = newG
	
	def totalStudents(self):
		return self.grad + self.undergrad


def main():
	Lehman = CUNYSchool("Lehman College", 10800, 2007)
	print(Lehman.GetName())
	print("Undergrad:\t",Lehman.GetUndergrad())
	print("Grad:     \t",Lehman.GetGrad())
	print("Total:    \t",Lehman.totalStudents())
	
	Lehman.SetUndergrad(11320)
	Lehman.SetGrad(2009)
	
	print(Lehman.GetName())
	print("Undergrad:\t",Lehman.GetUndergrad())
	print("Grad:     \t",Lehman.GetGrad())
	print("Total:    \t",Lehman.totalStudents())

if __name__ == "__main__":
	main()
