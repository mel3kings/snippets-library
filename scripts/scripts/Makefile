CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate; conda activate

# local:
install: conda-setup hasura-cli-setup npm-install
all: setup infra iterm-split

setup:
	echo "checking if config files are in setup folder"
	test -s ./setup/frontend-env || { echo "Missing frontend config file"; exit 1; }
	cp ./setup/frontend-env ./frontend/.env
	cp ./setup/kedro-server-env.sh ./

iterm-split:
	echo "starting everything"
	./iterm-split.sh $$(pwd)

frontend-pm2:
	cd frontend; npm install; npx pm2 delete AD-FE; npx pm2 start --name=AD-FE npm -- run start

start-be:
	cd backend; npm install; npx pm2 delete AD-BE; npx pm2 start --name=AD-BE npm -- run staging

infra:
	cd server; docker-compose up -d --build

npm-install:
	cd frontend; npm install
	cd backend; npm install

stop-infra:
	cd server; docker-compose down

clear-infra:
	rm -rf ./volumes

## Kedro
kedro-server:
	$(CONDA_ACTIVATE) sim
	cd kedro-server; make install; kedro info;

kedro-staging-pipeline:
	$(CONDA_ACTIVATE) sim; cd ./packages/sim; pip install -r ./src/requirements.txt; nohup bash -c 'kedro server start' > kedro-logs.log 2>&1 & echo $! > save_pid.txt;

kill-kedro:
	cd ./packages/sim; kill -9 `cat save_pid.txt`; rm save_pid.txt;

## Init
conda-setup:
	conda create --name sim python=3.8 -y
	conda activate sim
	conda config --append channels conda-forge
	conda config --append channels pytorch-lts

hasura-cli-setup:
	curl -L https://github.com/hasura/graphql-engine/raw/stable/cli/get.sh | bash

# destroy everything from scratch
teardown:
	cd ./server; docker-compose down;
	cd ./server; rm -rf ./volumes;
	#cd ./infra/local/hasura-server; mv migrations migrations-test; hasura migrate delete --all --force --database-name default; rm -rf migrations; mv migrations-test migrations;
	# conda activate base; conda env remove -n sim
