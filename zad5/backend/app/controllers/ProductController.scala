package controllers

import model.Product
import play.api.libs.json._
import play.api.mvc._
import repositories.ProductRepository
import utils.FileHelper

import javax.inject._

@Singleton
class ProductController @Inject()(val controllerComponents: ControllerComponents) extends BaseController {

  implicit val productFormat: OFormat[Product] = Json.format[Product]

  FileHelper.loadDemoData()

  def getAllProducts: Action[AnyContent] = Action {
    val products = ProductRepository.fetchAll
    Ok(Json.toJson(products))
  }

  def getProduct(id: Long): Action[AnyContent] = Action {
    ProductRepository.fetchById(id) match {
      case Some(product) => Ok(Json.toJson(product))
      case None => NotFound
    }
  }

  def createProduct: Action[JsValue] = Action(parse.json) { request =>
    request.body.validate[Product].fold(
      problems => BadRequest("Invalid JSON"),
      input => {
        val product = ProductRepository.addProduct(input)
        Created(Json.toJson(product))
      }
    )
  }

  def updateProduct(id: Long): Action[JsValue] = Action(parse.json) { request =>
    request.body.validate[Product].fold(
      problems => BadRequest("Invalid JSON"),
      input => {
        ProductRepository.fetchById(id) match {
          case Some(_) =>
            val updatedProduct = ProductRepository.updateProduct(input)
            Ok(Json.toJson(updatedProduct))
          case None => NotFound
        }
      }
    )
  }

  def deleteProduct(id: Long): Action[AnyContent] = Action {
    ProductRepository.deleteProduct(id) match {
      case Some(product) => Ok(Json.toJson(product))
      case None => NotFound
    }
  }

}
