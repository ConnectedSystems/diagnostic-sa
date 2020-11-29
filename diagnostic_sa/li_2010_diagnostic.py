from SALib.sample.morris import sample as m_sampler
from SALib.analyze.morris import analyze as m_analyzer

import matplotlib.pyplot as plt
import pandas as pd

from diagnostic_sa.li_2010 import li_2010_case1
from settings import *


li_case1 = {
    'names': [f'x{i}' for i in range(1, 6)],
    'num_vars': 5,
    'bounds': [[-100.0, 100.0]] * 5
}

samples = m_sampler(li_case1, 2)
results = li_2010_case1(*samples.T)
analysis = m_analyzer(li_case1, samples, results)

df = analysis.to_df().rename(columns={'mu': '$\\mu$', 'mu_star': '$\\mu*$'})
ax = df.loc[:, ['$\\mu$', '$\\mu*$']].plot(kind='bar', 
                        title='Unexpected Morris results for Case #1 in Li et al. (2010)\n(n=2, N=12)',
                        rot=0,
                        xlabel='Parameters')

fig = plt.gcf()
fig.savefig(f'{FIG_DIR}morris_li2010_example_results.png', dpi=300, bbox_inches='tight')
