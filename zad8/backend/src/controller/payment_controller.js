const utils = require("../utils");

function paymentController(app, product_repository) {
    app.post("/payments", ((req, res) => {
        utils.printReqSummary(req)
        const payments = req.body
        if (payments.every(p => utils.validatePayment(p) && product_repository.getProductById(p.id) !== undefined)) {
            return res.status(200).send({message: 'Payment successful'})
        } else {
            return res.status(404).send({error: 'Data not found'})
        }
    }))

}

module.exports = {
    paymentController: paymentController
}
