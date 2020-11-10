import main
import unittest


class TestOutput(unittest.TestCase):
	def testValid(self):
		self.assertEqual("Soft, Soft, Tough, Soft and Soft.", str(main.Line("SST", 5)))
		self.assertEqual("Soft, Soft and Tough.", str(main.Line("SST", 3)))
		self.assertEqual("Soft, Soft, Tough, Soft, Soft and Tough.", str(main.Line("SST", 6)))
		self.assertEqual("Soft, Soft, Tough, Soft, Tough, Soft, Soft, Tough, Soft and Tough.", str(main.Line("SSTST", 10)))
		self.assertEqual("Soft, Soft, Soft and Tough.", str(main.Line("SSSTTTTSSTT", 4)))
		self.assertEqual("Soft, Soft, Soft, Tough, Tough, Tough, Tough, Soft, Soft, Tough and Tough.", str(main.Line("SSSTTTTSSTT", 11)))
		self.assertEqual("Positive integers only!", str(main.Line("SST", -1)))
		self.assertEqual("", str(main.Line("SST", 0)))
	

class TestValidation(unittest.TestCase):
	def testInvalid(self):
		self.assertEqual(True, main.validation(["SST", "5.60"])[0])
		self.assertEqual(True, main.validation(["sst", "5"])[0])
		self.assertEqual(True, main.validation(["SSTA", "5"])[0])
		self.assertEqual(True, main.validation(["SST", "9", "5.60"])[0])
		self.assertEqual(True, main.validation(["SST", "hello"])[0])
		self.assertEqual(True, main.validation(["SST", "jgi545"])[0])
		self.assertEqual(True, main.validation(["SST", "jgieg", "5"])[0])
		self.assertEqual(False, main.validation(["SST", "0"])[0])
		self.assertEqual(False, main.validation(["SST", "-1"])[0])
		self.assertEqual(True, main.validation(["SST"])[0])
		self.assertEqual(True, main.validation([])[0])


if __name__ == '__main__':
	unittest.main()