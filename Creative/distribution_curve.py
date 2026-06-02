#Trying something new :)!
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random
data = {
    "normal":random.normal(loc=50,scale=5,size=1000),
    "binomial":random.binomial(n=100,p=0.5,size=1000),
    "possion":random.poisson(lam=20,size=10),
    "uniform":random.uniform(low=0,high=500,size=1000),
    "logistic":random.logistic(loc=30,scale=2,size=10),
    "Multinomial":random.multinomial(n=6,pvals=[1/6,1/6/3/6,1/6], size=10),
    "Exponential":random.exponential(scale=5,size=100),
    "chisquare":random.chisquare(df=1, size=1000),
    "rayleigh":random.rayleigh(size=1000),
    "pareto":random.pareto(a=2, size=1000),
    "zipf":random.zipf(a=2, size=1000)
}
sns.displot(data.get("normal"),kind="kde")
sns.displot(data.get("binomial"),kind="kde")
sns.displot(data.get("zipf")[data.get("zipf")<10],kind="kde")
plt.show()