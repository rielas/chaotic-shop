# Chaotic Shop

Chaotic Shop is a mock internet shop which generates pages randomly. It can be used to test web
scraping and build on FastHTML.

# What is Chaos?

Chaos is a measure of how much randomness is introduced into the generated pages. It can be random id for HTML elements or changing the order of elements. The higher the chaos, the more unpredictable the generated pages will be.

## How to run

```sh
$ poetry lock
$ poetry install
$ CATEGORY_CHAOS=5 PRODUCT_CHAOS=2 NUMBER_OF_PRODUCTS=1000 poetry run chaotic_shop
```

# Docker
You can also run it using Docker. The following command will build the image and run the server:

```sh
$ docker build -t chaotic-shop .
$ docker run -e CATEGORY_CHAOS=5 -e PRODUCT_CHAOS=2 -e NUMBER_OF_PRODUCTS=1000 -p 8000:5001 chaotic-shop
```

Then, you can access the server at `http://localhost:8000`.


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
