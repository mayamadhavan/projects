# Project Proposals

#### Thought Process- Ignore
So I've had quite a few project ideas, but I've been throwing them away for various reasons
1. Predicting Scholarshps- There is the education.gov college scorecard, which is absolutely massive and has multile years. I could do a related project using this. See below.
2. Predicting Spread of Cholera- Not enough data, and this is a water born disease, not a seasonal one.
3. Predicting Impact of Well Placement in Certain Areas- Not enough data about impacts of current wells (train sets
4. Image Recognition of Bikes for use with cameras behind cars- Not enough video data, though there is plenty image data and I remember that image analysis wasn't recommended.
6. Improving Youtube advertising using video titles and description boxes- Not sure how sucessful this would be; I would need to pick and choose the videos I would use, and then I'd worry about how I could generalize given the inauthicity of the data.

## Final Idea- Recommending Best Fit College

### Data
I will be working with College Scorecard Data (https://collegescorecard.ed.gov/data/). This is a collection of datasets from 1996 to 2015. As of now, I don't plan to make this into a time series problem, so I will only be focusing on the most recent school year that's available in the download, which is information about the 2015-2016 school year.

The 2015 file has 7594 schools with 2060+ columns relating to their acceptance rates, sat scores, graduation rate, etc..

I am also planning to combine this data with US News ranking for 2016 where applicable.

### Domain
Since I just graduated from college and went through the 2013-2014 application process, I'm fairly familiar with this domain. I am not well versed in community college operations though.

### Game Plan
I plan to make a recommender for prospective students. These students will input desirable college traits, testing scores, desired income (still deciding what to put here), whether they need a loan and how long they would be willing to spend paying it off, and I'll return a list of the highest ranked schools that:
1. Fit their requirements, and
2. They can get into

The prospective project looks like:
1. Clean Data
2. Join New Data Tables as Needed (for cleaning and additional info)
3. Predict Likelood of Acceptance for Every School That Meets Requirements
4. Return List of Highest Ranked Schools with >25% chance acceptance
5. Make Flask App, preferably with image of top ranked school and map with top ~10 school locations
6. If time permits, go back, add data for income, predict ability to afford using that
 

### Known Unknowns
The dataset is fairly messy, and I anticipate a heavy data cleaning aspect. There is a data dictionary which maps some of the the current column names, which are largely unreadable, to a user friendly name. Unfortunately, it's not comprehensive, so there are still some columns whose meanings I can't interpret. I still have enough data even without these columns, but this is a consideration to keep in mind.
