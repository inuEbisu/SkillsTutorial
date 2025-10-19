.PHONY: serve

serve:
	mkslides serve slides

build:
	mkslides build slides

format:
	npm run format

check:
	npm run format:check
