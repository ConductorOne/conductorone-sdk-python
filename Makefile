
.PHONY: gen
gen:
	@echo "Generating SDK"
	curl -sSL https://insulator.conductor.one/api/v1/openapi.yaml -o openapi.yaml
	speakeasy generate sdk -s openapi.yaml -o . -d --lang python
	#rm openapi.yaml

.PHONY: build
build: 
	@echo "Building SDK"
	python3 -m build

.PHONY: publish
publish:
	@echo "Publishing SDK"
	python3 -m twine upload dist/conductorone_sdk*