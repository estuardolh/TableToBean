cat: input.csv
	rm ./output/Cat.java
	python TableToBean.py input.csv
sight-cat: ./output/Cat.java
	cat ./output/Cat.java
