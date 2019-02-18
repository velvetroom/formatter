import os
import unittest

def tcr():
	os.system('pwd')
	suite = unittest.defaultTestLoader.discover(".")
	if unittest.TextTestRunner(verbosity=0, failfast=True).run(suite).wasSuccessful():
		os.system("git add .")
		os.system("git commit -m 'tcr passed'")
	else:
		os.system('echo 2')
tcr()