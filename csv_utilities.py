import pandas as pd

LATAM_COUNTRIES = ['Belize',
                   'Costa Rica',
                   'El Salvador',
                   'Guatemala',
                   'Honduras',
                   'Mexico',
                   'Nicaragua',
                   'Panama',
                   'Argentina',
                   'Bolivia',
                   'Brazil',
                   'Chile',
                   'Colombia',
                   'Ecuador',
                   'French Guiana',
                   'Guyana',
                   'Paraguay',
                   'Peru',
                   'Suriname',
                   'Uruguay',
                   'Venezuela',
                   'Cuba',
                   'Dominican Republic',
                   'Haiti',
                   'Guadeloupe',
                   'Martinique',
                   'Puerto Rico',
                   'Saint-Barthélemy',
                   'Saint-Martin']


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


def detect_countries(text):
    detected_countries = [country for country in LATAM_COUNTRIES if country in text]
    return detected_countries


def inject_detected_countries_to(dfs):
    dfs['countries'] = dfs['affiliations'].apply(detect_countries)
