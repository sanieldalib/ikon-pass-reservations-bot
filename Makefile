install:
	python3 -m pip install -r requirements.txt

run:
	source .secrets && python3 main.py

build:
	docker build -t ski-reservations .

run-docker:
	docker run -it --rm -v ~/Desktop/personal/ski-reservations/:/ski-reservations/ ski-reservations