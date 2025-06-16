from app.utils.image import fig_to_image
from app.models.model import Plotparams
from scipy.stats import uniform, binom
import matplotlib.pyplot as plt

def generate_distribution(params: Plotparams):
    match params.distribution:
        case "binomial":
            pass
        case "uniform":
            pass
    pass

def plot_binomial(params: Plotparams):
    # plot figure for different sample size
    n,p,size,show_mean = params.n, params.p, params.size, params.show_mean
    samples = binom.rvs(n,p,size=size)
    fig, ax = plt.subplots(figsize=(6,4))
    counts, bin_edges, patches = plt.hist(samples)
    # add description to the diagram
    ax.set_ylabel("count")
    ax.set_xlabel("value")
    ax.set_title(f"{size} samples of X~Bin({n},{p})")
    # show mean
    if show_mean:
        mean_x = n*p
        # if the previous bin is empty
        mean_y =  patches[int(mean_x)].get_height() if patches[int(mean_x)-1].get_height() == 0 else patches[int(mean_x)-1].get_height() 
        ax.vlines(mean_x,0,mean_y,linestyles="--",colors="black",linewidth=0.8)
        ax.text(x=mean_x, y=mean_y + 10, s=fr"$\mu$",va="top",ha="center", fontsize="8")
    # export image
    pass



def plot_uniform(params: Plotparams):
    pass
    

        
        
        