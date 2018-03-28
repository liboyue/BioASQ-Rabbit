.PHONY: all
all:
	make -C Ranker
	make -C Splitter
	make -C Results
	make -C Tiler
	make -C Expander
