"""Experimental settings

Functions
---------
get_settings(experiment_name)
"""

__author__ = "Elizabeth A. Barnes and Noah Diffenbaugh and Patrick Keys"
__date__   = "20 May 2022"


def get_settings(experiment_name):
    experiments = {  
        #---------------------- MAIN SIMULATIONS ---------------------------
        "exp0": { 
            "ssp" : "119",             #[options: '126' or '119']
            "netzero_year" : 2056,            
            "focus_year" : 2056,
            "time_horizon" : 10,            
            "n_members" : 5,
            "filenames" : None,
            "warming_cutoff" : 0.01,
            "plot_member" : 12,
            "gdp_year" : 2060,
            "pop_year" : 2060,
        },    
        
        "exp1": { 
            "ssp" : "119",             #[options: '126' or '119']
            "netzero_year" : 2056,            
            "focus_year" : 2025,
            "time_horizon" : 10,            
            "n_members" : 5,
            "filenames" : None,
            "warming_cutoff" : 0.01,
            "plot_member" : 8,  
            "gdp_year" : 2030,
            "pop_year" : 2030,            
        },            
        
        "exp2": { 
            "ssp" : "126",             #[options: '126' or '119']
            "netzero_year" : 2076,            
            "focus_year" : 2076,
            "time_horizon" : 10,            
            "n_members" : 5,
            "filenames" : None,
            "warming_cutoff" : 0.01,    
            "plot_member" : 8,            
            "gdp_year" : 2080,
            "pop_year" : 2080,               
        },       
        
        "exp3": { 
            "ssp" : "126",             #[options: '126' or '119']
            "netzero_year" : 2076,            
            "focus_year" : 2025,
            "time_horizon" : 10,            
            "n_members" : 5,
            "filenames" : None,
            "warming_cutoff" : 0.01,    
            "plot_member" : 10,            
            "gdp_year" : 2030,
            "pop_year" : 2030,               
        },            
        
        
    }
    
    exp_dict = experiments[experiment_name]
    exp_dict['exp_name'] = experiment_name

    return exp_dict

