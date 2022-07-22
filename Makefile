build:
	docker build -t kettan/tgdc-forwarder:latest .

publish: build
	docker push kettan/tgdc-forwarder:latest
