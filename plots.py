"""Metrics for generic plotting.

Functions
---------
plot_metrics(history,metric)
plot_metrics_panels(history, settings)
plot_map(x, clim=None, title=None, text=None, cmap='RdGy')
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy as ct
import numpy.ma as ma
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import palettable
from matplotlib.colors import ListedColormap

mpl.rcParams["figure.facecolor"] = "white"
mpl.rcParams["figure.dpi"] = 150

def savefig(filename,dpi=300):
    for fig_format in (".png",".pdf"):
        plt.savefig(filename + fig_format, 
                    bbox_inches="tight",
                    dpi=dpi)

def get_qual_cmap():
    cmap = palettable.colorbrewer.qualitative.Accent_7.mpl_colormap
    cmap = ListedColormap(cmap(np.linspace(0,1,11)))
    cmap2 = cmap.colors
    cmap2[6,:] = cmap.colors[0,:]
    cmap2[2:6,:] = cmap.colors[5:1:-1,:]
    cmap2[1,:] = (.95,.95,.95,1)
    cmap2[0,:] = (1,1,1,1)
    cmap2[5,:] = cmap2[6,:]
    cmap2[6,:] = [0.7945098 , 0.49647059, 0.77019608, 1.]
    cmap2 = np.append(cmap2,[[.2,.2,.2,1]],axis=0)
    cmap2 = np.delete(cmap2, 0, 0)
    
    
    return ListedColormap(cmap2)   
        
    
def drawOnGlobe(ax, map_proj, data, lats, lons, cmap='coolwarm', vmin=None, vmax=None, inc=None, cbarBool=True, contourMap=[], contourVals = [], fastBool=False, extent='both', border_color='k'):

    data_crs = ct.crs.PlateCarree()
    data_cyc, lons_cyc = add_cyclic_point(data, coord=lons) #fixes white line by adding point#data,lons#ct.util.add_cyclic_point(data, coord=lons) #fixes white line by adding point
    data_cyc = data
    lons_cyc = lons
    
    
#     ax.set_global()
#     ax.coastlines(linewidth = 1.2, color='black')
#     ax.add_feature(cartopy.feature.LAND, zorder=0, scale = '50m', edgecolor='black', facecolor='black')    

    # ADD COASTLINES
    land_feature = cfeature.NaturalEarthFeature(
        category='physical',
        name='land',
        scale='50m',
        facecolor='None',
        edgecolor = border_color,
        linewidth=.75,
    )
    ax.add_feature(land_feature)
    
    # ADD COUNTRIES
    country_feature = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_0_countries',
        scale='50m',
        facecolor='None',
        edgecolor = border_color,
        linewidth=.5,
        alpha=.5,
    )
    ax.add_feature(country_feature)
    
    
    
#     ax.GeoAxes.patch.set_facecolor('black')
    
    if(fastBool):
        image = ax.pcolormesh(lons_cyc, lats, data_cyc, transform=data_crs, cmap=cmap)
#         image = ax.contourf(lons_cyc, lats, data_cyc, np.linspace(0,vmax,20),transform=data_crs, cmap=cmap)
    else:
        image = ax.pcolor(lons_cyc, lats, data_cyc, transform=data_crs, cmap=cmap,shading='auto')
    
    if(np.size(contourMap) !=0 ):
        contourMap_cyc, __ = add_cyclic_point(contourMap, coord=lons) #fixes white line by adding point
        ax.contour(lons_cyc,lats,contourMap_cyc,contourVals, transform=data_crs, colors='fuchsia')
    
    if(cbarBool):
        cb = plt.colorbar(image, shrink=.45, orientation="horizontal", pad=.02, extend=extent)
        cb.ax.tick_params(labelsize=6) 
    else:
        cb = None

    image.set_clim(vmin,vmax)
    
    return cb, image   

def add_cyclic_point(data, coord=None, axis=-1):

    # had issues with cartopy finding utils so copied for myself
    
    if coord is not None:
        if coord.ndim != 1:
            raise ValueError('The coordinate must be 1-dimensional.')
        if len(coord) != data.shape[axis]:
            raise ValueError('The length of the coordinate does not match '
                             'the size of the corresponding dimension of '
                             'the data array: len(coord) = {}, '
                             'data.shape[{}] = {}.'.format(
                                 len(coord), axis, data.shape[axis]))
        delta_coord = np.diff(coord)
        if not np.allclose(delta_coord, delta_coord[0]):
            raise ValueError('The coordinate must be equally spaced.')
        new_coord = ma.concatenate((coord, coord[-1:] + delta_coord[0]))
    slicer = [slice(None)] * data.ndim
    try:
        slicer[axis] = slice(0, 1)
    except IndexError:
        raise ValueError('The specified axis does not correspond to an '
                         'array dimension.')
    new_data = ma.concatenate((data, data[tuple(slicer)]), axis=axis)
    if coord is None:
        return_value = new_data
    else:
        return_value = new_data, new_coord
    return return_value    

def adjust_spines(ax, spines):
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', 5))
        else:
            spine.set_color('none')  
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
    else:
        ax.yaxis.set_ticks([])
    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
    else:
        ax.xaxis.set_ticks([]) 

def format_spines(ax):
    adjust_spines(ax, ['left', 'bottom'])
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('dimgrey')
    ax.spines['bottom'].set_color('dimgrey')
    ax.spines['left'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.tick_params('both',length=4,width=2,which='major',color='dimgrey')
#     ax.yaxis.grid(zorder=1,color='dimgrey',alpha=0.35)   


def plot_emissions(ax):
    x = [2015,2020,2030,2040,2050,2060,2070,2080,2090,2100]
    x_interp = np.arange(2015,2101)
    low_color = 'teal'
    high_color = 'tab:pink'
    alpha = .8


    ssp119 = [39152.726,39693.726,22847.271,10475.089, 2050.362, -1525.978,-4476.970,-7308.783,-10565.023,-13889.788]
    ssp126 = [39152.726,39804.013,34734.424,26509.183,17963.539,10527.979,4476.328,-3285.043,-8385.183,-8617.786]

    ssp119_interp = np.interp(x_interp,x,ssp119)*1000000
    ssp126_interp = np.interp(x_interp,x,ssp126)*1000000

    i = np.where(ssp119_interp<=0)[0]
    ssp119_yr = x_interp[i][0]

    i = np.where(ssp126_interp<=0)[0]
    ssp126_yr = x_interp[i][0]

    #--------------------------------------------------------
    plt.axhline(y=0,color='dimgray',linewidth=1.)

    plt.plot(x_interp,ssp119_interp/(10e9),
             linewidth=3,
             color=low_color,
             alpha=alpha,
             label='SSP1-1.9')
    plt.plot(x_interp,ssp126_interp/(10e9),
             linewidth=3,     
             color=high_color,         
             alpha=alpha,         
             label='SSP1-2.6')

    plt.legend()

    plt.annotate(ssp119_yr,(ssp119_yr,0),
                 color=low_color,
                 xytext=(2045,-.75),
                 arrowprops=dict(arrowstyle="->",
                                 color=low_color,
                                 connectionstyle="arc3"),             
                )

    plt.annotate(ssp126_yr,(ssp126_yr,0),
                 color=high_color,
                 xytext=(2082,.5),
                 arrowprops=dict(arrowstyle="->",
                                 color=high_color,
                                 connectionstyle="arc3"),             
                )



    plt.ylabel('Gt per year')
    plt.xlabel('year')

    format_spines(plt.gca())
    plt.xticks(np.arange(2010,2110,10),np.arange(2010,2110,10))
    plt.yticks(np.arange(-2,10,1),np.arange(-2,10,1))

    plt.xlim(2015,2100)
    plt.ylim(-1.5,4.5)

    plt.title('anthropogenic CO$_2$ emissions under SSP1')    