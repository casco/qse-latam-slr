import pandas as pd
import re
import string

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
                   'Brasil',
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
        items=['Document Title', 'Authors', 'Author Affiliations', 'Publication Title', 'Publication Year', 'Abstract'], axis=1)
    ieee_df.rename(inplace=True,
                   columns={'Document Title': 'title', 'Authors': 'authors', 'Author Affiliations': 'affiliations',
                            'Publication Title': 'publication', 'Publication Year': 'year', 'Abstract': 'abstract'})
    return ieee_df


def df_from_scopus_csv_file(file):
    scopus_df = pd.read_csv(file)
    scopus_df = scopus_df.filter(items=['Title', 'Authors', 'Affiliations', 'Source Title', 'Year', 'Abstract'], axis=1)
    scopus_df.rename(inplace=True, columns={'Title': 'title', 'Authors': 'authors', 'Affiliations': 'affiliations',
                                            'Source Title': 'publication', 'Year': 'year', 'Abstract': 'abstract'})
    return scopus_df


def detect_countries(text):
    text = re.sub(re.escape('Brasil'), 'Brazil', text, flags=re.IGNORECASE)
    detected_countries = [country for country in LATAM_COUNTRIES if country.lower() in text.lower()]
    return detected_countries


def inject_detected_countries_to(dfs):
    dfs['countries'] = dfs['affiliations'].apply(detect_countries)


def mark_duplicates_in(df):
    df['title_canonical'] = (df['title'].str.lower().str.replace(' ', '', regex=True)
                             .str.replace('[{}]'.format(string.punctuation), '', regex=True))
    df_duplicates = df[df['title_canonical'].duplicated(keep=False)]
    df['is_duplicate'] = ''
    df.loc[df_duplicates.index, 'is_duplicate'] = 'duplicate'
