# I am following the structure of the code in this article to learn how to create scatter plots using Python's Atlair library:
# https://towardsdatascience.com/creating-interactive-scatter-plots-with-python-altair-e4b47e0aa8eb

# NOTE: I am choosing to keep csv rows with NA values as part of the data that is read into the pandas dataframe.

import pandas as pd
import altair as alt

column_list = ["species", "bill_length_mm", "flipper_length_mm", "body_mass_g"]
species_domain = ["Adelie", "Chinstrap", "Gentoo"]
species_color_range = ["#FF9013", "#9932CC", "#048B8C"]

dataframe = pd.read_csv(
    "penglings.csv",
    usecols=column_list,  # Select only subsets of columns from the csv file, which allows for more efficient file reading.
    na_filter=False,  # Do not filter data rows with NA values.
    nrows=345
)

alt.Chart(dataframe).mark_circle(radius=40).encode(
    alt.X("Flipper Length (mm)"),
    alt.Y("Body Mass (g)"),
    alt.Color("species",
              scale=alt.Scale(domain=species_domain, range=species_color_range),
              legend=alt.Legend(
                  title="species",
                  orient='right',
                  titleFontSize=15,
                  labelFontSize=12))
).properties(
    height=385, width=580
).configure_axis(
    titleFontSize=20,
    labelFontSize=15
)
