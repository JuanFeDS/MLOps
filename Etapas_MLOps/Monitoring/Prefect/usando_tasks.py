import pandas as pd
from prefect import flow, task

from src import create_df, transform_data, create_another_df, merge_df

@flow(log_prints=True)
def hello_world():
    '''
    Función principal que encapsula nuestro flujo (flow) de trabajo
    '''    
    # Ejecutamos la lógica de nuestro script
    df = create_df.run()
    new_df = transform_data.run(df)

    another_df = create_another_df.run()

    final_df = merge_df.run(new_df, another_df)

if __name__ == '__main__':
    # Ejecutamos nuestro flujo
    hello_world()