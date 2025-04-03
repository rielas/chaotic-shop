# Chaotic Shop

Chaotic Shop is a mock internet shop which generates pages randomly. It can be used to test web
scraping and build on FastHTML.

Generated products and categories are reproducible. Every time you run the server with the same
parameters, the same products and categories will be generated. This is useful for testing and
debugging.

# What is Chaos?

Chaos is a measure of how much randomness is introduced into the generated pages. It can be random
id for HTML elements or changing the order of elements. The higher the chaos, the more
unpredictable the generated pages will be.

# Parameters

- `CATEGORY_CHAOS`: Every product in category will get the same mutations. It helps to separate
products by categories. 0 means no mutations.
- `PRODUCT_CHAOS`: Every product will get a unique set of mutations. 0 means no mutations.
- `NUMBER_OF_PRODUCTS`: Number of products to generate. The higher the number, the more products
will be generated. The default is 1000.

So, to run shop with no difference between products, you can run:

```sh
$ CATEGORY_CHAOS=0 PRODUCT_CHAOS=0 poetry run chaotic_shop
```

If you want to test how your scrapper works with drift between products in the same category, you
can run:

```sh
$ CATEGORY_CHAOS=2 PRODUCT_CHAOS=5 poetry run chaotic_shop
```

In this case category chaos will distinguish products in categories, and product chaos will
fuzz the products in the same category.

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
