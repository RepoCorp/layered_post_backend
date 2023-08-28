PYTHON=python3.9

all: layer-requirements.zip

clean:
	- rm -rf resources
	- rm -rf .aws-sam/*
	- rm layer-requirements.zip

layer-requirements.zip:
	mkdir -p resources/python
	PYTHONUSERBASE=resources/python $(PYTHON) -m pip install -r blog/post/requirements.txt
	wget -O resources/python/rds-combined-ca-bundle.pem https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem
	cd resources && zip -r ../layer-requirements.zip python && cd ..
	rm -rf resources

build: resources/layer-requirements.zip template.yaml
	sam build

sam: build
	sam deploy --capabilities CAPABILITY_NAMED_IAM --guided
