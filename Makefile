
##@ Interactive Env

env:
	hatch env remove
	hatch env create
.PHONY: env

##@ Build & Test

test: ## Run the unit tests locally
	hatch run +py=310 test:cov
.PHONY: test


build:
	hatch build
.PHONY: build

##@ Release Mgmt.

bumpversion:
	hatch version minor
.PHONY: bumpversion

publish:
	HATCH_INDEX_USER='salotz' hatch -v publish
.PHONY: publish

