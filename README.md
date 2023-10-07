# ML4641_NBA_Betting
Predicting NBA Bet outcomes using ML for ML4641

## Introduction
Using our extensive data collection of NBA betting trends from Dec 2021 to Dec 2022, our team is looking at developing an accurate intelligent tool using basketball betting trends to predict outcomes. The data includes the moneyline betting market, spread, and total bets, as well as the game date, period, and team information such as all quarter scores. Sports wagering has been a thing for many years, with the league being one of the most popular avenues for sports gambling. With such a big market in mind, there is a significant opportunity to develop a Machine Learning (ML) model that can predict outcomes from NBA betting lines with high accuracy.


## Motivation
The main motivation behind the project implement machine learning to accurately predict NBA betting lines to perhaps benefit. The NBA generates a massive amount of data, including player statistics, team performance metrics, injury reports, and historical game results. Leveraging this data to train and test a machine learning model can lead to valuable insights for betting predictions while at the same time improving our machine learning and data analysis skills. We also hope that by creating the model we can enhance our understanding and enjoyment when engaging with the sport.

## Methods
We will use the “NBA Betting Lines” dataset found on [Kaggle](https://www.kaggle.com/datasets/thedevastator/uncovering-hidden-trends-in-nba-betting-lines-20). It includes 341 files of sequential data including won/lost games, complete statistics for all players in the NBA in the 2021-2022 season, some player data from 2012, tip-off stats, as well as points scored per game. We will use each team’s features to analyze which team should be favored when it comes to making a bet on a particular sporting event or match-up. We plan to split the problem into multiple phase focusing on Data collection, Data cleaning, feature engineering, model fitting, and result validation. For our models, we tentatively plan on using Random forest and Support Vector Machine (SVM) but we aren't as experienced with ML and could potentially change the model in the near future as we get more familiar. Furthermore, if additional data is needed, we could also pull extra data available online such as from "Basketball Reference"'s API. For the implmentation, we are planning on either using scikit-learn or pytorch to avoid the intricities of implementing our own algorithms from scratch.

## Potential Results
We expect our model to be able to predict a team’s odds of success in a sporting event with reasonable accuracy given the betting lines and data about the team and players. Given our diverse dataset and that data cleaning is done correctly, our RF and SVM will take multiple teams’ features (scoring history, location, player statistics etc) for training, and then be able to run inference on a particular set of features to predict outcome. When performing validation, accuracy should not drop by a significant amount, ensuring our results are valid for any generalized data.

![gantt](https://drive.google.com/uc?export=view&id=1b2r_xWCzn10PgITWFVW8WeUyWPoCgBVi)

[Video Presentation](https://youtu.be/WkIxE3tXc4o)

## Reference
Walsh, C., & Joshi, A. (2023, June 29). Machine learning for sports betting: Should predictive models be optimised for accuracy or calibration?. arXiv.org. https://arxiv.org/abs/2303.06021 \
\
Bucquet, A., &amp; Sarukkai, V. (2018). The bank is open: Ai in sports gambling. https://cs229.stanford.edu/proj2018/report/3.pdf \
\
Hubáček, O., Železný, F., & Šourek, G. (2019, February 19). Exploiting sports-betting market using machine learning. International Journal of Forecasting. https://www.sciencedirect.com/science/article/pii/S016920701930007X 

