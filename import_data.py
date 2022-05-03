import pandas as pd
import weaviate

client = weaviate.Client("http://localhost:8080")

class_obj = {
    "class": "Wine",
    "properties": [
        {
            "name": "title",
            "dataType": ["text"]
        },
        {
            "name": "description",
            "dataType": ["text"]
        }
    ]
}

new_class = client.schema.create_class(class_obj)

# open wine dataset (10000 items)
df = pd.read_csv('data/wine_reviews.csv', index_col=0)

def add_wines(data, batch_size=99):
    no_items_in_batch = 0

    for index, row in data.iterrows():
        wine_object = {
            "title": row["title"] + '.',
            "description": row["description"],
        }

        client.batch.add_data_object(wine_object, "Wine")

        no_items_in_batch += 1

        if no_items_in_batch >= batch_size:
            results = client.batch.create_objects()
            no_items_in_batch = 0

    client.batch.create_objects()

add_wines(df)
