.PHONY: all clean

all:
	python mm.py > mm.csv

clean:
	rm mm.csv
