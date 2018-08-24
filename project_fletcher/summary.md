# Overview
Throughout this project, I wanted to maintain the goal of accomplishing something that would be useful to either Fenty Beauty or Sephora as a business. The brunt of what I did for this project therefore did not make it into my final presentation because it was unsuccessful in that respect.

The general process I had was more or less:
1.	Scraping
2.	Overall Reviews:
  + Topic Model
  + Classify
  + Sentiment Analysis
3.	Over Negative Reviews:
  + Topic Model
  + Classify

# Scraping
I did an involved scrape of Sephora, a company which for some reason didn’t built a site that would be friendly to data mongers. A primarily brick and mortar beauty company doesn’t care about techies trying to creep on them? Who would’ve thought.

The site was rendered using javascript and you could only click through 6 reviews at a time, which all accumulated as you added more. Eventually, the page would time out because it couldn’t handle all the reviews on the screen. Most of the class names referenced css and were something like css-123asjkdf; because they couldn’t have called a class ‘review’ apparently.

Technically the reviews were auto sorted by most helpful, which is a poor idea because then people will only be seeing the same reviews (hence my helpfulness predictor), although there is an option to organize the page by the most recent reviews. Weirdly, though it said it was sorting by the most helpful reviews it wasn’t actually organized in that order.

I tried a 9 hour, a 6 hour, and a full day scrape, reminding myself that this is not a primarily tech company throughout. The most I got was 2,657 reviews. Some people had posted reviews multiple times, and some hadn’t written anything, so I dropped those. Thankfully there were only a few of these.

# Topic Modelling on Overall and Negative Reviews
I used count vectorizer for all my topic modelling because_____

I tried all three topic modelling methods we talked about in class, LSA, LDA, and NMF.

This was iterative, so I went back and played with parameters as needed. For example, I removed stop words as I saw them, changed the max_df a few times, etc…

In the end, I had similar results for both overall and negative reviews, finding the most coherent topics with LDA using Truncated SVD and a max_df of 0.6. This was what I used as needed for the remainder of the project,

# Classification on overall reviews
I built a pseudo-package with this, which was essentially a pipeline for trying different classification methods and easily fiddling with the parameters.

Within the pipeline there was a class, which had functions for each of four models: KMeans, DBSCAN, Spectral Shift, and Meanshift. There was also a function to print out a TSNE and the number of items in a given cluster.

Outside of the class, I had two functions to print out the 4 closest reviews to the centroids for meanshift and kmeans using cosine similarity as the metric.

I used the pipeline-package to decide on the “best” clustering technique.

First, I checked for dimensions by running TSNE plots. The best one for all the reviews was 50.

Then I checked the SSE/Silhouette score plots to find the best number of clusters and printed the results.

Sadly, it made no sense. :cry:

# Classification on negative reviews
I used the clustering method that was found for the overall reviews, i.e. KMeans on the topic space in order to maintain consistency. At this point I still thought both of these would make it to my final presentation.

The rest was essentially a repeat of the classification on overall reviews; i.e. changing dimensions, checking the SSE/silhouette score for the number of clusters, printing out the silhouette score per cluster, trying a few different cluster numbers, printing the four closest reviews, and skimming them for some relationship.

Again, no success here. :cry: :cry:


## Star Rating


## Helpfulness




# Final Thoughts
Looking back, there were a couple things that I would do differently. I’m definitely happy that I took on something that I wasn’t sure would have an answer (i.e. a good cluster), but I would have wanted to prepare for that earlier on.

Stepping back a bit and thinking about the role of these projects as portfolios for businesses, I wish I’d used MongoDB.
