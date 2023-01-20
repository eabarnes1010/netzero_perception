"""Analysis functions.

Functions
---------
process_variable(var, da, YEAR_RANGE)
compute_global_mean(da)
fraction_positive(da)
compute_global_mean(da)
fraction_positive(da)
"""

import numpy as np
import xarray as xr
import pandas as pd
import datetime
from tqdm import tqdm

def compute_global_mean(da):
    weights = np.cos(np.deg2rad(da.lat))
    weights.name = "weights"
    temp_weighted = da.weighted(weights)
    global_mean = temp_weighted.mean(("lon", "lat"), skipna=True)
    
    return global_mean


def fraction_positive(da):
    frac = 0.
    return frac


def compute_trends(da, start_year, end_year):
    print('computing trends for ' + str(start_year) + '-' + str(end_year))
    iy = np.where((da["time"]>=start_year) & (da["time"]<=end_year))[0]
    if(len(da.shape)==3):
        da_years = da[iy,:,:]
    elif(len(da.shape)==4):
        da_years = da[:,iy,:,:]
    else:
        raise NotImplementedError()
        
    da_reg = da_years.polyfit(dim="time",deg=1,)["polyfit_coefficients"]
    
    return da_reg


def get_gdp(SHAPE_DIRECTORY, DATA_DIRECTORY, decade):
    regs_shp = pd.read_csv(SHAPE_DIRECTORY + 'ne_10m_admin_0_countries_CSV.csv')  
    country_mask = xr.load_dataarray(SHAPE_DIRECTORY + 'countries_10m_2.5x2.5.nc')

    ## test things worked
    # regs_shp[regs_shp["ADMIN"]=="United States of America"]
    # a = country_mask.where(country_mask==154,np.nan)

    GDP_DIRECTORY = DATA_DIRECTORY + "gdp/"
    gdp_file = GDP_DIRECTORY + "iamc_db_ssp1.csv"
    gdp_raw = pd.read_csv(gdp_file)
    gdp_raw.head()
    gdp = gdp_raw[["Region", str(decade)]]    
    
    return gdp, regs_shp, country_mask


def get_land_mask(filepath, var):
    mask = xr.open_dataset(filepath)[var]
    mask = mask.where(mask >= 50, np.nan, drop=False)*0. + 1
    
    return mask


def get_population(filepath, da_grid):
    inc_lon = np.diff(da_grid["lon"])[0]/2
    inc_lat = np.diff(da_grid["lat"])[0]/2    
    
    da_pop = xr.load_dataarray(filepath)
    da_pop.coords["lon"] = np.mod(da_pop["lon"], 360)
    da_pop = da_pop.sortby(da_pop.lon)
    print(da_pop.sum(("lat","lon"))) 
    
    da_pop_regrid = xr.zeros_like(da_grid[0,0,:,:].squeeze())

    for ilat,lat in tqdm(enumerate(da_grid["lat"].values)):
        for ilon,lon in enumerate(da_grid["lon"].values):
            ilat_pop = np.where((da_pop["lat"]>=da_grid["lat"][ilat]-inc_lat) & (da_pop["lat"]<da_grid["lat"][ilat]+inc_lat))[0]
            ilon_pop = np.where((da_pop["lon"]>=da_grid["lon"][ilon]-inc_lon) & (da_pop["lon"]<da_grid["lon"][ilon]+inc_lon))[0]

            da_pop_regrid[ilat,ilon] = da_pop[ilat_pop,ilon_pop].sum(("lat","lon"))
    
    print(da_pop_regrid.sum(("lat","lon")))     
    
    return da_pop_regrid


def get_data(DATA_DIRECTORY, YEAR_RANGE, N_MEMBERS=None, filenames=None, ssp="119", time_horizon=10):
    
    if filenames is None:
        if ssp=="119":
            filenames = (
                "tas_Amon_ssp119_CNRM-ESM2-1_all_ncecat_ann_mean_2pt5degree.nc",
                "tas_Amon_ssp119_CanESM5_all_ncecat_ann_mean_2pt5degree.nc",
                "tas_Amon_ssp119_GISS-E2-1-G_all_ncecat_ann_mean_2pt5degree.nc",
                "tas_Amon_ssp119_IPSL-CM6A-LR_all_ncecat_ann_mean_2pt5degree.nc",
                "tas_Amon_ssp119_MIROC-ES2L_all_ncecat_ann_mean_2pt5degree.nc",
                "tas_Amon_ssp119_MRI-ESM2-0_all_ncecat_ann_mean_2pt5degree.nc",
                "tas_Amon_ssp119_UKESM1-0-LL_all_ncecat_ann_mean_2pt5degree.nc",
                "tas_Amon_ssp119_MPI-ESM1-2-LR_all_ncecat_ann_mean_2pt5degree.nc",
            )
        elif ssp=="119-x-pre":
            filenames = (
                "tas_day_historical_CanESM5_r1-5_ncecat_yearmax_2pt5degree.nc",
                "tas_day_historical_CNRM-ESM2-1_r1-5_ncecat_yearmax_2pt5degree.nc",
                "tas_day_historical_MIROC-ES2L_r1-5_ncecat_yearmax_2pt5degree.nc",
                "tas_day_historical_MPI-ESM1-2-LR_r1-5_ncecat_yearmax_2pt5degree.nc",
                "tas_day_historical_MRI-ESM2-0_r1-5_ncecat_yearmax_2pt5degree.nc",
                "tas_day_historical_UKESM1-0-LL_r1-5_ncecat_yearmax_2pt5degree.nc",
            )
        elif ssp=="119-x":
            filenames = (
                "tas_day_ssp119_CanESM5_r1-5_ncecat_yearmax_2pt5degree.nc",
                "tas_day_ssp119_CNRM-ESM2-1_r1-5_ncecat_yearmax_2pt5degree.nc",
                "tas_day_ssp119_MIROC-ES2L_r1-5_ncecat_yearmax_2pt5degree.nc",
                "tas_day_ssp119_MPI-ESM1-2-LR_r1-5_ncecat_yearmax_2pt5degree.nc",
                "tas_day_ssp119_MRI-ESM2-0_r1-5_ncecat_yearmax_2pt5degree.nc",
                "tas_day_ssp119_UKESM1-0-LL_r1-5_ncecat_yearmax_2pt5degree.nc",
            )
        elif ssp=="119-x-pre-pr":
            filenames = (
                "pr_day_historical_CanESM5_r1-5_ncecat_yearmax_2pt5degree.nc",
                "pr_day_historical_IPSL-CM6A-LR_r1-5_ncecat_yearmax_2pt5degree.nc",
                "pr_day_historical_MIROC-ES2L_r1-5_ncecat_yearmax_2pt5degree.nc",
                "pr_day_historical_MPI-ESM1-2_r1-5_ncecat_yearmax_2pt5degree.nc",
                "pr_day_historical_MRI-ESM2-0_r1-5_ncecat_yearmax_2pt5degree.nc",
                "pr_day_historical_UKESM1-0-LL_r1-5_ncecat_yearmax_2pt5degree.nc",
            )
        elif ssp=="119-x-pr":
            filenames = (
                "pr_day_ssp119_CanESM5_r1-5_ncecat_yearmax_2pt5degree.nc",
                "pr_day_ssp119_IPSL-CM6A-LR_r1-5_ncecat_yearmax_2pt5degree.nc",
                "pr_day_ssp119_MIROC-ES2L_r1-5_ncecat_yearmax_2pt5degree.nc",
                "pr_day_ssp119_MPI-ESM1-2_r1-5_ncecat_yearmax_2pt5degree.nc",
                "pr_day_ssp119_MRI-ESM2-0_r1-5_ncecat_yearmax_2pt5degree.nc",
                "pr_day_ssp119_UKESM1-0-LL_r1-5_ncecat_yearmax_2pt5degree.nc",
            )
        elif ssp=="126":
            filenames = (
                "tas_Amon_historical_ssp126_CanESM5_r1-10_ncecat_ann_mean_2pt5degree.nc",
                "tas_Amon_historical_ssp126_MIROC6_r1-10_ncecat_ann_mean_2pt5degree.nc",
                "tas_Amon_historical_ssp126_ACCESS-ESM1-5_r1-10_ncecat_ann_mean_2pt5degree.nc",
                "tas_Amon_historical_ssp126_UKESM1-0-LL_r1-10_ncecat_ann_mean_2pt5degree.nc",
                "tas_Amon_historical_ssp126_MIROC-ES2L_r1-10_ncecat_ann_mean_2pt5degree.nc",
                "tas_Amon_historical_ssp126_CNRM-CM6-1_r1-5_ncecat_ann_mean_2pt5degree.nc",
                "tas_Amon_historical_ssp126_CNRM-ESM2-1_r1-5_ncecat_ann_mean_2pt5degree.nc",
                "tas_Amon_historical_ssp126_GISS-E2-1-G_r1-5_ncecat_ann_mean_2pt5degree.nc",
                "tas_Amon_historical_ssp126_IPSL-CM6A-LR_r1-5_ncecat_ann_mean_2pt5degree.nc",
                "tas_Amon_historical_ssp126_MRI-ESM2-0_r1-5_ncecat_ann_mean_2pt5degree.nc",
            )            
        else:
            raise NotImplementedError

    da_all = None
    for file in filenames:
        print(file)
        
        da = xr.open_dataarray(DATA_DIRECTORY + file)
        da['time'] = da["time.year"]
        da = da.sel(time=slice(YEAR_RANGE[0],YEAR_RANGE[1]))     

        try:
            da["member"]
        except:
            da = da.rename({"record": "member"})

        # compute anomalies from first 10 years of SSP
        da = da - da.sel(time=slice(YEAR_RANGE[0],YEAR_RANGE[0]+(time_horizon-1))).mean(('time','member'))
        
        if N_MEMBERS is not None:
            da = da[:N_MEMBERS, :, :, :]
        
        if da_all is None:
            da_all = da
        else:
            da_all = xr.concat([da_all, da],dim="member")
        
    print('da_all.shape = ' + str(da_all.shape))
    return da_all, filenames

    