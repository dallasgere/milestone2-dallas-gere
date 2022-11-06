launch:
	flyctl launch

deploy:
	flyctl deploy

run:
	python3 server.py

proxy:
	flyctl proxy 5432 -a dallas-demo-db

connect:
	fly pg connect -a dallas-demo-db