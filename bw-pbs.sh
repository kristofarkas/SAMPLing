#!/bin/bash

export RADICAL_PILOT_DBURL=
export RADICAL_PILOT_PROFILE=True
export RADICAL_ENMD_PROFILE=True
export RADICAL_ENMD_PROFILING=1
export RP_ENABLE_OLD_DEFINES=True

export RADICAL_ENTK_VERBOSE='DEBUG'
export RADICAL_SAGA_VERBOSE='DEBUG'
export RADICAL_PILOT_VERBOSE='DEBUG'

export WORKDIR="/u/sciteam/farkaspa"
export PATH="$WORKDIR/miniconda2/bin:$PATH"
export LD_LIBRARY_PATH="$WORKDIR/miniconda2:$LD_LIBRARY_PATH"

python abigail-single.py &> rp.session.log
