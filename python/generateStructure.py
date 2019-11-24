import json
import io
from operator import itemgetter
from collections import Counter


with open('normalizedMovies.json') as f:
    normalizedData = json.load(f)

finalMovies = [] 


for year in range(28):
    yearData = {
        "year": str(year + 1990),
        "movies": []
    }
    finalMovies.append(yearData)

for movie in normalizedData:
    for yearData in finalMovies:
        if yearData["year"] == str(movie["year"]):
            yearData["movies"].append(movie)

# check if is in 50 highest budgets
for finalMovieYear in finalMovies:
    finalMovieYear["movies"] = sorted(finalMovieYear["movies"], key=itemgetter('budget'), reverse=True)
    finalMovieYear["movies"] = finalMovieYear["movies"][:20]

    totalBudget = 0
    for m in finalMovieYear["movies"]:
        totalBudget += m["budget"]
    finalMovieYear["averageBudget"] = totalBudget/ len(finalMovieYear["movies"])

# sort movies by rating
for finalMovieYear in finalMovies:
    finalMovieYear["movies"] = sorted(finalMovieYear["movies"], key=itemgetter('rating')) 
print(finalMovies)


with io.open('finalData.json', 'w', encoding='utf8') as outfile:
    data = json.dumps(finalMovies, outfile, ensure_ascii=False, indent=4)
    outfile.write(unicode(data))