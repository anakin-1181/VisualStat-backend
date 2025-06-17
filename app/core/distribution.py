from app.utils.image import fig_to_image
from app.models.model import Plotparams
from scipy.stats import uniform, binom
# use off-screen rendering
import matplotlib
matplotlib.use("Agg")  
import matplotlib.pyplot as plt

def generate_distribution(params: Plotparams):
    if params.distribution == "binomial":
            fig = plot_binomial(params)
    elif params.distribution == "uniform":
            fig = plot_uniform(params)
    return fig_to_image(fig)

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
        mean_y = patches[len([x for x in bin_edges if x <= mean_x])-1].get_height() # get the height of the patch with x as mean
        ax.vlines(mean_x,0,mean_y,linestyles="--",colors="black",linewidth=0.8)
        ax.text(x=mean_x + 0.03, y=mean_y / 2, s=fr"$\mu$",va="top",ha="center", fontsize="8")
    # export image
    return fig


def plot_uniform(params: Plotparams):
    low,high,size,show_mean = params.low, params.high, params.size, params.show_mean
    # plot figure for different sample size
    samples = uniform.rvs(low,high,size=size)
    fig, ax = plt.subplots(figsize=(6,4))
    counts, bin_edges, patches = plt.hist(samples)
    # add description to the diagram
    ax.set_ylabel("count")
    ax.set_xlabel("value")
    ax.set_title(f"{size} samples of X~U({low},{high})")
    # show mean
    if show_mean:
        mean_x = (low + high)/2
        mean_y = patches[len([x for x in bin_edges if x <= mean_x])-1].get_height() # get the height of the patch with x as mean
        ax.vlines(mean_x,0,mean_y,linestyles="--",colors="black",linewidth=0.8)
        ax.text(x=mean_x + 0.03, y=mean_y / 2, s=fr"$\mu$",va="top",ha="center", fontsize="8")
    # export image
    return fig

        
        
        