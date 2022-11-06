launch:
	flyctl launch

deploy:
	flyctl deploy

run:
	python3 server.py

proxy:
	flyctl proxy 5432 -a app-two-db

connect:
	fly pg connect -a app-two-db