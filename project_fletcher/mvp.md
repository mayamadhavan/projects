# Domain
I will be working with makeup data. I'm taking reviews on Feny Beauty Pro Filt'r Matte Foundation on Sephora. I've got a pretty good awareness of the domain, given that I'm pathologically obsessed with skincare/makeup.

# Data
There are currently 10,443 reviews on the website, all of which have some amount of text content.

The columns look like this:

| User | Rating | Helpful | Review | Skin Color | Skin Concern |

You can find the jupyter notebook where I am scraping from in the main page of this repository. In progress as of Aug 14, 5:00pm.

# Known Unknowns
I think my biggest concern with this project will be making sure I understand what I can and can't do with the data using NLP.

Currently finding the scraping to be more complicated than expected (reviews are in javascript and you can only load 6 more reviews at a time).

# Current Plan
I can do sentiment analysis on the reviews to predict the output and also look at how helpful each review has been tagged as. I'd want to segment the complaints by skin color and type then see which concerns pop up more frequently (Categorizing feedback) and can maybe throw in some recommendations (eg if this concern pops up, try this product/hack).

It has a clear business use case, and I'm really interested in the topic so I would like to move forward with it.