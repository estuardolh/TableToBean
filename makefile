cat: input.csv
	rm -f ./output/Cat.java
	python TableToBean.py input.csv
checkout-cat: ./output/Cat.java
	cat ./output/Cat.java
