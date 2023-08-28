.SHELLFLAGS += -x -e
PWD = $(shell pwd)
UID = $(shell id -u)
GID = $(shell id -g)

all: clean fetch diff build

clean:
	rm -rf authentik/
	rm -rf docs/

build:
	docker run \
		--rm -v ${PWD}:/local \
		--user ${UID}:${GID} \
		docker.io/openapitools/openapi-generator-cli:v7.0.0 generate \
		-i /local/schema.yml \
		-g python \
		-o /local \
		-c /local/config.yaml
	rm -rf authentik/test
	rm -f authentik_README.md

diff: fetch
	docker run \
		--rm -v ${PWD}:/local \
		--user ${UID}:${GID} \
		docker.io/openapitools/openapi-diff:2.1.0-beta.7 \
		--markdown /local/diff.xccheckout \
		/local/schema-old.yml /local/schema.yml
	rm -f schema-old.yml

fetch:
	mv schema.yml schema-old.yml
	wget -O schema.yml https://raw.githubusercontent.com/goauthentik/authentik/master/schema.yml
