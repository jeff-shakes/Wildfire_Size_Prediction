# Project 1: Reddit: Web API & NLP


## Table of Contents
- [Project 1: Reddit: Web API \& NLP](#project-1-reddit-web-api--nlp)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Problem-Statement](#problem-statement)
  - [Datasets](#datasets)
  - [Analysis Summary](#analysis-summary)
    - [Overall Data Analysis](#overall-data-analysis)
  - [Conclusion \& Recommendation](#conclusion--recommendation)

## Overview


Data Analysis has been conducted using following libraries:
  - `pandas`
  - `numpy`
  - `seaborn`
  - `matplotlib`
  - `skylearn`
    - `BaggingClassifier`
    - `RandomForestClassifier`
    - `ExtraTreesClassifier`
    - `GradientBoostingClassifier`
    - `AdaBoostClassifier`
    - `VotingClassifier`
    - `StackingClassifier`
    - `confusion_matrix`
    - `ConfusionMatrixDisplay`
    - `classification_report`
    - `RocCurveDisplay`
    - `accuracy_score`
    - `Pipelin`
    - `train_test_split`
    - `GridSearchCV`
    - `cross_val_score`
    - `cross_val_predict`
    - `make_column_transformer`
    - `StandardScaler`
    - `MultinomialNB`
    - `LogisticRegression`
    - `KNeighborsClassifier`
    - `CountVectorizer` 
    - `TfidfVectorizer`
  - `nltk`
    - `SentimentIntensityAnalyzer`
    - `PorterStemmer`
  - `meteostat`
  - `POWER-api`


## Problem-Statement


## Datasets
| Features     | Data Types | Description                   |
| :----------- | :--------- | :---------------------------- |
| selftext     | object     | Post body text                |
| title        | object     | Post title                    |
| score        | int64      | User upvote to downvote ratio |
| domain       | object     | Subreddit domain              |
| id           | object     | User unique identification    |
| author       | object     | Username                      |
| num_comments | int64      | Number of comments            |
| url          | object     | Url used on a post            |
| created_utc  | int64      | Post posted timestamp         |
| subreddit    | int64      | Subreddit name                |


---

## Analysis Summary

### Overall Data Analysis

![Price Distribution](./presentation/charts/models_performance.png)
Model `performance` comparison to determine which model should be picked for modeling



----
## Conclusion & Recommendation
