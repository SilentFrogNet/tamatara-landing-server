#------------------------------------------------------------
#					INSTALL
#------------------------------------------------------------

install-all:
	pip install --no-cache-dir -r requirements.txt

install-all-dev:
	pip install --no-cache-dir -r requirements.dev.txt

#------------------------------------------------------------
#					RUN
#------------------------------------------------------------

run:
	uvicorn app.main:app

run-dev:
	uvicorn app.main:app --reload
