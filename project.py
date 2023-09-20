# Main python file used for benchmarking sorting algorithms.
# Code sourced and adapted from <https://learnonline.gmit.ie/pluginfile.php/579189/mod_resource/content/0/CTA_Project.pdf>
# and lecture notes <https://learnonline.gmit.ie/course/view.php?id=5341>
# and <https://realpython.com/sorting-algorithms-python/>


# Import python packages.
# Randint to help generate random numbers.
from random import randint

# Using time to record time complexity.
import time

# Pandas for working with dataframes.
import pandas as pd

# This is used for data visualisation. 
import matplotlib.pyplot as plt

# Import individual py function files for my sorting algorithms.
import bubble_sort
import merge_sort
import counting_sort
import insertion_sort
import quick_sort


# Main function for benchmarking the sorting algorithims.
def benchmarking(algorithms, n, runs):
    # Variables to append results to. 
    time_taken = [] 
    sizes_used =[] 
    trial_runs =[] 
    sort_type =[] 
    # Loop for each algorithm.
    for sort_algo in algorithms:       
        # Loop to run each size in array to each algorithm.
        for size in n:
            # Loop again to do it 10 times.
            for run in range(runs):
                # call function below to generate random numebrs to use.
                nums = get_random_array(size)                
                # Select each algo to monitor time. 
                algorithm = algorithms[sort_algo]
                # Use time method to record start time.
                start_time = time.time()
                # Call the algo after start time recorded.
                algorithm(nums)
                # Record the end time.
                end_time = time.time()
                # Subtract to get the time elapsed and by 1000 to return it in milliseconds.
                difference = (end_time - start_time)* 1000 
                # Save results to var above. 
                time_taken.append(difference)               
                # Record the amount of runs in the var above.
                trial_runs.append(run+1)
                # Add the size used for each to var above.
                sizes_used.append(size)
                # And record the algo name for each.
                sort_type.append(sort_algo) 
    # Using pandas to create a dataframe of results from the four variables above.           
    df = pd.DataFrame({"Sort":sort_type, "Size":sizes_used, "Times":time_taken, "trialNo":trial_runs})
    return df


# Seperate function to generate random numbers. 
def get_random_array(n):
    array = []
    for i in range(0, n, 1):
        # Append random numbers to an array to use for benchmarking. 
        array.append(randint(0, 100))
    return array


# A function to calculate averages of benchmarking process.
def mean_for_each(df):
    # Set index as size column.
    df.set_index('Size', inplace=True)
    # Using mean and round to get averages and groupby the sort and size.
    avg_speeds = (df.iloc[:, 0:2].groupby(['Sort','Size']).mean()).round(3)
    # Using unstack method to change format of dataframe.
    return avg_speeds.unstack()
    

# A function to plot the data. 
def plot_the_benchmarks(df2):
    # Set the figure size.
    plt.rcParams["figure.figsize"]=(10,5)
    #T.plot to plot multiple series on on plot. 
    df2.T.plot(lw=1 , marker='.', markersize=5, alpha=0.5)
    plt.title('Benchmarking Sorting Algorithms')
    plt.ylabel("Running time in Milliseconds")
    plt.xlabel("Array Size")
    #plt.show()
    # Save plot as png file.
    plt.savefig('plot.png')


# Main function called when program is run. 
def main():
    # List of algos importing them from their seperate py files.
    algorithms = {"Bubble Sort": bubble_sort.bubble_sort,"Insertion Sort":insertion_sort.insertion_sort,"Merge Sort":merge_sort.merge_sort, 
                "Quick Sort":quick_sort.quick_sort, "Counting Sort": counting_sort.counting_sort}
    # Array sizes for each algo. 
    n = [100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000]
    # Call the main function using the algos, array sizes and 10 runs for each.
    benchmark = benchmarking(algorithms, n, 10)
    # Storing the average running times in a new df.
    df2 =  mean_for_each(benchmark)
    # Renamaing the axis to none to remove the sort heading for the algorithims.
    df2.rename_axis(None, inplace=True)
    # Dropping the sizes down a level so that Size heading is above the algos with the sizes horizontally across the table.
    df2.columns = df2.columns.droplevel()
    # Saving the df2 to a csv in order to create a table of console results. 
    df2.to_csv('averages'+'.csv')
    # Print df to console.
    print(df2)    
    # Call function to plot df2.
    plot_the_benchmarks(df2) 


# Will only run when it reaches the main function. 
if __name__ == "__main__":
    main()