import sys, os
# dirty hack for dev purposes only
sys.path.insert(0, os.path.abspath(".."))


import numpy as np
import pandas as pd
from SALib.sample.radial.radial_mc import sample as mc_sampler
from settings import *  # import project-specific settings


tgt_param = "Farm___Irrigations___PipeAndRiser___irrigation_efficiency"
problem = {
    'num_vars': 1,
    'names': [tgt_param],
    'bounds': [(0.6, 0.9)]
}

# Create MC samples (p+1)*n
# SALib expects purely numeric values so categoricals are transformed as such
roat_samples = mc_sampler(problem, 10, seed=101)


inbounds = pd.read_csv(indir+'2019-11-06_012547_272b10e9-6383-5514-89bb-6403d8f8c0a7_param_bounds.dat', index_col=0)

# read in previous sample set for a single climate scenario
# we use this as a template
df = pd.read_csv(indir+'example_sample.csv', index_col=0)

# Make 20 identical rows (10*(p+1) = 20)
roat_df = df.iloc[0, :].copy()
roat_df = roat_df.to_frame().T
roat_df = pd.DataFrame(np.repeat(roat_df.values,20,axis=0))

roat_df.columns = df.columns

# Perturb only parameter of interest
roat_df.loc[roat_df.index, tgt_param] = roat_samples.flatten()

targeted = roat_df.copy()
targeted.to_csv(indir+"roat_targeted_samples.csv")

targeted = targeted.infer_objects()

# Convert non-numeric inputs into categorical integer values
cat_cols = targeted.select_dtypes('object').columns

numeric_df = targeted.copy()
for col in numeric_df:
    if col in cat_cols:
        numeric_df[col] = numeric_df[col].astype('category')
        numeric_df[col] = numeric_df[col].cat.codes

# export numeric values
numeric_df.to_csv(indir+"roat_targeted_numeric_samples.csv")
