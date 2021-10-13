# climate_query_sqlalchemy

Using SQLAlchemy ORM queries, Pandas, and Matplotlib, an analysis was conducted for temperature and precipitation measurements with queries into dates, date ranges, and locations of a climate database. A precipitation analysis was conducted by querying 12 months of precipitation data and plotted within a chart for the date ranges marked by precipitation in Inches. Calculations were conducted for a Station Analysis to inquire on the most active station in the dataset(i.e. the station with the highest number of observations). Using that Station ID, calculations were conducted to find the lowest, highest and average temperature for a years time of station data and plotted within a histogram for temperature ranges on a y-axis of frequency counts. <a href="https://github.com/cspence001/climate_query_sqlalchemy/blob/main/climate_starter.ipynb">climate query</a>

Based on the queries developed a  <a href="https://github.com/cspence001/climate_query_sqlalchemy/blob/main/climate_app.py">Flask based API</a> was created for data exploration within the range of dates.

Two alternative Temperature analysis were conducted and are contained within the Bonus folder: </br>
<ul>
<li>The first, <a href="https://github.com/cspence001/climate_query_sqlalchemy/blob/main/Bonus/Temp_Analysis_I.ipynb">Temperature Analysis I</a> compares temperature averages in Hawaii for the months of June in December and runs Statistic tests to determine if there is a meaningful difference in temperature between the two seasons, known that Hawaii is reputed to have mild weather year-round. [Temp_Analysis_I.ipynb] </br></li>
<li>The second <a href="https://github.com/cspence001/climate_query_sqlalchemy/blob/main/Bonus/Temp_Analysis_II.ipynb">Temperature Analysis II</a>, conducts a study looking into the historical data for a selected week of August to compare temperatures in previous years for the week. A calculation for minimum, maximum, and average temperature were queried and plotted into a bar chart. For that same week, a Daily Rainfall Average analysis was conducted and plotted into an area plot to show the daily normals for each date in the week with calculations of a=minimum, maximum, and average precipitation measurements.[Temp_Analysis_II.ipynb]</br></li>
</ul>

The [Resources] folder contains two csv files for the data, hawaii_measurements.csv and stations_measurements.csv both join on Station.
