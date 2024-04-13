package utils

import model.Product
import play.api.libs.json.{JsValue, Json, OFormat}
import repositories.ProductRepository

import scala.io.Source

object FileHelper {

  implicit val productsFormat: OFormat[Product] = Json.format[Product]

  def loadDemoData(): Unit = {
    val source = Source.fromResource("resources/demo_products.json")
    val json = source.getLines.mkString
    source.close()
    val data: JsValue = Json.parse(json)
    data.validate[Seq[Product]].foreach {
      _.foreach(ProductRepository.addProduct)
    }
  }

}
