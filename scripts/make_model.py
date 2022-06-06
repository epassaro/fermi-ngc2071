#!/usr/bin/env bash
# Based on: https://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/binned_likelihood_tutorial.html

import subprocess


def to_cmd(params):
    return [f"{k}={v}" if k != "bin" else v for k,v in params.items()]

# README: https://github.com/fermi-lat/fermitools-fhelp/blob/master/fhelp_files/gtselect.txt
gtselect = { "bin": "gtselect",
             "evclass": 128,
             "evtype": 3,
             "infile": "@events.txt",
             "outfile": "ngc2071_filtered.fits",
             "ra": 86.7683,
             "dec": 0.3636,
             "rad": 20.0,
             "tmin": 239557417,
             "tmax": 302227202,
             "emin": 100,
             "emax": 300000,
             "zmax": 90, }

# README: https://github.com/fermi-lat/fermitools-fhelp/blob/master/fhelp_files/gtmktime.txt
gtmktime = { "bin": "gtmktime",
             "scfile": "spacecraft.fits",
             "filter": "(DATA_QUAL>0)&&(LAT_CONFIG==1)",
             "roicut": "no",
             "evfile": "ngc2071_filtered.fits",
             "outfile": "ngc2071_filtered_gti.fits", }

# README: https://github.com/fermi-lat/fermitools-fhelp/blob/master/fhelp_files/gtvcut.txt
gtvcut = { "bin": "gtvcut",
           "infile": "ngc2071_filtered_gti.fits",
           "table": "EVENTS", }

# README: https://fermi.gsfc.nasa.gov/ssc/data/analysis/user/readme_make4FGLxml.txt
make4FGLxml = ["python", 
               "make4FGLxml.py", 
               "gll_psc_v30.fit", 
               "ngc2071_filtered_gti.fits"]

subprocess.run(to_cmd(gtselect), capture_output=True, check=True)
subprocess.run(to_cmd(gtmktime), capture_output=True, check=True)
subprocess.run(to_cmd(gtvcut), capture_output=True, check=True)
subprocess.run(make4FGLxml, capture_output=True, check=True)
