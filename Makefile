
##@ Interactive Env

env:
	hatch env remove
	hatch env create
.PHONY: env

##@ Testing

test: ## Run the unit tests locally
	hatch run -- pytest --cov-report=term-missing:skip-covered --cov-config=.coveragerc --cov=pytest_datadir_extras tests || true
	hatch run -- coverage html
.PHONY: test

serve-cov: ## Run a web server to display the coverage results.
	python3 -m http.server --directory htmlcov 4321
.PHONY: serve-cov
##@ Release Mgmt.

build:
	hatch build
.PHONY: build

bumpversion:
	hatch version minor
.PHONY: bumpversion

publish:
	HATCH_INDEX_USER='salotz' hatch -v publish
.PHONY: publish

