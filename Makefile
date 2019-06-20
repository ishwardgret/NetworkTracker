
# Install duplication 
install:
	 pip3 install -r /requirements.txt
	 
# Build the application config 
build:
	python3 DatabaseCreation.py

# Run the network tracker 
run:
	python3 NetworkTracker.py

runMac:
	python3 main.py -i en0

runWindow:
	python3 main.py -i r'\Device\NPF_{756436B5-1D0B-47B4-9953-0D138C651CAA}'



