import numpy as np
import pandas as pd

# Sample data
# Each column represents a distribution
state = np.random.RandomState(51423)
data = state.rand(20, 8).cumsum(axis=0).cumsum(axis=1)[:, ::-1]
data = data + 20 * state.normal(size=(20, 8)) + 30
data = pd.DataFrame(data, columns=np.arange(0, 16, 2))
data.columns.name = 'column number'
data.name = 'variable'

# Calculate error data
# Passed to 'errdata' in the 3rd subplot example
means = data.mean(axis=0)
means.name = data.name  # copy name for formatting
fadedata = np.percentile(data, (5, 95), axis=0)  # light shading
shadedata = np.percentile(data, (25, 75), axis=0)  # dark shading

import proplot as pplt
import numpy as np

# Loop through "vertical" and "horizontal" versions
varray = [[1], [2], [3]]
harray = [[1, 1], [2, 3], [2, 3]]
for orientation, array in zip(('vertical', 'horizontal'), (varray, harray)):
    # Figure
    fig = pplt.figure(refwidth=4, refaspect=1.5, share=False)
    axs = fig.subplots(array, hratios=(2, 1, 1))
    axs.format(abc='A.', suptitle=f'Indicating {orientation} error bounds')

    # Medians and percentile ranges
    ax = axs[0]
    kw = dict(
        color='light red', edgecolor='k', legend=True,
        median=True, barpctile=90, boxpctile=True,
        # median=True, barpctile=(5, 95), boxpctile=(25, 75)  # equivalent
    )
    if orientation == 'horizontal':
        ax.barh(data, **kw)
    else:
        ax.bar(data, **kw)
    ax.format(title='Bar plot')

    # Means and standard deviation range
    ax = axs[1]
    kw = dict(
        color='denim', marker='x', markersize=8**2, linewidth=0.8,
        label='mean', shadelabel=True,
        mean=True, shadestd=1,
        # mean=True, shadestd=(-1, 1)  # equivalent
    )
    if orientation == 'horizontal':
        ax.scatterx(data, legend='b', legend_kw={'ncol': 1}, **kw)
    else:
        ax.scatter(data, legend='ll', **kw)
    ax.format(title='Marker plot')

    # User-defined error bars
    ax = axs[2]
    kw = dict(
        shadedata=shadedata, fadedata=fadedata,
        label='mean', shadelabel='50% CI', fadelabel='90% CI',
        color='ocean blue', barzorder=0, boxmarker=False,
    )
    if orientation == 'horizontal':
        ax.linex(means, legend='b', legend_kw={'ncol': 1}, **kw)
    else:
        ax.line(means, legend='ll', **kw)
    ax.format(title='Line plot')