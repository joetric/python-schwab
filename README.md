python-schwab
=============

Python library to retrieve information from a Schwab bank account.

Get Balance
-----------

	import schwab
	schwab_browser = schwab.SchwabBrowser(your_username, your_pw)
	print schwab_browser.get_balance()

Test Setup
----------

Copy `test.dummy.sh` and replace the default values with your user id and password:

	cp test.dummy.sh test.sh
	chmod +x test.sh
	vim test.sh

You can now run tests using `./test.sh`.

Installation
------------

	./setup.py build
	./setup.py install
