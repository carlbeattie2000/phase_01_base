
## Setup
##### Windows

- Open three instances of your OS terminal.
- In one, CD to where you want the project to be located.
- Clone the git repository
	```bash
	git clone https://github.com/carlbeattie2000/phase_01_base.git ./phase_01
	```
- Now move all your terminals to your project directory.
	```bash
	cd /your/project/location/phase_01/
	```
- Initialize the database data.
	```bash
	sqlite3 tax.db < create_sql.sql
	```

- Now, in a single terminal create the virtual environment and install the requirements.
	```bash
	python -m venv ./venv/
	pip install -r requirements.txt
	```
- Then in all three terminals, activate the venv.
	```bash
	. ./venv/bin/activate
	```

- One terminal will need to run the name server, so let's do that in one of the terminals.
	```bash
	python -m Pyro4.naming
	```
	###### Do not close this terminal
- Now the last two are used to run the client and server
	- Terminal 2
		```bash
		python server.py
		```
	- Terminal 3
		```bash
		python client.py
		```

