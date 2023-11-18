import pandas as pd


def df_from_ieee_csv_file(file):
    ieee_df = pd.read_csv(file)
    ieee_df = ieee_df.filter(
        items=['Document Title', 'Authors', 'Author Affiliations', 'Publication Title', 'Publication Year'], axis=1)
    ieee_df.rename(inplace=True,
                   columns={'Document Title': 'title', 'Authors': 'authors', 'Author Affiliations': 'affiliations',
                            'Publication Title': 'publication', 'Publication Year': 'year'})
    return ieee_df


def df_from_scopus_csv_file(file):
    scopus_df = pd.read_csv(file)
    scopus_df = scopus_df.filter(items=['Title', 'Authors', 'Affiliations', 'Source Title', 'Year'], axis=1)
    scopus_df.rename(inplace=True, columns={'Title': 'title', 'Authors': 'authors', 'Affiliations': 'affiliations',
                                            'Source Title': 'publication', 'Year': 'year'})
    return scopus_df
