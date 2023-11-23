import spacy


# spacy.cli.download('en_core_web_sm')

# Function to extract countries using SpaCy
# It does not really extract countries but also cities; not really useful for our case
def extract_countries(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    countries = [ent.text for ent in doc.ents if ent.label_ == 'GPE']  # GPE: Geopolitical Entity
    return countries


def inject_countries_to(dfs):
    dfs['countries'] = dfs['affiliations'].apply(extract_countries)

# %%
