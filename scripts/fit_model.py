#!/usr/bin/env bash

from fermipy.gtanalysis import GTAnalysis


# data preparation
gta = GTAnalysis('configuration.yaml', logging={'verbosity': 3})
gta.setup()

# recommended three rounds of optimization
OPTIMIZATION_ROUNDS = 3
_ = [ gta.optimize() for i in range(OPTIMIZATION_ROUNDS)]

gta.print_roi()

# free normalization of all sources within 3 deg of ROI center
gta.free_sources(distance=5.0,pars=['norm', 'Prefactor', 'alpha', 'beta', 'Index', 'Eb', 'Index1',
                                    'Index2', 'Expfactor'])

# free all parameters of isotropic and galactic diffuse components
gta.free_source('galdiff')
gta.free_source('isodiff')

# free sources with TS>10
gta.free_sources(minmax_ts=[10,None],pars=['norm', 'Prefactor'])
gta.free_source('2FGLJ0547.1+0020c')

# model fit, first round.
gta.write_roi('fit_model_0')

# print ROI and model parameters and refit
gta.print_roi()
gta.print_params()
gta.fit()

# write ROI
gta.write_roi('fit_model')
