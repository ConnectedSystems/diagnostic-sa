import sys, os
# dirty hack for dev purposes only
sys.path.insert(0, os.path.abspath(".."))


import numpy as np
import pandas as pd
from SALib.sample.radial.radial_mc import sample as mc_sampler
from settings import *  # import project-specific settings



problem = {
    'num_vars': 1,
    'names': ['Farm___Irrigations___PipeAndRiser___irrigation_efficiency'],
    'bounds': [(0.6, 0.9)]
}

tgt_param = "Farm___Irrigations___PipeAndRiser___irrigation_efficiency"

inbounds = pd.read_csv(indir+'2019-11-06_012547_272b10e9-6383-5514-89bb-6403d8f8c0a7_param_bounds.dat', index_col=0)

# read in previous sample set for a single climate scenario
# we use this as a template
df = pd.read_csv(indir+'example_sample.csv', index_col=0)

# We only need two rows
extremity_df = df.iloc[0:2, :].copy()

# Make both rows identical
extremity_df.iloc[1, :] = df.iloc[0, :]

# Perturb only parameter of interest
indices = extremity_df.index
extremity_df.loc[indices[0], tgt_param] = 0.6
extremity_df.loc[indices[1], tgt_param] = 0.9

extremes = extremity_df.copy()
extremes.to_csv(indir+"roat_extremity_samples.csv")

cat_cols = extremes.select_dtypes('object').columns
numeric_df = extremes.copy()
for col in numeric_df:
    if col in cat_cols:
        numeric_df[col] = numeric_df[col].astype('category')
        numeric_df[col] = numeric_df[col].cat.codes

# export numeric values
numeric_df.to_csv(indir+"roat_extremity_numeric_samples.csv")
