package main

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strconv"

	"github.com/labstack/echo/v4"
)

type Product struct {
	Id    int     `json:"id"`
	Name  string  `json:"name"`
	Price float64 `json:"price"`
}

var (
	products = map[int]*Product{}
)

func main() {
	loadDemoProducts()

	e := echo.New()

	e.GET("/products", getAllProducts)
	e.GET("/products/:id", getProduct)
	e.POST("/products", createProduct)
	e.PUT("/products/:id", updateProduct)
	e.DELETE("/products/:id", deleteProduct)

	e.Logger.Fatal(e.Start(":8080"))
}

func loadDemoProducts() {
	file, err := os.Open("demo_products.json")
	if err != nil {
		log.Fatalf("Failed to open products file: %v", err)
	}
	defer file.Close()

	byteValue, err := ioutil.ReadAll(file)
	if err != nil {
		log.Fatalf("Failed to read products file: %v", err)
	}

	var tempProducts []*Product
	if err := json.Unmarshal(byteValue, &tempProducts); err != nil {
		log.Fatalf("Failed to unmarshal products: %v", err)
	}

	for _, product := range tempProducts {
		products[product.Id] = product
	}
}

func getAllProducts(c echo.Context) error {
	allProducts := make([]*Product, 0, len(products))
	for _, product := range products {
		allProducts = append(allProducts, product)
	}
	return c.JSON(http.StatusOK, allProducts)
}

func getProduct(c echo.Context) error {
	id, _ := strconv.Atoi(c.Param("id"))
	product, ok := products[id]
	if !ok {
		return echo.NewHTTPError(http.StatusNotFound, "Product not found")
	}
	return c.JSON(http.StatusOK, product)
}

func createProduct(c echo.Context) error {
	p := new(Product)
	if err := c.Bind(p); err != nil {
		return err
	}
	products[p.Id] = p
	return c.JSON(http.StatusCreated, p)
}

func updateProduct(c echo.Context) error {
	id, _ := strconv.Atoi(c.Param("id"))
	product, ok := products[id]
	if !ok {
		return echo.NewHTTPError(http.StatusNotFound, "Product not found")
	}
	if err := c.Bind(product); err != nil {
		return err
	}
	products[id] = product
	return c.JSON(http.StatusOK, product)
}

func deleteProduct(c echo.Context) error {
	id, _ := strconv.Atoi(c.Param("id"))
	product, ok := products[id]
	if !ok {
		return echo.NewHTTPError(http.StatusNotFound, "Product not found")
	}
	delete(products, id)
	return c.JSON(http.StatusOK, product)
}
