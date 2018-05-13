#!/bin/bash

export RADICAL_PILOT_DBURL=
export RADICAL_PILOT_PROFILE=True
export RADICAL_ENMD_PROFILE=True
export RADICAL_ENMD_PROFILING=1
export RP_ENABLE_OLD_DEFINES=True

export RADICAL_ENTK_VERBOSE='DEBUG'
export RADICAL_SAGA_VERBOSE='DEBUG'
export RADICAL_PILOT_VERBOSE='DEBUG'

# Activate, export PATH, etc.

python afe-dummy.py &> rp.session.log
