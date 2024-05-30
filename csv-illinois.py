import pandas as pd

df = pd.read_csv('datasets/restaurants-with-menus-utf8.csv')

# Dictionary mapping state abbreviations to full state names
state_abbrev_to_name = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
    'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
    'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
    'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
    'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
    'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
}

# Function to extract state abbreviation from full address
def extract_state(full_address):
    if isinstance(full_address, str):
        try:
            return full_address.split(',')[-2].strip().split()[-1]
        except IndexError:
            return None
    return None

df['state_abbrev'] = df['full_address'].apply(extract_state)
df['state'] = df['state_abbrev'].map(state_abbrev_to_name)
df.drop('state_abbrev', axis=1, inplace=True)

print(df['state'].value_counts())


df_illinois = df[df['state'] == 'Illinois']
df_illinois.to_csv('datasets/restaurants-with-menus-utf8-illinois.csv', index=False)