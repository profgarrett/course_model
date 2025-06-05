# Python Functions

## Learning Outcomes

By the end of this section, you will be able to:

- Create basic plots such as scatter plots, line plots, and histograms using Seaborn.
- Visualize relationships between variables with functions like `sns.relplot`, `sns.scatterplot`, and `sns.lineplot`.
- Display distributions of data using `sns.histplot`, `sns.kdeplot`, and `sns.distplot`.
- Use categorical plots such as `sns.boxplot`, `sns.violinplot`, and `sns.stripplot` to compare groups.
- Customize plot appearance with Seaborn themes, color palettes, and style options.
- Combine multiple plots using Seaborn's FacetGrid and multi-plot functions.

## Seaborn Plot Code Samples

### Bar Plot

A bar plot displays the mean (or other estimator) of a quantitative variable for each category. Major options include `x` and `y` for variable assignment, `hue` for grouping, and `estimator` to change the summary statistic (default is mean). You can also control error bars with `ci` and change the color palette with `palette`.

```python
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
sns.barplot(x='day', y='total_bill', data=tips, hue='sex', ci='sd', palette='pastel')
plt.show()
```

### Line Plot

A line plot shows the relationship between two variables, typically with one as a continuous variable. Use `x` and `y` for axes, `hue` for grouping, and `style` or `markers` for line style and point markers. The `ci` option controls confidence intervals, and `palette` sets the color scheme.

```python
sns.lineplot(x='size', y='total_bill', data=tips, hue='sex', style='sex', markers=True, ci=None)
plt.show()
```

### Jointplot

A jointplot displays the relationship between two variables along with their marginal distributions. The `kind` parameter controls the type of plot in the joint area (e.g., 'scatter', 'reg', 'hex', 'kde'). You can set `height` for figure size and pass additional keyword arguments to customize the marginal or joint plots.

```python
sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg', height=6)
plt.show()
```

### Distribution Plot

A distribution plot (histogram or KDE) visualizes the distribution of a single variable. Use `kind` in `displot` to choose between 'hist', 'kde', or 'ecdf', and set `bins` for histogram bin count. The `hue` parameter allows for grouping, and `multiple` controls how distributions are stacked or layered.

```python
sns.displot(tips['total_bill'], kind='hist', bins=20, kde=True, color='skyblue')
plt.show()
```

### Violin Plot

A violin plot combines a boxplot and a kernel density plot to show the distribution of a variable across categories. Use `x` and `y` for axes, `hue` for grouping, and `split=True` to show split violins for each hue level. The `inner` parameter controls the display of box, stick, or quartile lines inside the violin.

```python
sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True, inner='quartile', palette='muted')
plt.show()
```

### Pairplot

A pairplot creates a matrix of scatterplots for all pairs of variables in a DataFrame, with histograms or KDEs on the diagonal. Use `hue` to color by category, `kind` to choose between 'scatter' and 'reg', and `diag_kind` for the diagonal plots ('auto', 'hist', or 'kde'). The `palette` option customizes colors, and `markers` can set marker styles for each category.

```python
sns.pairplot(tips, hue='sex', kind='scatter', diag_kind='kde', palette='coolwarm')
plt.show()
```

## Practice Problems

- TBD
