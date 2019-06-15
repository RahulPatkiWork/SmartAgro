# SmartAgro
--------------------------------------------------------------------------------------------------
*Introduction*:

Smart Agro is a cross platform system which provides :

#**Ecommerce** (buying and selling of crops),

#**Prediction of optimal crop prices in future**,

#**Recommendation systems for farmers.**

*Languages*:
-------------------------------------------------------------------------------------------------

The project uses: python, java, css, js, html etc. Sqlite3 and Postgre have been used for database.
It is mainly developed using :
Python(ML-Google Colab),
Java(Android),
Django-oscar framework(Ecommerce Website) .
and is available as a webapp,native android app!

API's used:
Google Analytics;
Paypal Express;
Haystack and Solr search backend;

*Details*:
--------------------------------------------------------------------------------------------------------

The python modules perform the following tasks:

  -Future Crop price prediction is performed on dataset provided by government website (data.gov.in) by applying SVR to perform time series crop price predictions.For better accuracy Elastic Net has been applied on updated dataset

  -The website provides a broker-free ecommerce platform to the farmers. It allows citizens, farmers to sell/buy crops needed on a daily basis directly from farmers (partners).

  -Apriori algorithm is used to perform Market Basket Analysis and provides cross selling recommendations to sellers  based on customer buying pattern of the crops on the ecommerce website to further increase profitability.

  -Data from government repositories is used to determine most suitable crops in a particular area for a particular season by applying Regression, these crops are recommended to the seller.

The java part is used to make the android app which performs following tasks:

  -The android app integrates the ML models and ecommerce site and provides additional information.

  -The app provides some motivational videos as well as success stories and ideas used by peer farmers to increase profitability.

  -The application provides farmers with links to various central and state government schemes and websites.The app acts as a complete guide containing different varieties of crops, suitable weather and soil conditions for the crops, production methods, fertilizers, possible diseases along with treatment and yield information thereby meeting most of the farmer’s requirements.

  
Read More :-
------------------------------------------------------------------------------------------------------------------------------------
Paper1:
  [Survey-Paper](http://ijsrd.com/Article.php?manuscript=IJSRDV6I100248)
  
Paper2:
  To be updated!
  
WebSite:
  [SmartAgro-Ecommerce](https://smartagroecom.pythonanywhere.com/)
  
Android:
  [SmartAgro-PlayStore](https://play.google.com/store/apps/details?id=com.sneha.smartagro)

Scope of Repository:
----------------------------------------------------------------------------------------------------------------------------------------
The repo has code for ecommerce platform, recommendation system for : cross selling, MRP,seasonal weather,soil based crop recommendations, price prediction.Datasets are used from available government sites.


Demos:
------------------------------------------------------------------------------------------------------------------------

-[SmartAgro-Brief-Demo](https://drive.google.com/file/d/1-QM0HnnmrqbW1UooB4SsNs92EvI4LuGv/view?usp=sharing)

Detailed Demo:

  -[SmartAgro-Ecommerce_Buyer](https://drive.google.com/file/d/1f9vDAmvBEvEVlo6LQEpLa5VmEDFmyFux/view?usp=sharing)


  -[SmartAgro-Ecommerce_Seller&Admin](https://drive.google.com/file/d/1-3RnuCrpiyhKKd3S4R2w7TEPZTsoCwZz/view?usp=sharing)


  -[SmartAgro-Recommendation Systems](https://drive.google.com/file/d/1-5zUOuAL0g3oixkQ5lSGBTxP6abzPrkU/view?usp=sharing)


  -[SmartAgro-Prediction Systems](https://drive.google.com/file/d/1-9s8Cap6RrKnc4h6Xu7PfANhOx7eDb0I/view?usp=sharing)


*App Link:*
[SmartAgro-PlayStore](https://play.google.com/store/apps/details?id=com.sneha.smartagro)



  
Creator/Maintainer:
------------------------------------------------------------------------------------------------------
Rahul.R.Patki
