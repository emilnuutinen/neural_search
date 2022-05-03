# Weaviate Neural Wine Search (multilingual)

Data: [Kaggle](https://www.kaggle.com/zynicide/wine-reviews)

Model: [paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2)

(Better model for English only [multi-qa-MiniLM-L6-cos-v1](https://huggingface.co/sentence-transformers/multi-qa-MiniLM-L6-cos-v1)
)

## Usage

1. Start up Weaviate: `docker-compose up -d`. Once completed, Weaviate is running on [`http://localhost:8080`]().
3. Run `python import_data.py` to import the wine data to Weaviate.
4. Navigate to [console.semi.technology](https://console.semi.technology/), connect to `http://localhost:8080`, navigate to the query module.
5. Run query's like:
```graphql
{
  Get {
    Wine(limit: 3, nearText: {concepts: ["Sopii juuston kanssa"]}) {
      title
      description
    }
  }
}
```

Result is:

```graphql
{
  "data": {
    "Get": {
      "Wine": [
        {
          "description": "Oxidative in style, this Vidal Blanc boasts aromas of cidery apple, toasted nut and brioche dough. Medium to full in body, this offers concentrated flavors and tart acids. Try pairing it with a wedge of goat cheese to tame its raciness.",
          "title": "Molliver Vineyards NV Vidal Blanc (Virginia)."
        },
        {
          "description": "This is an unfettered but very enjoyable Amarone, with upfront aromas of black fruit. The palate shows ripe but not exuberant plum and prune flavors, with a hint of chocolate. Pair with seasoned cheeses or braised meat dishes.",
          "title": "Antica Corte 2010  Amarone della Valpolicella."
        },
        {
          "description": "Honeylike aromas, ripe peach and apple flavors and rather full body give this wine good depth and breadth. It seems like just the thing for a picnic or to serve with cheese at a party.",
          "title": "Balo 2014 Pinot Gris (Anderson Valley)."
        }
      ]
    }
  }
}
```
