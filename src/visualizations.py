import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

def create_grouped_column_rate_df(df, column):
    qty_buildings = df.building_id.nunique()
    df_grouped = df.groupby(column).size().to_frame().rename(columns={0:'count'}).reset_index()
    df_grouped['col_rate'] = (df_grouped['count']/qty_buildings)*100
    return df_grouped.sort_values(by='col_rate', ascending=False)


def join_despreciable_values(df, column, limit=.5):
    df_new = df.copy()
    df_split = df_new.loc[df_new['col_rate']<0.5]
    df_new = df_new.loc[df_new['col_rate']>limit]
    print(f"Los valores de '{column}' que están por debajo del ~{limit}% son: {str(df_split[column].values.tolist())}")
    df_new = df_new.append({column: str(df_split[column].values.tolist()),\
                            'count': df_split['count'].sum(),\
                            'col_rate': df_split['col_rate'].sum()},\
                            ignore_index=True).set_index(column)    
    return df_new


## Anomalies functions  ----------------------------------------------------------------

def find_anomalies(data):
    #define a list to accumlate anomalies
    anomalies = []
    
    # Set upper and lower limit to 3 standard deviation
    data_std = np.std(data)
    data_median = np.median(data)
    anomaly_cut_off = data_std * 3
    
    lower_limit  = data_median - anomaly_cut_off 
    upper_limit = data_median + anomaly_cut_off
    
    # Generate outliers
    for outlier in data:
        if (outlier > upper_limit or outlier < lower_limit) and (outlier not in anomalies):
            anomalies.append(outlier)
    if anomalies:
        print(f"std: {data_std} | median: {data_median} | lower_limit: {lower_limit} | upper_limit: {upper_limit} | ANOMALIES: {anomalies}")
    return anomalies

def get_columns_with_anomalies(df):
    columns_with_anomalies = {}
    for c in df.columns:
        anomalies = find_anomalies(df[c].values.tolist())
        if anomalies:
            columns_with_anomalies[c] = anomalies
    return columns_with_anomalies      
    
## Plot functions --------------------------------------------------------------------------


def plot_column_rate_pie(df, column, limit=.5):
    qty_buildings = df.building_id.nunique()
    df_grouped = create_grouped_column_rate_df(df, column)
    df_grouped_resized = join_despreciable_values(df_grouped, column, limit)
    df_grouped_resized.plot(kind='pie', y='count', autopct='%1.0f%%', explode=[.1 for n in range(1, len(df_grouped_resized)+1)], radius=1, figsize=(15,8))
    plt.legend(loc='best', bbox_to_anchor=(1.5, 1), title=column)
    plt.title(f"Porporción de '{column}' sobre {qty_buildings} edificaciones relevadas tras el terremoto Gorkha 2015")
    
    
def plot_column_boxplot(df, column):
    qty_buildings = df.building_id.nunique()
    fig, ax = plt.subplots(figsize=(15,10))
    sns.boxplot(data=df, x=column, color='pink', ax=ax)
    ax.set_title(f"Boxplot de '{column}' sobre {qty_buildings} edificaciones relevadas en relacion al terremoto Gorkha", fontsize=14)
    ax.set_xlabel(column, fontsize=14)
    
    
def plot_anomalies_with_function(df, columns_with_anomalies):
    for column, anomalies in columns_with_anomalies.items():
        values = np.array(df[column])
        values_unique, counts = np.unique(values, return_counts=True)

        size = (counts-counts.min())/(counts.max()-counts.min())*10000

        colors = ['blue' if value not in anomalies else 'red' for value in values_unique ]

        plt.rcParams.update({'font.size': 18, 'figure.figsize': [15, 10]})
        plt.title(f"Distribucion de valores de '{column}' | Evidencia de valor anómalo")
        plt.axhline(1, color='k', linestyle='--')
        plt.scatter(values_unique, np.ones(len(values_unique)), s = size, color=colors)
        plt.xlabel(f'Valores de {column}')
        plt.ylabel(f'Relevancia')
        plt.yticks([])
        plt.show()       