import matplotlib
import pandas as pd

def cover():
	df = pd.read_csv("pokemon.csv")
	df[(df["Attack"] > 80) & (df["Speed"] > 52)].to_csv("newpokemon.csv") #chuyen sang file csv moi voi cac pokemon co attack > 80
																		  #va speed >52
	return

def matplotlib():
	df = pd.read_csv("newpokemon.csv", usecolums = ["Attack", "Speed"])
	df.plot()
	return 

if __name__ == '__main__':
	cover()
