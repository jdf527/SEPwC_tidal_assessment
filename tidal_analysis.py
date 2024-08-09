#!/usr/bin/env python3

# necessary modules imported
import argparse
import os
import numpy as np
import pandas as pd
from scipy.stats import linregress
from matplotlib import dates as mdates

def read_tidal_data(filename):
    """
    Reads tidal data from file and returns a DataFrame.
    
    Parameters:
    filename Path to the tidal data file containing files.
    
    Returns:
    pd.DataFrame: DataFrame containing tidal data with a datetime index and Sea Level as a float.
    """
    data = []
    if os.path.isdir(filename):
        # If a directory is provided, read all files within the directory
        filenames = [os.path.join(filename, f)
                     for f in os.listdir(filename) if f.endswith(".txt")]
    else:
        # If a single file is provided, use that file
        filenames = [filename]

    for filename in filenames:
        df = pd.read_table(filename, delim_whitespace=True, skiprows=11,
                           names=['Cycle', 'Date', 'Time', 'Sea Level', 'Residual'])
        
        df['Time'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%Y/%m/%d %H:%M:%S')
        df.set_index('Time', inplace=True)

        # Replace values ending in M, N, or T with NaN
        df.replace(to_replace=".*[MNT]$", value={'Sea Level': np.nan}, regex=True, inplace=True)
        df['Sea Level'] = df['Sea Level'].astype(float)

        data.append(df)
    
    # Combine all data if reading from a directory
    combined_data = pd.concat(data) if len(data) > 1 else data[0]
    combined_data.sort_index(inplace=True)
    
    return combined_data
    
def extract_single_year_remove_mean(year, data):
    """
    Extracts data for a single year and removes the mean sea level.
    
    Parameters:
    year: The year to extract.
    data: DataFrame containing tidal data.
    
    Returns:
    pd.DataFrame: DataFrame with mean sea level removed for the specified year.
    """
    year_data = data[data.index.year == int(year)].copy()
    mean_sea_level = year_data['Sea Level'].mean()
    year_data['Sea Level'] -= mean_sea_level
    
    return year_data


def extract_section_remove_mean(start, end, data):
    """
    Extracts a section of data and removes the mean sea level.
    
    Parameters:
    start: Start date of the data section.
    end: End date of the data section.
    data: DataFrame containing tidal data.
    
    Returns:
    pd.DataFrame: DataFrame with mean sea level removed for the section.
    """
    section_data = data.loc[start:end].copy()
    mean_sea_level = section_data['Sea Level'].mean()
    section_data['Sea Level'] -= mean_sea_level
    
    return section_data


def join_data(data1, data2):

    return 



def sea_level_rise(data):

                                                     
    return 

def tidal_analysis(data, constituents, start_datetime):


    return 

def get_longest_contiguous_data(data):


    return 

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
                     prog="UK Tidal analysis",
                     description="Calculate tidal constiuents and RSL from tide gauge data",
                     epilog="Copyright 2024, Jon Hill"
                     )

    parser.add_argument("directory",
                    help="the directory containing txt files with data")
    parser.add_argument('-v', '--verbose',
                    action='store_true',
                    default=False,
                    help="Print progress")

    args = parser.parse_args()
    dirname = args.directory
    verbose = args.verbose
    


