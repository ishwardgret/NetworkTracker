
# Install duplication 
install:
	 pip3 install -r /requirements.txt
	 
# Build the application config 
build:
	python3 DatabaseCreation.py

# Run the network tracker 
run:
	python3 NetworkTracker.py



