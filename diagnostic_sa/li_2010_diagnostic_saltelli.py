"""Applying GSA to identify inactive parameter."""

from SALib.sample.saltelli import sample as s_sampler
from SALib.analyze.sobol import analyze as s_analyzer

import matplotlib.pyplot as plt
import pandas as pd

from diagnostic_sa.li_2010 import li_2010_case1_inactive
from settings import *


li_case1 = {
    'names': [f'x{i}' for i in range(1, 6)],
    'num_vars': 5,
    'bounds': [[-100.0, 100.0]] * 5
}

s1_val = pd.DataFrame(columns=['S1', 'S1_conf'])

for i in range(2, 100, 2):
    samples = s_sampler(li_case1, i, calc_second_order=False)
    results = li_2010_case1_inactive(*samples.T)
    analysis = s_analyzer(li_case1, results, calc_second_order=False)

    total, first = analysis.to_df()

    num_evals = samples.shape[0]

    s1_val.loc[f"{i} ({num_evals})", :] = first.loc['x4', :]
    # s1_val = s1_val.append(first.loc['x4', :])

print(s1_val)

s1_val.plot(kind='bar', yerr='S1_conf')
fig = plt.gcf()
fig.savefig(f'{FIG_DIR}saltelli_li2010_inactive_x4_results.png', dpi=300, bbox_inches='tight')


# print(samples.shape)

# total, first = analysis.to_df()  # .rename(columns={'mu': '$\\mu$', 'mu_star': '$\\mu*$'})

# # first.plot(kind='bar')
# ax = analysis.plot()

# plt.suptitle("Test")

# # ax = df.loc[:, ['$\\mu$', '$\\mu*$']].plot(kind='bar', 
# #                         title='Number of trials necessary to identify inactive parameter with Morris for Case #1 in Li et al. (2010)',
# #                         rot=0)

# fig = plt.gcf()
# fig.savefig(f'{FIG_DIR}morris_li2010_inactive_saltelli_results.png', dpi=300, bbox_inches='tight')
