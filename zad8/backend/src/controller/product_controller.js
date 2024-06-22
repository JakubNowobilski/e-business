const utils = require("../utils");

function productController(app, product_repository) {
    app.get("/products", ((req, res) => {
        utils.printReqSummary(req)
        return res.status(200).send(product_repository.getAllProducts())
    }))

    app.get("/products/:id", ((req, res) => {
        utils.printReqSummary(req)
        const product = product_repository.getProductById(parseInt(req.params.id));
        if (product === undefined) {
            return res.status(404).send({error: 'Data not found'})
        } else {
            return res.status(200).send(product)
        }
    }))

    app.post("/products", ((req, res) => {
        utils.printReqSummary(req)
        const product = req.body
        if (utils.validateProduct(product)) {
            product_repository.addProduct(product)
            return res.status(200).send(product)
        } else {
            return res.status(404).send({error: 'Invalid product data'})
        }
    }))

    app.put("/products/:id", ((req, res) => {
        utils.printReqSummary(req)
        const product = req.body
        if (utils.validateProduct(product)) {
            product_repository.updateProduct(product)
            return res.status(200).send(product)
        } else {
            return res.status(404).send({error: 'Invalid product data'})
        }
    }))

    app.delete("/products/:id", ((req, res) => {
        utils.printReqSummary(req)
        product_repository.deleteProduct(parseInt(req.params.id))
        return res.status(200).send({message: 'Product deleted'})
    }));

}

module.exports = {
    productController: productController
}
