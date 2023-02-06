# Project 4: Wildfire Acreage Prediction

## Table of Contents
* 00_collect_data
  * landcover_data_collection
  * meteorology_data_collection_api_meteostat
  * meteorology_data_collection_api_POWER
  * wildfire_data_collection
* 01_cleaning_eda
  * 01.1_wildfires_cleaning
  * 01.2_meteorology_cleaning
  * 01.3_basic_EDA
  * 01.4_extended_EDA
* 02_processing
  * 02.1_meteorology_historical_preprocessing
  * 02.2_merging_data
* 03_modeling
  * ...

---
## Problem Statement
Using only the reported initial location of a wildfire, can we use the historical and present meteorological data and land cover zoning data to predict the total acres burned? What variability of predicted wildfire acreage could be explained by only meteorological data and vegetation type?

---
## Python Libraries
Following python libraried were used during the project:
  - `pandas`
  - `numpy`
  - `seaborn`
  - `matplotlib`
  - `sklearn`
  - `nltk`
  - `meteostat`
  - `POWER-api`
  - `mpl_toolkits.basemap`
---
## Datasets
During the project, we collected the following data to be used as predictors:
1. Wildfires dataset covering south-western portion of the US
1. Current meteorological data, including atmospheric measurements like temperature, wind, air humidity, soil humidity, UV index etc.
2. Historical precipitation for 6 months preceding the fire start date
3. Land cover data, describing what type of vegetation is the dominant in the start location of the fire
<div style="width:50px; height:50px"></div>
<img src='public/visuals/wildfire_all_locations.png' alt='test' width='50%' height='50% title = 'test'>

---
## Data Collection
 The biggest part of data collection was getting meteorological data. It was acquired using [POWER API](https://power.larc.nasa.gov/docs/methodology/data/sources/), which utilizes space-based data from the meteo satellites. We've also tried using Meteostat API that is using ground-based meteo data, but it's coverage wasn't good enough for our goals.  
 Wildfires data came from [WFIGS Wildland Fire Locations](https://data-nifc.opendata.arcgis.com/datasets/nifc::wfigs-wildland-fire-locations-full-history/about) which are reported by IRWIN wildland fires reporting and management system.  
Land Cover data was collected from [GAP/LANDFIRE National Terrestrial Ecosystems](https://www.usgs.gov/programs/gap-analysis-project/science/land-cover-data-overview) dataset.

---
## Data Cleaning
We did some extensive cleaning of wildfire entries, by removing 'tiny' fires which are less than 1 acre and took less than one day to contain. 
In general data cleaning of weather and wildfires dataset involved removal of missing values, invalid entries and a lot of preprocessing.
Land cover data layer was preprocessed in QGIS, where its resolution was downsampled from 30 meters to 1 kilometer by getting the most frequent land cover category from the source dataset. By spatial intersection of wildfires' starting points and land cover raster, we got the csv file containing land cover category per incident.

---
## EDA
During EDA, we've made sure to explore our data well enough to figure out any patterns. In general, wildfires data we worked with has a lot of variance and it's hard to detect any patterns apart. This is probably why modeling was challenging as well

### Variance of fire data
![Scatter Plot](public/visuals/wildfire_all_size_vs_duration.png)
  
### Seasonality of precipitation and fires:
![Scatter Plot](public/visuals/fire_rain_snow.png)

### Most burned vegetation types:
![Scatter Plot](public/visuals/landcover_most_burned.png)

----
## Modeling
Initially we investigated modeling for the data on all fires, as well as fires filtered to over an acre and lasting longer than 24 hours. The best of those initial models had RMSE values around 6000 acres.  

Next we utilitzed dozens of different machine learning models with extensive parameter tuning on four different train/test sets derived from the filtered fires but with outliers removed. Those train/test sets inlcuded:
- dataset without the categorical feature (landcover_class)
- dataset with the categorical feature dummied
- dataset with the categorical feature dummied but transformed by PCA (to eliminate dimensionality)
- dataset without the categorical feature but transformed by Polynomial Features and then transformed by PCA (to investigate any compounding features but also reduce dimensionality)

The two best models were a stacked ensemble model with a RandomForest Regression, Adaboost Regression, and Lasso Regression as the base estimators and a Linear Regression as the final estimator--all carried out on the dataset without the categorical feature. That model resulted in scores of:  

|RMSE|Training R-Squared|Testing R-Squared|
| :-: | :-: | :-:|
| 62.05 | 0.126 | 0.205 |

Interestingly, the next closest model was a simple linear regression carried out on the same train/test set.  

Next, we generated predictions from the test set and compared to true values for post-model analysis. It seems our model could not predict values under 16.65 acres. Given that the majority of the fires used in the final data were below 15 acres (median was 10.60 acres), this model's inability to correctly predict small fires is the biggest cause of the remaining error inherent in this prediction model. Moreover, the mean our prediction-errors was around 1.96 acres. The over-predictions were averaged with the under-prediction of 338.2 acres in the most extreme case.   
     
### Distribution of True and Predicted Values:
![Histogram](public/visuals/True_vs_Preds.png)
     

Investigating the coefficients from the linear regression (2nd best model) showed the biggest factors it used was wind speed and surface soil wetness (5cm below). These findings makes sense within the context of our investigation. However, it was interesting present rain or past precipiation didn't affect the model as much as the other features.


----
## Conclusion & Recommendation

Based on the wide variety of analysis conducted, we've concluded it is challenging to build a model that could predict how many acres would burn during a wildfire event. There clearly are many factors that can cause a wildfire to spread and burn more than others. For instance, certain terrain such as the desert is dry and arid, yet there usually is not enough vegetation and biomass to spread and cause massive fires. Furthermore, since the direct cause of a fire starting is often by humans and often during a time perfect for wildfires, correctly predicting the size of the resulting fire is nearly impossible with just the initial location.

----

## Future Research

For future investigations, the model could potentially be better at predicting the size of the resulting fire by incorporating:
     
- Accurate Slope Data
- Geography - Human Elements such as roads which would allow quicker human intervention
- Geography - Natural Elements such as lakes, rivers, and steep mountains; giving a native boundary for the fire
- Narrowing the parameters for the investigation (i.e. - An area with only a certain vegetation coverage)

Also, it would be worth investigating modeling/predicting daily fire growth rather than total acres burned. This would allow the incorporation of weather data through the fire (i.e.- the second day might be extremely windy, allowing the fire to spread rapidly. This case would not have been accurately represented by our models in this study).


----



## Data Dictionary

| Features                | Data Types | Description                                                                                                                                                                                                                                                                                                         |
| :---------------------- | :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| T2M                     | float64    | The average air (dry bulb) temperature at 2 meters above the surface of the earth.                                                                                                                                                                                                                                  |
| T2M_MAX                 | float64    | The maximum hourly air (dry bulb) temperature at 2 meters above the surface of the earth in the period of interest.                                                                                                                                                                                                 |
| QV2M                    | float64    | The ratio of the mass of water vapor to the total mass of air at 2 meters (g water/kg total air).                                                                                                                                                                                                                   |
| PRECTOTCORR             | float64    | The bias corrected average of total precipitation at the surface of the earth in water mass (includes water content in snow).                                                                                                                                                                                       |
| WS2M                    | float64    | The average of wind speed at 2 meters above the surface of the earth.                                                                                                                                                                                                                                               |
| WS2M_MAX                | float64    | The maximum hourly wind speed at 2 meters above the surface of the earth.                                                                                                                                                                                                                                           |
| WS10M                   | float64    | The average of wind speed at 10 meters above the surface of the earth.                                                                                                                                                                                                                                              |
| WS10M_MAX               | float64    | The maximum hourly wind speed at 10 meters above the surface of the earth.                                                                                                                                                                                                                                          |
| GWETTOP                 | float64    | The percent of soil moisture a value of 0 indicates a completely water-free soil and a value of 1 indicates a completely saturated soil; where surface is the layer from the surface 0 cm to 5 cm below grade.                                                                                                      |
| GWETPROF                | float64    | The percent of profile soil moisture a value of 0 indicates a completely water-free soil and a value of 1 indicates a completely saturated soil; where profile is the layer from the surface down to the bedrock.                                                                                                   |
| T2MDEW                  | float64    | The dew/frost point temperature at 2 meters above the surface of the earth.                                                                                                                                                                                                                                         |
| T2MWET                  | float64    | Wet Bulb Temperature at 2 Meters                                                                                                                                                                                                                                                                                    |
| RH2M                    | float64    | The ratio of actual partial pressure of water vapor to the partial pressure at saturation, expressed in percent.                                                                                                                                                                                                    |
| CLRSKY_SFC_PAR_TOT      | float64    | Clear Sky Surface PAR Total                                                                                                                                                                                                                                                                                         |
| ALLSKY_SFC_PAR_TOT      | float64    | All Sky Surface PAR Total                                                                                                                                                                                                                                                                                           |
| ALLSKY_SFC_UV_INDEX     | float64    | All Sky Surface UV Index                                                                                                                                                                                                                                                                                            |
| PRECTOTCORR_SUM         |            | Precipitation Corrected Sum                                                                                                                                                                                                                                                                                         |
| tavg                    | float64    | The average air temperature in °C                                                                                                                                                                                                                                                                                   |
| tmin                    | float64    | The minimum air temperature in °C                                                                                                                                                                                                                                                                                   |
| tmax                    | float64    | The maximum air temperature in °C                                                                                                                                                                                                                                                                                   |
| prcp                    | float64    | The daily precipitation total in mm                                                                                                                                                                                                                                                                                 |
| snow                    | float64    | The maximum snow depth in mm                                                                                                                                                                                                                                                                                        |
| wdir                    | float64    | The average wind direction in degrees (°)                                                                                                                                                                                                                                                                           |
| wspd                    | float64    | The average wind speed in km/h                                                                                                                                                                                                                                                                                      |
| wpgt                    | float64    | The peak wind gust in km/h                                                                                                                                                                                                                                                                                          |
| pres                    | float64    | The average sea-level air pressure in hPa                                                                                                                                                                                                                                                                           |
| tsun                    | float64    | The daily sunshine total in minutes (m)                                                                                                                                                                                                                                                                             |
| station                 | float64    | The weather station ID                                                                                                                                                                                                                                                                                              |
| X                       | float64    | Centroid of Latitude                                                                                                                                                                                                                                                                                                |
| Y                       | float64    | Centroid of Longitude                                                                                                                                                                                                                                                                                               |
| ContainmentDateTime     | object     | The date and time a wildfire was declared contained.                                                                                                                                                                                                                                                                |
| ControlDateTime         | object     | The date and time a wildfire was declared under control.                                                                                                                                                                                                                                                            |
| DailyAcres              | float64    | A measure of acres reported for a fire.  More specifically, the number of acres within the current perimeter of a specific, individual incident, including unburned and unburnable islands.  The minimum size must be 0.1.                                                                                          |
| DiscoveryAcres          | float64    | An estimate of acres burning upon the discovery of the fire. More specifically when the fire is first reported by the first person that calls in the fire.  The estimate should include number of acres within the current perimeter of a specific, individual incident, including unburned and unburnable islands. |
| FireCause               | object     | Broad classification of the reason the fire occurred identified as human, natural or unknown.                                                                                                                                                                                                                       |
| FireDiscoveryDateTime   | object     | The date and time a fire was reported as discovered or confirmed to exist.  May also be the start date for reporting purposes.                                                                                                                                                                                      |
| IncidentTypeCategory    | object     | The Event Category is a sub-group of the Event Kind code and description. The Event Category further breaks down the Event Kind into more specific event categories.                                                                                                                                                |
| IncidentTypeKind        | object     | A general, high-level code and description of the types of incidents and planned events to which the interagency wildland fire community responds.                                                                                                                                                                  |
| InitialLatitude         | float64    | The latitude location of the initial reported point of origin specified in decimal degrees.                                                                                                                                                                                                                         |
| InitialLongitude        | float64    | The longitude location of the initial reported point of origin specified in decimal degrees.                                                                                                                                                                                                                        |
| IrwinID                 | object     | Unique identifier assigned to each incident record in IRWIN.                                                                                                                                                                                                                                                        |
| LocalIncidentIdentifier | int64      |                                                                                                                                                                                                                                                                                                                     |
| POOCounty               | object     | The County Name identifying the county or equivalent entity at point of origin designated at the time of collection.                                                                                                                                                                                                |
| POODispatchCenterID     | object     | A unique identifier for the dispatch center that intersects with the incident point of origin.                                                                                                                                                                                                                      |
| POOFips                 | int64      | The code which uniquely identifies counties and county equivalents.  The first two digits are the FIPS State code and the last three are the county code within the state.                                                                                                                                          |
| POOState                | object     | The State alpha code identifying the state or equivalent entity at point of origin.                                                                                                                                                                                                                                 |
| UniqueFireIdentifier    | object     | Unique identifier assigned to each wildland fire.  yyyy = calendar year, SSUUUU = POO protecting unit identifier (5 or 6 characters), xxxxxx = local incident identifier (6 to 10 characters)                                                                                                                       |
| id                      | int64      | Unique ID                                                                                                                                                                                                                                                                                                           |
| Count                      | int64      | Number of pixels with particular value                                                                                                                                                                                                                                                                                                            |
| Value                      | int64      | Unique value of land cover zone                                                                                                                                                                                                                                                                                                            |
| RED                      | float64      | Red channel of given pixel                                                                                                                                                                                                                                                                                                            |
| GREEN                      | float64      | Green channel of given pixel                                                                                                                                                                                                                                                                                                            |
| BLUE                      | float64      | Blue channel of given pixel                                                                                                                                                                                                                                                                                                           |
| CL                      | int64      | Code: Class                                                                                                                                                                                                                                                                                                           |
| NVC_CLASS                      | object      | Class: dominant general growth forms adapted to basic moisture, temperature, and/or substrate or aquatic                                                                                                                                                                                                                                                                                                            |
| SC                      | object      | Code: Subclass                                                                                                                                                                                                                                                                                                           |
| NVC_SUBCL                      | object      |  Subclass: global macroclimatic factors driven primarily by latitide and continental postion, or reflect overriding substrate or  aquatic condtions                                                                                                                                                                                                                                                                                                            |
| FRM                      | object      | Code: Formation                                                                                                                                                                                                                                                                                                           |
| NVC_FORM                      | object      |  Formation: global macroclimatic conditions as modified by altitide, seasonality of precipitation, substrates, hydrological conditions                                                                                                                                                                                                                                                                                                            |
| DIV                      | object      | Code: Division                                                                                                                                                                                                                                                                                                           |
| NVC_DIV                      | object      | Division:  continental differences in mesoclimate, geology, substrates, hydrology, disturbance regimes                                                                                                                                                                                                                                                                                                            |
| MACRO_CD                      | object      | Code: Macrogroup                                                                                                                                                                                                                                                                                                            |
| NVC_MACRO                      | object      | Macrogroup: sub-continental to regional differences in mesoclimate, geology, substrates, hydrology, disturbance regimes                                                                                                                                                                                                                                                                                                            |
| GR                      | object      | Code: Group                                                                                                                                                                                                                                                                                                           |
| NVC_GROUP                      | object      | Group: regional differences in mesoclimate, geology, substrates, hydrology, disturbance regimes                                                                                                                                                                                                                                                                                                            |
| LEVEL3                       | int64      | Code: Level                                                                                                                                                                                                                                                                                                            |
| ECOLSYS_LU                      | object      |  Level description                                                                                                                                                                                                                                                                                                           |
| NVCMES                       | object      |  Code of the sublevel                                                                                                                                                                                                                                                                                                            |