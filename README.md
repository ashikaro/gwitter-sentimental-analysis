# gwitter-sentimental-analysis

# Objective

* To visually represent the sentiment of the tweets associated with a phrase by geographical regions using Raspberry Pi.

# Working of project
* Implemented in Python using Raspberry Pi, Breadboard and LEDs.
* Takes a query or phrase from the user using GUI.
* Queries Twitter APIs based on a geo-code and radius for the regions using Tweepy.
* Calculates the sentiment of the tweets for the regions using Textblob.
* Lights up the (RGY) color leds for the cities appropriately depending on the sentiment.
* Displays a bar graph for the distribution of sentiments in the Desktop App
