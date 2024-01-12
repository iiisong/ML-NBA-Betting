![image](https://github.com/iiisong/ML4641_NBA_Betting/assets/60973363/b5112a47-ef67-4b23-8bba-fbf31992d91a)
# ML4641_NBA_Betting
Predicting NBA Bet outcomes using ML for ML4641

[old intro](intro.md)
[midterm check](midterm.md)

## Table of Contents
1. [Introduction](#intro)
2. [Problem Definition](#problem)
3. [Motivation](#motivation)
4. [Methods Introduction](#intro_methods)
5. [Data Visualization](#datavis)
6. [Motivation](#methods)
7. [Results and Discussion](#results)
8. [Testing](#testing)
9. [Midterm Contribution Table](#mct)
10. [Bibliography and Sources](#bib)

<a id="intro"> </a>
## Introduction
In the past couple years with sports betting services like DraftKings, Sports betting is an increasingly popular pastime for Americans with 46% of all adults having placed a bet in the last year. Alongside the rapid growth of popularity also comes along the rapid growth of the market. Valued at 242 billion dollars, sports betting is an increasingly lucrative business in the modern era. 

The moneyline odds, also known as American odds, provides the league with an insanely popular method for sports wagering. Moneyline betting is a two-way market that is focused on a single game between the two teams: the favorite receives a negative value while the underdog gets a positive value. With this billion-dollar industry in mind, our team realizes the significant part that accurate intelligent tools can play in the betting market, and want to try our hand at developing a prediction model for this purpose. Machine learning models would not only be highly relevant, they would also be well fed from the glut of data from this highly visible and documented industry.

<a id="problem"></a>
## Problem Definition
Alongside the NFL, the NBA is an extremely popular avenue for sports betting and one which we would be focusing on in this project. ML models would be highly relevant and well fed with data as this market is highly visible and well documented. The motivation behind the project is to develop an intelligent tool to use in the betting market. To do this, the model would have to consider many different factors of the teams and games of previous seasons to better understand the inner logistics of the market and produce the winning team. Therefore, we want to carefully examine the most important insights and features of both of the teams with regards to data pertaining to injury reports, past game results, player statistics, and other team metrics to make our model answer the big question: should we take the bet?

To tackle this, we focus on predicting the score differential of the teams that play in a given game and determining whether or not to place bets on the provided betting lines. An accurate result using past game statistics and bets on games where the predicted score differential is greater than the projected score differential would be highly valuable to an individual in the betting market especially within the “spread” style of betting which we would elaborate later. 


<a id="motivation"> </a>
## Motivation
The motivation behind the project is to develop an intelligent tool to use in the betting market. To do this, the model would have to consider many different factors of the teams and games of previous seasons to better understand the inner logistics of the market and produce the winning team. In the NBA Betting Line, the negative value associated with the favored team is how much money the better has to put in in order to receive a net profit of $100. On the other hand, the positive value of the underdog team is how much the better could earn if they bet $100. This creates a market where the favored team has more of a probability of winning, but the underdog has the possibility of a larger payout. Although the “favored” team has the better odds, nothing is set in stone. A number of different reasons could cause the underdog to rise in the game. That is the fun in the world of sports betting. Therefore, we want to carefully examine the most important insights and features of both of the teams with regards to data pertaining to injury reports, past game results, player statistics, and other team metrics to make our model answer the big question: *should we take the bet?*


<a id="intro_methods"> </a>
## Methods Introduction
We will use the ["gambling_stuff"](https://github.com/jimtheflash/gambling_stuff) dataset on Github from the user jimtheflash which was found as the original source of the “NBA Betting Lines” dataset found on [Kaggle](https://www.kaggle.com/datasets/thedevastator/uncovering-hidden-trends-in-nba-betting-lines-20). It includes 341 files of sequential data including won/lost games, complete statistics for all players in the NBA in the 2021-2022 season, some player data from 2012, tip-off stats, as well as points scored per game. We will use each team’s features to analyze which team should be favored when it comes to making a bet on a particular sporting event or match-up.

During data processing, the main issue was with the very large and widely scoped datasets in the “gambling_stuff” Github site. We used the pandas library to retrieve the most relevant information to start off with our basic models. We made our own csv files with pertinent information that could help with prediction model accuracy. Since the dataset includes over 9600 games (excluding the exhibition games), we decided to only use statistics per team instead of individual player data. First, we unified basic game information into a single file for easy access. Then, we added features that included final scores with both team IDs and the winner, game IDs, away team win probability, away team spreads, away team totals, and the rolling win percentages of the past 25, 50, 75, and 100 games. Later on, we also extrapolated the rolling statistics of every single stat for each team over the previous 25, 50, 75, and 100 games before the game. 

The reason we focus on rolling data is because to predict outcomes of future games, we are limited by the stats we have before the game so we do not have access to the actual stats of that game. Essentially, instead of being provided with the statistics of the game we have to predict, we need to predict the data of the game. While there are many ways to do this of varying difficulty, one relatively simple method is by the rolling average, or the average of the previous specified number of entries not including itself. Especially in a world as fast-paced and ever changing as the NBA, rolling averages are pretty suitable as it gets a good estimate of the stats for a team in a future game by taking only recent games into account. By having a maximum rolling average of 100 games, or 1.25 seasons roughly, it gets a good projection of the stats while still being relatively relevant in terms of data recency.

<a id="datavis"> </a>
## Data Visualization

Using the available data for the team statistics, we created multiple tools for visualization and assessing patterns in the data. One of the main useful visualizations is to compare rolling stats between teams for an incoming game. The most primitive of these is the point-scored scatterplot. Through plotting the points scored by team 1 and team 2 throughout all 9600+ games, we can see that the distribution of scores is very expected, with it huddled around the y=x axis. No game has equal points, however, due to the lack of a tie in basketball.

![y/ppg](https://media.discordapp.net/attachments/1181806486398181446/1181807550849613957/image.png?ex=6582670d&is=656ff20d&hm=b880461cfac2b4fc4eb4cd94e1968587c525241427005760eb0435986ac14a38&=&format=webp&quality=lossless&width=2592&height=808)

While the distribution seems mostly normal, the distribution of points is in-fact not precisely unimodal. Better viewed through the contour graphs of point distribution, the centers of the contour graph actually hovers a bit away from the y=x.

![fig2](https://media.discordapp.net/attachments/1181806486398181446/1181807551139041392/image.png?ex=6582670d&is=656ff20d&hm=36ea25b7eb633f974d6d117bf0cf40ed4cc0aeebcafeac8a359d54c8cf15082a&=&format=webp&quality=lossless&width=2592&height=806)

When plotting the results of the histogram of absolute score differentials, the bimodal nature of point distribution becomes extremely clear. Mostly result from the playing nature of basketball, where teams who are behind tend by a decent bit during the last few minutes tend to reduce effort in order to load manage (also termed as “garbage time”) while teams that are close in points usually spend extra effort to cover the difference, it is clearly not unimodal.

![fig](https://media.discordapp.net/attachments/1181806486398181446/1181807551415853136/image.png?ex=6582670d&is=656ff20d&hm=cdff647e5961e7315698c11751d8f68bba3d4245702f5d8be4aa9c9fc6efd2a9&=&format=webp&quality=lossless&width=2592&height=800)

Though it may be harder to see in a point histogram, the histogram is slightly flattened at the top than if it was more normal.

![fig](https://media.discordapp.net/attachments/1181806486398181446/1181807551705251980/image.png?ex=6582670d&is=656ff20d&hm=b12e8ff6a6b1bb65e11142c6843d2a3356b2cde1962aa87edd4023f506ddc23b&=&format=webp&quality=lossless&width=2592&height=804)


While points are important and “the” way to determine the victors is by points, there is more than basketball than just points. With 20 specific stats in box-scores including points, we can see a rough idea of the impact each stat has on winning percentage by plotting the rolling average of the box-score to the win percentage.

To start off, with the most obvious, the connection between the rolling average of wins is easily correlated with the probability of winning the next game.

![fig](https://media.discordapp.net/attachments/1181806486398181446/1181807552128897024/image.png?ex=6582670d&is=656ff20d&hm=624feda16f9cea58332d91cabdd5bf8031dc35d9e36e3efcc52d0efb7dbd9048&=&format=webp&quality=lossless&width=2592&height=796)

While this is relatively straightforward, not all stats are as straightforward as it is. For other stats such as 3 point percentage, the slope is less obvious.
![fig](https://cdn.discordapp.com/attachments/1181806486398181446/1181817383611019344/image.png?ex=65827035&is=656ffb35&hm=3c9af4a2e3d0a5500bc0a1f278f1aba0f904795fdd82174ee2917221fc104a4a&)

Some statistics, like defensive rebounds, may be harder to identify because of its low variance so the outliers have less data to work with.

![fig](https://cdn.discordapp.com/attachments/1181806486398181446/1181817386437980230/image.png?ex=65827036&is=656ffb36&hm=501bdf0c52f23fd8a19a33853cc39680edea5cead7a4ebc69d89daa89ee39bfe&)

While comparing teams with the same data in a scatterplot, the effect of each statistic could be seen relatively easily.

![fig](https://media.discordapp.net/attachments/1181806486398181446/1181807596043247657/image.png?ex=65826717&is=656ff217&hm=763f95ba437a735017a9322f21afb9def462f9e5fb5424c14e1e32b5326e302b&=&format=webp&quality=lossless&width=2592&height=804)

One method we used consisted of preprocessing the points scored by the teams each year and labeling each team ID as a different cluster. Consequently, we were able to create a mapping of each year to a set of corresponding games and their final scores per team. This result is plotted in the following figure:

![fig](https://cdn.discordapp.com/attachments/1181806486398181446/1181808641775501382/image.png?ex=65826811&is=656ff311&hm=6551707c0ce6fa38dc190bcdb66d83547291bd2cc6b110a054cd517e2ebcea63&)

To find relevant patterns and features, it is important to consider games that more directly impact betting/money lines. As a result, it is important to combine game data with betting line data from the additional datasets in our project. We computed a weighted score for each team (per year), and removed data points that resulted in smaller values. This way, we can now visualize more meaningful scores and identify trends:

![fig](https://cdn.discordapp.com/attachments/1181806486398181446/1181808642278830100/image.png?ex=65826811&is=656ff311&hm=8cecafb5ce733d36a1cb33f49ac1bf834f92f04b4632ef0ccb343fd28ab7e4fa&)
![fig](https://cdn.discordapp.com/attachments/1181806486398181446/1181808642656325713/image.png?ex=65826811&is=656ff311&hm=36575f56576c007081da2d9adc8bc643304b31456081da84b83ee6afa468b37c&)

In these plots, we visualize the weighted score per team (y-axis) per year (x-axis). It now becomes much easier to understand how the data has evolved over time, as well as what we can (and should) expect from fitting a model for prediction across different time periods.

Another important aspect of visualization is understanding the correlation that exists in the data by considering the player features as a set of impactful variables for determining a game’s outcome. This is because in each game, the performance of the team is in part determined by the current players that are part of it, each having a different set of statistics and rankings. As a result, we compute each player’s performance score as a function of their gaming history, consisting of average points per game, weight, height and ranking. We call this score “prob_model” since it models a player’s performance probability as a function of their features. To ensure that this score is a representative measure, we compare it against actual historical data of past game results. This ensures that the data we use for fitting our model correctly correlates with ground truth data.

![fig](https://cdn.discordapp.com/attachments/1181806486398181446/1181808642991849512/image.png?ex=65826811&is=656ff311&hm=ce558f11b48036ec5c8248934e71631f3dde48d03eb2772f84d032eca8ea725b&)

This graph shows the computed performance score against historical data. The graph shows that our representation correctly correlates with player statistics. Similarly, we can then visualize the correlation between player performance score and historical data records:

![fig](https://cdn.discordapp.com/attachments/1181806486398181446/1181808643306434662/image.png?ex=65826811&is=656ff311&hm=a8dbf0f45d0c8f0670f8f200d282a14287feface8fb3ab6ed33c443a053cd50b&)
![fig](https://cdn.discordapp.com/attachments/1181806486398181446/1181808643608432650/image.png?ex=65826811&is=656ff311&hm=ad2a541a82b69babfa2e118ab7fedf829b92e6fe6380c3a13782925d2c204fa5&)

While player data could be extremely useful for our model, for the sake of time, we ended up not incorporating player data into our model instead of just aggregating all player data per game into general team data.

<a id="methods"> </a>
## Methods

With many features to consider, we decided to use basic linear regression as a first model with our processed data. For an initial validation, we ran linear regression using both team IDs, away team win probability, away spread, and away total to predict the score differential of the actual game outcome. With five features, we had a MSE of 156 and a coefficient of determination of 0.21. We felt that it was a good start, but it was only a start.

We needed more relevant features to use if we really wanted to get anywhere. We also had the goal of removing betting line information itself from the input dataset. This is where the data preprocessing was important, and we were able to retrieve many relevant features from the original raw data as well as extrapolate some of our own, such as the overall rolling win percentages of the games in the past 35, 50, 75, and 100 games.
In that vein, we decided to step away from our initial linear regressions and introduce Support Vector Machine Regression using the polynomial kernel as our final model. We fit the model many times with our various features, experimenting with including game IDs as a feature and various kernel shapes. We processed our data further and created rolling statistics of rebounds, assists, steals, free throws percentage, and field goal percentages per team. 

We further employed data augmentation techniques to ensure we were using meaningful data to train our models. In the realm of SVMs, one powerful technique we were able to utilize was the kernel method. The kernel trick is able to work in a feature space implicitly as opposed to explicitly computing every coordinate of the higher-dimensional space. In this case, we used the player performance score “prob_model” and weighted it based on how recently that score was obtained in the player’s game history (using time data in the dataset). We refer to this new axis as the “Net Rating”. We show our results in a 3D-plot:

![fig](https://cdn.discordapp.com/attachments/1181806486398181446/1181808664542199968/image.png?ex=65826816&is=656ff316&hm=6bbc510da5bfef54a5b3d865360503a57a7bee8c8b221c559af065e807751cac&)

The plot effectively shows that introducing the Kernel Method can further improve the separability and classification of our data.
We processed the team statistics for each game based on boxscores. We validate the boxscores by using the primitive graph method to detect outliers and manually remove errors. Then, we connect the datasets together through the game IDs using a dictionary to map the two sets of NBA and SBR data. We ended up with multiple csv files that specified basic final scores, betting lines, box scores, and team statistics. The combined data into the master file contains around 260 features total.

Our main processed dataset used rolling averages over a specified number of entries to create a relatively decent estimate for the statistics of the game. This metric considers the fact that teams in the NBA change players a lot, so getting an average better captures the team. By having a maximum rolling average of 100 games (1.26 seasons roughly), it gets a good projection of the stats while still being relatively relevant in recent years.


<a id="results"> </a>
## Results and Discussion

A key metric we are using to analyze our model’s performance is The coefficient of determination (R2). It measures the percentage of the variation that the model explains. Essentially, the higher the R2 value, the better the regression fits the observed data. In the middle of development, we saw that we were getting extremely low (<.15) R2 values that would sometimes even be negative, which was counter-intuitive and pointed to the fact that there was most likely a bug within the processed data. We realized that there was a problem with the way we were processing the dataset: games would be listed twice because there would be one home listing and one away listing. We solved the issue by overwriting the away listing with the corresponding home listing, when we ran into it.
Another metric that we also used to evaluate the performance of the model was the Max Error which measures the maximum residual error between the predicted and actual values in a dataset. The usage of the max error as evaluation of the model gave us insight on where the model produced the largest deviation for a particular sample (in the data set). In other words, it allowed us to see what outliers in the data set caused the model to perform significantly worse than how it otherwise would have.
Using SVMs, we found that the shape of the kernel used yielded no large discrepancy between cross validation accuracy. This is indicative of a data shape that has no particular bias toward a shape, so we stuck with the polynomial kernel.


<a id="testing"> </a>
## Testing
We experimented with three linear regression models to predict score differentials in NBA games.

### **Model 1**
Model 1 Features: Team 2 rebounds, Team 2 assists, Team 2 steals

Metrics:
- Mean squared error: 133.29108
- Root Mean Squared Error: (RMSE): 11.54518
- Coefficient of determination (R2): 0.28487

Here we fit a model using only features corresponding to one team. Unsurprisingly, the model was not highly accurate due to the limited amount of information used to train the model.

Visualizations:
![mod1](https://media.discordapp.net/attachments/1146619129793617970/1173829000297185310/image.png?ex=65656072&is=6552eb72&hm=772fa45e40873044db4fbdc8da7703bd21751df742f6779aeccdf79fa60ee7b3&=&width=1824&height=1402)

This graph gives a sense of how accurate the model was at predicting the score differential. Since the actual values are plotted against the predicted values, a highly accurate graph would follow a linear pattern since the x and y value should be roughly the same. We can see the model does not follow a strong linear pattern due to the fairly low accuracy. We also noted an outlier in the graph when x is equal to 0, which could be caused by an error in our processed data. The broken outlier points have been removed later on.

![mod1res](https://media.discordapp.net/attachments/1146619129793617970/1173829404296744960/image.png?ex=656560d2&is=6552ebd2&hm=57eaf1dee8789ccfda022bbb207c480f6cef548e6d1aa78563d655364d1ce6a9&=&width=1826&height=1402)

This residual graph plots the predicted value subtracted by the actual value. This graph is useful in seeing the error in our model, since the distance from each point to the red line shows the error in the model’s prediction for that point. Essentially, a model with low error tends to maintain the points close to y=0.

### Model 2
Model 2 Features: Team 2 rebounds, Team 2 assists, Team 2 steals, Team 1 rebounds, Team 1 assists, Team 1 steals, Team 1 free throw percentage, Team 2 free throw percentage

Metrics:
- Mean Squared Error: 90.97132
- Root Mean Squared Error: (RMSE): 9.53789
- Coefficient of determination (R2): 0.57036

Here we can see an improvement over the previous model. The RMSE is about 17% less than the first model. The R2 value also significantly improved, essentially doubling from the first model. These improvements in the model’s ability to predict can be explained by incorporating features that correspond to both of the playing teams instead of just one. We also included an additional game metric which we believed would help make the model more accurate.

Visualizations:
![mod2](https://media.discordapp.net/attachments/1146619129793617970/1173829404577767455/image.png?ex=656560d2&is=6552ebd2&hm=037e569cf82ef5e1fc14b894cf589a551d7ccb8e46b7c877b6baaaa4ba32b84e&=&width=1858&height=1402)

The linear trend of this graph shows that the model tends to make accurate predictions. Since the predicted models tend to be close to the actual values, we see a linear correlation in the data, showing the model is able to make accurate predictions. This is a major improvement from model 1 which does not have a linear trend in the same graph. The broken outlier points have been removed later on.

![mod2r](https://media.discordapp.net/attachments/1146619129793617970/1173829404904931328/image.png?ex=656560d2&is=6552ebd2&hm=5abd320deb08c5c1387fe5f858370a7459e591814daaac58a04bd0da3d845109&=&width=1942&height=1402)

The majority of data points in the residual plot tend to be around y = 0 which is what is expected for this graph. We can also see that there are no extreme outliers in the graph.

### Model 3
Model 3 Features: Team 2 rebounds, Team 2 assists, Team 2 steals, Team 1 rebounds, Team 1 assists, Team 1 steals, Team 1 Free throw percentage, Team 2 free throw percentage, Team 1 Field goal percentage, Team 2 Field goal percentage

Metrics:
- Mean Squared Error: 76.43589
- Root Mean Squared Error (RMSE): 8.74276
- Coefficient of determination (R2): 0.63558

This model outperformed both Model 1 and Model 2. The model achieved a low RMSE meaning the average error in the model did not drastically deviate from the true value. The R2 value indicates that roughly 63% of the variance in the data can be explained with our model. We achieved our goal of finding a model with an R2 > 0.5. We saw an 11% increase in the R2 score compared to model 2 and an 8% decrease in the RMSE compared to model 2. The reason this model outperforms the others is because of the features used to train the model. We included 5 key game metrics from each team which gave the model enough data to predict the score differential within a reasonable margin of error.

Analytics:
![mod3](https://media.discordapp.net/attachments/1146619129793617970/1173829404577767455/image.png?ex=656560d2&is=6552ebd2&hm=037e569cf82ef5e1fc14b894cf589a551d7ccb8e46b7c877b6baaaa4ba32b84e&=&width=1858&height=1402)

The strong linear correlation shows the high accuracy of the model. We can clearly see the data tends to follow the line y = x better than the previous two models. There are no data points that are far from the line which means the model predicted all points reasonably close to the actual value.
![mod3r](https://media.discordapp.net/attachments/1146619129793617970/1173829423796080670/image.png?ex=656560d7&is=6552ebd7&hm=7ffdf5134b85cb0f81039e6e3ee79e9c65bd2a4821093bdd2bed9ba62a0fc6c8&=&width=1856&height=1402)

You can also see that for this graph, the majority of the data points are located around the y-axis = 0 which is what we expected for since the features for this model produced the highest coefficient of determination


We also show the correlation between our initial player performance score calculated from player features and the actual prediction results. We compute the “prob” score vs “prob_ground_truth” (top right), “prob_model” vs “prob_ground_truth” (bottom left), as well as the distributive relationship between each of the scatters (top left and bottom right):

![fig](https://cdn.discordapp.com/attachments/1181806486398181446/1181808829403504651/image.png?ex=6582683d&is=656ff33d&hm=a7b7c3e63b140d52236059d97331d229562b1c461e06e06c2ba4920a5e701155&)

Initial attempts of our model tried to predict game winners, but we had low quality data, it wasn’t scalable, and was more of a classification. It was also hard to extrapolate it to use with betting terminologies. While there is technically an approach that could work with classification, the approach logically is a little more convoluted. The naive approach to using classification algorithms on betting data would be to classify the games based on which team won. The flaw to this approach is that oftentimes the difficulty is not determining which team won, but by how much and how likely, both important factors in betting statistics. The more probable approach for classification would be to classify the bids themselves, but a drawback would be the increased difficulty in visualizing and understanding the data. With a regression approach, we could predict specifically the score outcome and effectively tell us more than just which team they expect to win but also by how much which integrates well with the betting system.

Our dive into utilizing support vector machine regression was the solution to the problem. The more sophisticated model in combination with our newly processed data held many more advantages than our primitive linear regression models. Score differentials are scalable and translate directly to betting data in their spread. While initially the SVR had a high error, through reducing the dimensionality through normalization and  principal component analysis, it improved the model and lowered our error. Running SVR on the data to predict the score differential yielded an average RMSE of 13. This was not great, but it was a workable amount as by choosing a good buffer value, we could only bet on those that we think have a high enough chance of converging despite the error.

![fig](https://media.discordapp.net/attachments/1181806486398181446/1181841559315030046/image.png?ex=658286b9&is=657011b9&hm=6710d184c054ec074b4833f64c19789681fcfad578996300bb6e074473511b4f&=&format=webp&quality=lossless&width=1454&height=1402)

Next, we did training and testing on around 80% of the database with 60% dedicated to training and 20% to testing, and then ran a gambling simulation on the remaining 20%. We then used the  projected score differential from the SVR model to apply to  the betting strategy. We can then simulate primitive betting by betting a constant value of 100 every time we decide to take a bet. The basic idea behind this was to consider a select amount of past games and take the bet whenever the results were favorable according to our model, or where there is a significant enough discrepancy in the betting spread and our project score differentials. Taking into consideration the profit of all the bets that would have won and the losses of all the bets that we would have lost, this averaged around $20 of profit per game following this strategy in our testing, succeeding in our initial goal to develop a model to aid us in determining when to take the bet. All visualizations of the various features of this SVR model are located in the data visualizations section of this report.

Overall, the world of sports betting is not an easy thing to predict, but that’s why it’s a valuable market for ML. With the combination of our rolling team statistics as well as the more sophisticated algorithm we were able to improve our model greatly to better reflect the data with the features. If we were to proceed with this model in the future, we would like to incorporate player statistics instead of aggregating all of the data into the team statistics in order to get a better overview of the value of player composition to a team. We could also vary betting amounts depending on the score differential, since larger differences in the betting line means larger bets. Nothing is ever truly “finished” in a model such as this one, but knowing how to manipulate machine learning to tap into this market proved to be a rewarding and interesting enterprise.


![fig](https://media.discordapp.net/attachments/1181806486398181446/1181822295833071716/image.png?ex=658274c8&is=656fffc8&hm=9cdbc2ad2cfeb1c05ada2dc8c664b58c6015221faf6b108d6c7aef567e26c851&=&format=webp&quality=lossless&width=2592&height=478)

If we were to proceed with this model in the future, we would like to incorporate player statistics instead of aggregating all of the data into the team statistics in order to get a better overview of the value of player composition to a team. We could also vary betting amounts depending on the score differential, since larger differences in the betting line means larger bets.


<a id="mct"> </a>
## Midterm Contribution Table

|   Teammember   | Contribution |
| ----------- | ----------- |
| Isaac | Wrote panda scripts to preprocess data into csv files |
| | Extrapolated new features like rolling win percentages and score differentials from raw data    |
| | Created regression models to validate data |
| | Worked on linear and log regression code by testing different features |
|  |  |
|Avery| Created initial sample visualizations|
||Worked on regression code by testing different features|
||Updated the project writing to reflect midpoint progress of the project|
|  |  |
|Adolfo| Worked on visualizations to provide insight into best features for the model.|
||Applied a weighted score and thresholding to determine meaningful trends from a combination of datasets.|
|  |  |
|Daniel|Preprocessed data|
||Worked on creating visualizations and metrics based on the model performance (included max error, coefficient of determination, mean-squared error)|
||Feature selection|
| |  |
|Alex|Preprocessed data|
||Worked on creating visualizations and metrics based on the model performance|
||Created linear regression models for score differential|
||Feature selection|




<a id="bib"> </a>
## Bibliography/Sources

Walsh, C., & Joshi, A. (2023, June 29). Machine learning for sports betting: Should predictive models be optimised for accuracy or calibration?. arXiv.org. https://arxiv.org/abs/2303.06021 \
\
Bucquet, A., &amp; Sarukkai, V. (2018). The bank is open: Ai in sports gambling. https://cs229.stanford.edu/proj2018/report/3.pdf \
\
Hubáček, O., Železný, F., & Šourek, G. (2019, February 19). Exploiting sports-betting market using machine learning. International Journal of Forecasting. https://www.sciencedirect.com/science/article/pii/S016920701930007X 

<a id="contrib"> </a>
### Contributions
The article created and tested three different models to predict betting lines of NBA games. It also provided us with the accuracy for each of the models they created which we then used to decide which model we wanted to go ahead and implement for our own project. As you can see from the table below, all of the models they tested had comparable accuracies with not a single one being clearly the best. Since all of them had similar accuracies we decided to go with logistic regression since we were more familiar with the model’s implementation and requirements.

![c1](https://media.discordapp.net/attachments/1146619129793617970/1173832909099118602/image.png?ex=65656416&is=6552ef16&hm=deacb42c67eec5d4b92a803da654bdd7dfb6426141e602c36c558f78d7645ae9&=&width=2592&height=552)

The article also provided us with an example of what features we should ideally use for a primitive version of our model. We based our initial model’s features from this and then we tweaked it along the way to see which features worked the best for our own model.

![c2](https://media.discordapp.net/attachments/1146619129793617970/1173832909514342490/image.png?ex=65656416&is=6552ef16&hm=e130b48a55b491cc40fd6fd8fa9537c4cd16e271b760d53705c4eff1ba5dc1e7&=&width=2592&height=952)

Bucquet, A., &amp; Sarukkai, V. (2018). The bank is open: Ai in sports gambling. https://cs229.stanford.edu/proj2018/report/3.pdf

This article/report was particularly helpful in determining what features work best to predict betting lines and what other models (apart from linear regression) we can possibly use for our predictions. As you can see from the picture below, the article provided us with sample features along with more complicated features that can also be used to more accurately predict betting lines. Along with the proposed features they used, the article also provided other models that accurately predicted betting lines such as Random Forests and Neural Networks which we are going to implement for our final sprint/proposal.

![c3](https://media.discordapp.net/attachments/1146619129793617970/1173832909925404712/image.png?ex=65656416&is=6552ef16&hm=0d403f16220ca71a97ec15983af7a32b4876d356f6f773e463b2f66fe902b04b&=&width=2002&height=1402)

Hubáček, O., Železný, F., & Šourek, G. (2019, February 19). Exploiting sports-betting market using machine learning. International Journal of Forecasting. https://www.sciencedirect.com/science/article/pii/S016920701930007X

Contributions: This article provided more concrete information and confirmation on which data features are the best to use for the model. The features that the researchers used in their model closely matched with the features that were shown in the other articles. As you can see from the picture below which contains some of the features that they used for their model.

![c4](https://media.discordapp.net/attachments/1146619129793617970/1173832949435744347/image.png?ex=6565641f&is=6552ef1f&hm=8fd96334ddf9a4a7dfd478b66e7db10c0997f2bc63531194f447694fe4241af2&=&width=1528&height=1402)
