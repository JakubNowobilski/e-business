const db = require("./db/db_service")
const utils = require("./utils");
const productController = require("./controller/product_controller");
const paymentController = require("./controller/payment_controller");
const userController = require("./controller/user_controller");
const express = require("express");
const cors = require("cors");
const { ProductRepository } = require("./repository/product_repository");
const port = 8080;
const app = express();

app.use(cors())
app.use(express.json());
app.use(express.urlencoded({extended: true}))

product_repository = new ProductRepository()
utils.loadDemoData(product_repository)

productController.productController(app, product_repository)
paymentController.paymentController(app, product_repository)
userController.userController(app)

app.get("/*", ((req, res) => {
    utils.printReqSummary(req)
    res.status(200).send({hello_world: "OK"});
}))

app.listen(port, () => {
    db.connectDb().then(() => {
        console.log("App server listening at http://localhost:" + port);
    })
})

