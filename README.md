# Route finder
This is a basic **Python route finder** that reads data from an excel file and outputs a shortest route between two nodes using Dijkstra's algorithm. It is best used for a custom *transportation system* as you can specify which line the two nodes belong to, and it will output a readable route between two stations. 

# Features 
- Reads stations and lines data from `stations.xlsx`
- Prompt the user to enter the start and destination stations
- Computes a route between the two stations utilising Dijkstra's algorithm
- Display the final route and the total time taken, plus the total time for each section

# Requirements 
Required dependencies:
- Python
- Pandas

# Modifying the stations.xlsx data file
First, configure stations and lines data: 
- Add all stations codes and station names in the `Station_code` and `Station_name` column
- Similarly, add all line codes and line names in the `Line_code` and `Line_name` column

Then, configure the routes:
- For each line, first add the line code in the `Line` column.
- The first station for each line in the `Station` column always have a `Time` of 0.
- For every station following the line, the `Time` is the travelling time between it and the previous station.
- Start a different line by separating them with a blank row.
- All routes are assumed to be bidirectional.

Example: PIE ---55--- CEN ---25--- TOW ---50--- BEA is represented by 
| Line    | Station | Time
| -------- | ------- | ------- |
| PIEL  | PIE    | 0 |
|   | CEN  | 55 |
|   | TOW  | 25 |
|   | BEA  | 50 |

To configure the units of the numbers provides (such as s, min), add that under the `Time_unit` column

# Running the code
To run the code:
```
python route_finder.py
```

Example output:
```
========================================
Enter start station name / code:bea
Start station: Beach (BEA)
========================================
Enter end station name / code:dep
End station: Depot (DEP)
========================================
****** Route information ******
Beach (BEA) -> Depot (DEP): 150.0 s
****************************************
1. Pier line
> Beach --- Time elapsed: 0 s
> Tower --- Time elapsed: 50.0 s
1 stations, 50.0 s
****************************************
2. Estate line
> Tower --- Time elapsed: 50.0 s
> Park --- Time elapsed: 95.0 s
1 stations, 45.0 s
****************************************
3. City line
> Park --- Time elapsed: 95.0 s
> Castle --- Time elapsed: 115.0 s
> Depot --- Time elapsed: 150.0 s
2 stations, 55.0 s
****************************************
```
