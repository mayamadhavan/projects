# MVP Summary
Predicting whether or not someone would be approved for a visa in the US. Granted more time, I will also look at how long it takes to get the visa.

Expectation: Said person knows where they are from, their education level, why they are leaving their country, and why they are going to the US. Essentially, they are not a child travelling alone. Unrealistic, but alas.

## Domain
I am working with US visa data. Since I'm a natural born citizen, I don't have any direct experience within this domain; however as the child of immigrants I have seen the process in action up close. 

## Data
I am working with the following Kaggle Data Set as my base data set: https://www.kaggle.com/jboysen/us-perm-visas
On its own, it has 154 columns and many rows (69.79 MB).

I'm personally most interested in:
 1. Decision Date
 2. Education
 3. Birth Country
 4. Country of Origin
 5. Employer 
 6. Destination
 7. Wage
 8. Type of Visa
 9. Original File Date
 10. Case Status
 
I want to add more features about the country of origin, which I could scrape from the UN (https://www.unicef.org/statistics/index_countrystats.html) or csv download from The World Bank (https://data.worldbank.org/country)

Example of target features:
1. Population
2. Diversity
3. Corruption
4. Violence
5. Conservativness (Gender Inequality, etc....)
6. Distance from the US
7. GNI Per Capita

I am currently searching for the most efficient way to get this data.

## Known unknowns
If I cleared every Nan from my dataset, even restricting to the features I described above, I would have no rows. I will need to figure out how I want to work around the Na's. As described above, I will also have to do some grunt work to get all the features I want.
