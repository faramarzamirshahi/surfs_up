# surfs_up
Weather analysis with sqllite
# Overview
To further assist W. Avy with the weather analysis, we create descriptive statistics on temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

# Results
To perform our analysis we do the following steps:
1- Create an engine to our database
`engine = create_engine("sqlite:///hawaii.sqlite")`
2- Reflect an existing database into a new model
`Base = automap_base()`
3- Reflect the tables
`Base.prepare(engine, reflect=True)`
3- Create references to each table
```
Measurement = Base.classes.measurement
Station = Base.classes.station
```
4- Create our session (link) from Python to the DB
`session = Session(engine)`

5- Query the database for the temperatures in the month of June and December
`june = session.query(Measurement.date,Measurement.tobs).filter(extract('month', Measurement.date) == 6)`
`december = session.query(Measurement.date,Measurement.tobs).filter(extract('month', Measurement.date) == 12)`

6- Convert the results into list
```
june = june.all()
december = december.all()
```
7- Create pandas dataframe on each list
```
juneDF = pd.DataFrame(june, columns=['date','temperature'])
decemberDF = pd.DataFrame(december, columns=['date','temperature'])
```
8- Gather descriptive stats on each dataframe
`juneDF.describe()`
![temperature statistics for the month of June](Resources/june_temp_stats_AllStations.png)
`decemberDF.describe()`
![temperature statistics for the month of June](Resources/december_temp_stats_AllStations.png)


# Summary
The comparison between temperatures for the months of June and December show little variance
![June and december temperatures](Resources/June_and_december_temp_stats_AllStations.png)


We also analyzed the average temperature and precipitations over the years
`SurfsUp_AdditionalAnalysis.ipynb`

![Oahu average temperatures over years](Resources/TempOverYears.png)
We notice minor temperature difference between June and December with average temperatures over 70
![Oahu average precipitations over years](Resources/PrcpOverYears.png)
We notice that apart from year 2010 the average precipations do not change much between June and December