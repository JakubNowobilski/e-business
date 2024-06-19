package repositories

import model.Product

object ProductRepository {
  private var products: Map[Long, Product] = Map()

  def fetchAll: Seq[Product] = products.values.toSeq

  def fetchById(id: Long): Option[Product] = products.get(id)

  def addProduct(product: Product): Product = {
    products = products + (product.id -> product)
    product
  }

  def updateProduct(product: Product): Product = {
    val updatedProduct = addProduct(product.copy(id = product.id))
    updatedProduct
  }

  def deleteProduct(id: Long): Option[Product] = {
    val found = products.get(id)
    products = products - id
    found
  }
}