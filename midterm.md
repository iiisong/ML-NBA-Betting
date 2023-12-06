# ML4641_NBA_Betting
Predicting NBA Bet outcomes using ML for ML4641

[old intro](intro.md)

## Table of Contents
1. [Introduction](#intro)
2. [Motivation](#motivation)
3. [Methods Introduction](#intro_methods)
4. [Data Visualization](#datavis)
2. [Motivation](#methods)
3. [Results and Discussion](#results)
4. [Testing](#testing)
4. [Midterm Contribution Table](#mct)
4. [Bibliography and Sources](#bib)

<a id="intro"> </a>
## Introduction
The NBA Betting Line provides the league with an insanely popular avenue for sports wagering. The moneyline is a two-way market that is focused on a single game between the two teams: using American odds, the favorite receives a negative value while the underdog gets a positive value. With this billion-dollar industry in mind, our team realizes the significant part that accurate intelligent tools can play in the betting market, and want to try our hand at developing a prediction model for this purpose. Machine learning models would not only be highly relevant, they would also be well fed from the glut of data from this highly visible and documented industry.


<a id="motivation"> </a>
## Motivation
The motivation behind the project is to develop an intelligent tool to use in the betting market. To do this, the model would have to consider many different factors of the teams and games of previous seasons to better understand the inner logistics of the market and produce the winning team. In the NBA Betting Line, the negative value associated with the favored team is how much money the better has to put in in order to receive a net profit of $100. On the other hand, the positive value of the underdog team is how much the better could earn if they bet $100. This creates a market where the favored team has more of a probability of winning, but the underdog has the possibility of a larger payout. Although the “favored” team has the better odds, nothing is set in stone. A number of different reasons could cause the underdog to rise in the game. That is the fun in the world of sports betting. Therefore, we want to carefully examine the most important insights and features of both of the teams with regards to data pertaining to injury reports, past game results, player statistics, and other team metrics to make our model answer the big question: *should we take the bet?*


<a id="intro_methods"> </a>
## Methods Introduction
We will use the ["gambling_stuff"](https://github.com/jimtheflash/gambling_stuff) dataset on Github from the user jimtheflash which was found as the original source of the “NBA Betting Lines” dataset found on [Kaggle](https://www.kaggle.com/datasets/thedevastator/uncovering-hidden-trends-in-nba-betting-lines-20). It includes 341 files of sequential data including won/lost games, complete statistics for all players in the NBA in the 2021-2022 season, some player data from 2012, tip-off stats, as well as points scored per game. We will use each team’s features to analyze which team should be favored when it comes to making a bet on a particular sporting event or match-up.

During data processing, the main issue was with the very large and widely scoped datasets in the “gambling_stuff” Github site. We used the Python Data Analysis Library (pandas) to retrieve the most relevant information to start off with our basic models. We made our own csv files with pertinent information that could help with prediction model accuracy. First, we unified basic game information into a single file for easy access. Then, we added features that included final scores with both team IDs and the winner, game IDs, away team win probability, away team spreads, away team totals, and 10/25/50/75 game rolling win percentages. These features may be modified or extended upon as we proceed with the project as our scope changes or expands.


<a id="datavis"> </a>
## Data Visualization

Using the available data for the team statistics, we created multiple tools for visualization and assessing patterns in the data. One of these methods consisted of preprocessing the points scored by the teams each year and labeling each team ID as a different cluster. Consequently, we were able to create a mapping of each year to a set of corresponding games and their final scores per team. This result is plotted in the following figure:

![y/ppg](https://media.discordapp.net/attachments/1146619129793617970/1173828006058393640/image.png?ex=65655f85&is=6552ea85&hm=ed3df97e1f4055e94afca7ffcce1a3f706cd386075d54e7e09db9b60a9043522&=&width=1776&height=1356)

To find relevant patterns and features, it is important to consider games that more directly impact betting/money lines. As a result, it is important to combine game data with betting line data from the additional datasets in our project. We computed a weighted score for each team (per year), and removed data points that resulted in smaller values. This way, we can now visualize more meaningful scores and identify trends:

![fig2](https://media.discordapp.net/attachments/1146619129793617970/1173828006389760150/image.png?ex=65655f85&is=6552ea85&hm=899a7024db7aed9f5d246f6c5f7a41e6f8e4841633755833562deb985c367bfd&=&width=2592&height=892)

In these plots, we visualize the weighted score per team (y-axis) per year (x-axis). It now becomes much easier to understand how the data has evolved over time, as well as what we can (and should) expect from fitting a model for prediction across different time periods.


<a id="methods"> </a>
## Methods

With many features to consider, we decided to use basic linear regression as a first model with our processed data. For an initial validation, we ran linear regression using both team IDs, away team win probability, away spread, and away total to predict the score differential of the actual game outcome. With five features, we had a MSE of 156 and a coefficient of determination of 0.21. We felt that it was a good start, but it is only a start.

We needed more relevant features to use if we really wanted to get anywhere. We also had the goal of removing betting line information itself from the input dataset. This is where the data preprocessing was important, and we were able to retrieve many relevant features from the original raw data as well as extrapolate some of our own, such as the rolling win percentages of the games. We also have an idea to include the win/lose ratios of the teams. The problem now lies finding exactly which of these features best fit with our model.

<a id="results"> </a>
## Results and Discussion

A key metric we are using to analyze our model’s performance is The coefficient of determination ($R^2$). It measures the percentage of the variation that the model explains. Essentially, the higher the $R^2$ value, the better the regression fits the observed data. In the middle of development, we saw that we were getting extremely low (<.15) $R^2$ values that would sometimes even be negative, which was counter-intuitive and pointed to the fact that there was most likely a bug within the processed data. We realized that there was a problem with the way we were processing the dataset: games would be listed twice because there would be one home listing and one away listing. We solved the issue by overwriting the away listing with the corresponding home listing, when we ran into it.
Another metric that we also used to evaluate the performance of the model was the Max Error which measures the maximum residual error between the predicted and actual values in a dataset. The usage of the max error as evaluation of the model gave us insight on where the model produced the largest deviation for a particular sample (in the data set). In other words, it allowed us to see what outliers in the data set caused the model to perform significantly worse than how it otherwise would have.

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