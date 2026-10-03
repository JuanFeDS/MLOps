import pandas as pd

from prefect import task

@task(name='create_df')
def run():
    '''
    Creamos un dataframe dummie 
    '''

    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [1, 2, 3],
        'C': [1, 2, 3]
    })

    return df

if __name__ == '__main__':
    run()