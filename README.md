
## Project Summary:
The free online encyclopedia Wikipedia says:
"The term Network Monitoring describes the use of a system that constantly monitors a computer network for slow or failing systems and that notifies the network administrator in case of outages via email, pager or other alarms."

For any company to grow and be successful, it is essential the it  establish a method of monitoring its network activity. This should include solutions that can automatically detect and respond to threats and performance issues in real time, as well as predict possible issues in the future.


## Project Description:
The object of this project is to add the monitoring infrastructure to the data engineering pipeline.  This provides the reporting capability on the capacity and performance of the hardware and applications so you can know when you are running into issues as well use it for forecasting future needs.

## Project Challenge:
1. Learning curve

2. Identifying what needs to be monitored
    * Creating a “visual” map of the most critical parts of the network
    * avoiding information overload

3. Deciding how to measure what is being monitored
   * Setting base lines

## Data Pipeline:   

__Ingestion:__ AWS S3    
__Data Processing:__ Spark   
__Storage:__ MySQL    
__User Interface (UI):__ Flask    


<img src= img/architecture.jpg>

## Monitoring System:

__Display__ Grafana       

__Monitoring System__ Prometheus    

<img src= img/monitor_sys.jpg>

<img src= img/connections_2018-09-30.png>

<img src= img/mysql_2018-09-30.png>


<img src= img/system_use_2018-09-30.png>


<img src= img/alerting_2018-09-30.png>






## Future Work:
* Containerize the monitoring system
* Add caching to the system

## Data Source

[New York City Parking Violations](https://data.cityofnewyork.us/City-Government/Parking-Violations-Issued-Fiscal-Year-2014-August-/jt7v-77mi)

## References:
[Prometheus] (http://prometheus.io/)    
[How to use prometheus ] (https://www.digitalocean.com/community/tutorials/how-to-use-prometheus-to-monitor-your-ubuntu-14-04-server)     
[ How to Install and Secure Grafana] (https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-grafana-on-ubuntu-16-04)      
[mysql_exporter] (https://github.com/prometheus/mysqld_exporter)      
[Monitoring MySQL] (https://dzone.com/articles/monitoring-mysql)       
[Monitoring Read/Write Latency](https://sqlperformance.com/2015/03/io-subsystem/monitoring-read-write-latency)
