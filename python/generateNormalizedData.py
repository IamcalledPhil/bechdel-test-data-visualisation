import json
import io

with open('moviesBechdel.json') as f:
    moviesBechdel = json.load(f)

with open('moviesBudget.json') as f:
    moviesBudget = json.load(f)

normalizedMovies = []

for movie in moviesBudget:
    for bechMovie in moviesBechdel:

        if movie["imdb_id"] == 'tt' + bechMovie["imdbid"]:
            normalizedMovie = bechMovie
            normalizedMovie["budget"] = movie["budget"]
            normalizedMovies.append(normalizedMovie)

with io.open('normalizedMovies.json', 'w', encoding='utf8') as outfile:
    data = json.dumps(normalizedMovies, outfile, ensure_ascii=False, indent=4)
    outfile.write(unicode(data))