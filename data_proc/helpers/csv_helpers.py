import os
import pandas as pd
from progressbar import progressbar

def combine_csv_dir(dir: str="../data/nba_gamelogs/") -> pd.DataFrame:
    '''Return dataframe of combined gamelogs
    
    Params:
        dir: directory of nba gamelogs
    '''
    df = pd.DataFrame()
    for filename in progressbar(os.listdir(dir)):
        f = os.path.join(dir, filename)
        # checking if it is a file
        if not os.path.isfile(f):
            continue

        df_file = pd.read_csv(f)
        df = pd.concat([df, df_file])
        
    return df