.PHONY: black-check
black-check:
	black --check .

.PHONY: lint
lint:
	poetry run ruff check src


.PHONY: fix
fix:
	poetry run ruff check --fix src && black .

.PHONY: quality
quality:
	make fix lint mypy black-check


.PHONY: build
build:
	docker build -t hackaton-template .

.PHONY: run
run:
	docker run -d --name cars_params -p 8080:8080 hackaton-template
