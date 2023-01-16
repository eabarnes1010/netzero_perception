"""Experimental settings

Functions
---------
get_settings(experiment_name)
"""

__author__ = "Elizabeth A. Barnes and Noah Diffenbaugh and Patrick Keys"
__date__ = "20 May 2022"


def get_settings(experiment_name):
    experiments = {
        # ---------------------- MAIN SIMULATIONS ---------------------------
        "exp0": {
            "ssp": "119",  # [options: '126' or '119']
            "netzero_year": 2056,
            "focus_year": 2056,
            "time_horizon": 10,
            "n_members": 5,
            "filenames": None,
            "warming_cutoff": 0.01,
            "plot_member": 12,
            "gdp_year": 2060,
            "pop_year": 2060,
        },

        "exp1": {
            "ssp": "119",  # [options: '126' or '119']
            "netzero_year": 2056,
            "focus_year": 2025,
            "time_horizon": 10,
            "n_members": 5,
            "filenames": None,
            "warming_cutoff": 0.01,
            "plot_member": 8,
            "gdp_year": 2030,
            "pop_year": 2030,
        },

        "exp2": {
            "ssp": "126",  # [options: '126' or '119']
            "netzero_year": 2076,
            "focus_year": 2076,
            "time_horizon": 10,
            "n_members": 5,
            "filenames": None,
            "warming_cutoff": 0.01,
            "plot_member": 8,
            "gdp_year": 2080,
            "pop_year": 2080,
        },

        "exp3": {
            "ssp": "126",  # [options: '126' or '119']
            "netzero_year": 2076,
            "focus_year": 2025,
            "time_horizon": 10,
            "n_members": 5,
            "filenames": None,
            "warming_cutoff": 0.01,
            "plot_member": 10,
            "gdp_year": 2030,
            "pop_year": 2030,
        },

        "exp4": {
            "ssp": "119",  # [options: '126' or '119']
            "netzero_year": 2056,
            "focus_year": 2056,
            "time_horizon": 10,
            "n_members": 5,
            "filenames": None,
            "warming_cutoff": 0.01,
            "plot_member": 12,
            "gdp_year": 2060,
            "pop_year": 2060,
        },

        # ---------------------- 20 years instead of 10--------------------
        "exp20": {
            "ssp": "119",  # [options: '126' or '119']
            "netzero_year": 2056,
            "focus_year": 2056,
            "time_horizon": 20,
            "n_members": 5,
            "filenames": None,
            "warming_cutoff": 0.01,
            "plot_member": 12,
            "gdp_year": 2065,
            "pop_year": 2060,
        },

        "exp21": {
            "ssp": "119",  # [options: '126' or '119']
            "netzero_year": 2056,
            "focus_year": 2025,
            "time_horizon": 20,
            "n_members": 5,
            "filenames": None,
            "warming_cutoff": 0.01,
            "plot_member": 8,
            "gdp_year": 2035,
            "pop_year": 2030,
        },

        "exp22": {
            "ssp": "126",  # [options: '126' or '119']
            "netzero_year": 2076,
            "focus_year": 2076,
            "time_horizon": 20,
            "n_members": 5,
            "filenames": None,
            "warming_cutoff": 0.01,
            "plot_member": 8,
            "gdp_year": 2080,
            "pop_year": 2080,
        },

        "exp23": {
            "ssp": "126",  # [options: '126' or '119']
            "netzero_year": 2076,
            "focus_year": 2025,
            "time_horizon": 20,
            "n_members": 5,
            "filenames": None,
            "warming_cutoff": 0.01,
            "plot_member": 10,
            "gdp_year": 2030,
            "pop_year": 2030,
        },

        "exp24": {
            "ssp": "119",  # [options: '126' or '119']
            "netzero_year": 2056,
            "focus_year": 2056,
            "time_horizon": 20,
            "n_members": 5,
            "filenames": None,
            "warming_cutoff": 0.01,
            "plot_member": 12,
            "gdp_year": 2060,
            "pop_year": 2060,
        },

        # ---------------------- 30 years instead of 10--------------------
        "exp30": {
            "ssp": "119",  # [options: '126' or '119']
            "netzero_year": 2056,
            "focus_year": 2056,
            "time_horizon": 30,
            "n_members": 5,
            "filenames": None,
            "warming_cutoff": 0.01,
            "plot_member": 12,
            "gdp_year": 2070,
            "pop_year": 2070,
        },

        "exp31": {
            "ssp": "119",  # [options: '126' or '119']
            "netzero_year": 2056,
            "focus_year": 2025,
            "time_horizon": 30,
            "n_members": 5,
            "filenames": None,
            "warming_cutoff": 0.01,
            "plot_member": 8,
            "gdp_year": 2040,
            "pop_year": 2040,
        },

        "exp32": {
            "ssp": "126",  # [options: '126' or '119']
            "netzero_year": 2076,
            "focus_year": 2076,
            "time_horizon": 30,
            "n_members": 5,
            "filenames": None,
            "warming_cutoff": 0.01,
            "plot_member": 8,
            "gdp_year": 2090,
            "pop_year": 2090,
        },

        "exp33": {
            "ssp": "126",  # [options: '126' or '119']
            "netzero_year": 2076,
            "focus_year": 2025,
            "time_horizon": 30,
            "n_members": 5,
            "filenames": None,
            "warming_cutoff": 0.01,
            "plot_member": 10,
            "gdp_year": 2040,
            "pop_year": 2040,
        },

        "exp34": {
            "ssp": "119",  # [options: '126' or '119']
            "netzero_year": 2056,
            "focus_year": 2056,
            "time_horizon": 30,
            "n_members": 5,
            "filenames": None,
            "warming_cutoff": 0.01,
            "plot_member": 12,
            "gdp_year": 2070,
            "pop_year": 2070,
        },


        # ---------------------- LARGE ENSEMBLES ---------------------------

        "exp50": {
            "ssp": "119",  # [options: '126' or '119']
            "netzero_year": 2056,
            "focus_year": 2056,
            "time_horizon": 10,
            "n_members": 50,
            "filenames": ('tas_Amon_ssp119_CanESM5_all_ncecat_ann_mean_2pt5degree.nc',),
            "warming_cutoff": 0.01,
            "plot_member": 12,
            "gdp_year": 2060,
            "pop_year": 2060,
        },

        "exp51": {
            "ssp": "119",  # [options: '126' or '119']
            "netzero_year": 2056,
            "focus_year": 2025,
            "time_horizon": 10,
            "n_members": 50,
            "filenames": ('tas_Amon_ssp119_CanESM5_all_ncecat_ann_mean_2pt5degree.nc',),
            "warming_cutoff": 0.01,
            "plot_member": 8,
            "gdp_year": 2030,
            "pop_year": 2030,
        },

        "exp52": {
            "ssp": "119",  # [options: '126' or '119']
            "netzero_year": 2056,
            "focus_year": 2056,
            "time_horizon": 10,
            "n_members": 24,
            "filenames": ('tas_Amon_ssp119_MPI-ESM1-2-LR_all_ncecat_ann_mean_2pt5degree.nc',),
            "warming_cutoff": 0.01,
            "plot_member": 12,
            "gdp_year": 2060,
            "pop_year": 2060,
        },

        "exp53": {
            "ssp": "119",  # [options: '126' or '119']
            "netzero_year": 2056,
            "focus_year": 2025,
            "time_horizon": 10,
            "n_members": 24,
            "filenames": ('tas_Amon_ssp119_MPI-ESM1-2-LR_all_ncecat_ann_mean_2pt5degree.nc',),
            "warming_cutoff": 0.01,
            "plot_member": 8,
            "gdp_year": 2030,
            "pop_year": 2030,
        },
        # ---------------------- PREINDUSTRIAL ---------------------------

        "exp100": {
            "ssp": "126",  # [options: '126' or '119']
            "netzero_year": 1876,
            "focus_year": 1850,
            "time_horizon": 10,
            "n_members": 5,
            "filenames": None,
            "warming_cutoff": 0.01,
            "plot_member": 8,
            "gdp_year": 1900,
            "pop_year": 1900,
        },

        "exp101": {
            "ssp": "119-x-pre",  # [options: '126' or '119']
            "netzero_year": 1876,
            "focus_year": 1850,
            "time_horizon": 10,
            "n_members": 5,
            "filenames": None,
            "warming_cutoff": 0.01,
            "plot_member": 8,
            "gdp_year": 1900,
            "pop_year": 1900,
        },
        "exp102": {
            "ssp": "119-x",  # [options: '126' or '119']
            "netzero_year": 2056,
            "focus_year": 2025,
            "time_horizon": 10,
            "n_members": 5,
            "filenames": None,
            "warming_cutoff": 0.01,
            "plot_member": 8,
            "gdp_year": 2030,
            "pop_year": 2030,
        },

    }

    exp_dict = experiments[experiment_name]
    exp_dict['exp_name'] = experiment_name

    return exp_dict
