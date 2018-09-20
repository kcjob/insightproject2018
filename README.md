

## Project Summary:
The free online encyclopedia Wikipedia says:
"The term Network Monitoring describes the use of a system that constantly monitors a computer network for slow or failing systems and that notifies the network administrator in case of outages via email, pager or other alarms."

For any company to grow and be successful, it is essential the it  establish a method of monitoring its network activity is essential to. This should include solutions that can automatically detect and respond to threats and performance issues in real time, as well as predict possible issues in the future.


## Project Description:
The object of this project is to setup the infrastructure needed by a Data Engineer
who in turn will create the environment for the application used by a Data Scientist to do the analysis stated above

Additionally, adding some resiliency around the database will ensure if for example, there is a problem passing data to the database which causes it to crash, the system automatically compares the Write Ahead Log (WAL) against a buffer and inserts the difference into the database. Once this is done, the system restarts itself.

## Project Challenge:
1. Identifying the best buffering software
2. Writing drivers that will write data to both MySQL and and ?? simultaneously
3. Figuring out how to check Write Ahead Log (WAL) against buffered data and insert the difference into MySQL
4. Restart the uploading process between Spark and MySQL

## Solution

Write some drivers that will copy the data being add to the main (MySQL) database to a back-up database (redis) which will be used to update any missing data in the main database after the restart.   


## Data Pipeline:   

__Ingestion:__ AWS S3    
__Data Processing:__ Spark   
__Storage:__ MySQL    
__User Interface (UI):__ Flask    

## Monitoring System:

__Display__ Grafana
__Monitoring System__ Prometheus


<img src= img/architecture.jpg>

<img src= img/architecture.jpg>


## Data Source

[New York City Parking Violations](https://data.cityofnewyork.us/City-Government/Parking-Violations-Issued-Fiscal-Year-2014-August-/jt7v-77mi)
