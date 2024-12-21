import collection

if __name__ == '__main__':
  rest_collection = collection.Collection()
  rest_collection.generate_collection("REST", "Kucoin REST API")

  res_collection = collection.Collection()
  res_collection.generate_collection("Abandoned Endpoints", "Kucoin REST API(Abandoned)")
