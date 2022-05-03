# Weaviate Neural Wine Search

Data: [Kaggle (from WineEnthusiast)](https://www.kaggle.com/zynicide/wine-reviews).
Model: [multi-qa-MiniLM-L6-cos-v1](https://huggingface.co/sentence-transformers/multi-qa-MiniLM-L6-cos-v1)


## Usage

1. Start up Weaviate: `docker-compose up -d`. Once completed, Weaviate is running on [`http://localhost:8080`]().
3. Run `python import_data.py` to import the wine data to Weaviate.
4. Navigate to [console.semi.technology](https://console.semi.technology/), connect to `http://localhost:8080`, navigate to the query module.
5. Run query's like:
```graphql
{
  Get {
    Wine(limit: 3, nearText: {concepts: ["wine that goes with cheese"]}) {
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
          "description": "This delicate, elegant NLH wine starts with alluring aromas of lush honey, apricot and citrus and offers a vibrant, lively balance of fruit and acid. Pair with cheeses and fruit salads.",
          "title": "Mulderbosch 2006 Noble Late Harvest Sauvignon Blanc (Stellenbosch)."
        },
        {
          "description": "This easygoing white starts with a fresh nose of grapefruit, fig and flowers and leads into zesty but complex flavors of tropical fruit and citrus. Approachable and balanced, the wine will pair well with seafood and chicken dishes.",
          "title": "Rietvallei Estate Wine 2008 Sauvignon Blanc (Robertson)."
        },
        {
          "description": "There's a hint of sweetness here, and light, almost watery fruit flavors of watermelon and strawberry. This could accompany a starter course of mild cheeses.",
          "title": "Sno Road 2014 Rosado of Tempranillo (Columbia Valley (OR))."
        }
      ]
    }
  }
}
```
