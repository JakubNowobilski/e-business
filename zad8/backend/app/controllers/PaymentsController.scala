package controllers

import model.ProductPayment
import play.Logger
import play.api.libs.json.{JsValue, Json, OFormat}
import play.api.mvc._
import repositories.ProductRepository

import javax.inject._

@Singleton
class PaymentsController @Inject()(val controllerComponents: ControllerComponents) extends BaseController {

  implicit val productPaymentFormat: OFormat[ProductPayment] = Json.format[ProductPayment]

  def processPayment: Action[JsValue] = Action(parse.json) { request =>
    request.body.validate[List[ProductPayment]].fold(
      problems => {
        Logger.error("Error: Invalid JSON")
        BadRequest("Invalid JSON")
      },
      payments => {
        val allProductsExist = payments.forall(payment => ProductRepository.fetchById(payment.id).isDefined)
        if (allProductsExist) {
          Logger.info(s"Bought ${payments.size} products")
          Ok("OK")
        } else {
          Logger.error("Error: one or more products do not exist")
          BadRequest("One or more products do not exist")
        }
      }
    )
  }

}