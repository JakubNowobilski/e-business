const fs = require("fs");

function readDemoProductsFromFile() {
    const demo_products = fs.readFileSync('resources/demo_products.json', 'utf8')
    return JSON.parse(demo_products)
}

function loadDemoData(product_repository) {
    const products = readDemoProductsFromFile()
    products.forEach(p => product_repository.addProduct(p))
}

function validateProduct(product) {
    const requiredAttributes = ["id", "name", "price", "description", "img_url"]
    const productAttributes = Object.keys(product)
    if (productAttributes.every(e => requiredAttributes.includes(e)) &&
        requiredAttributes.every(e => productAttributes.includes(e))) {
        return true;
    } else {
        return false;
    }
}

function validatePayment(payment) {
    const requiredAttributes = ["id", "count"]
    const paymentAttributes = Object.keys(payment)
    if (paymentAttributes.every(e => requiredAttributes.includes(e)) &&
        requiredAttributes.every(e => paymentAttributes.includes(e))) {
        return true;
    } else {
        return false;
    }
}

function printReqSummary(req) {
    console.log("Handling " + req.method + " " + decodeURI(req.originalUrl));
}

module.exports = {
    readDemoProductsFromFile: readDemoProductsFromFile,
    loadDemoData: loadDemoData,
    validateProduct: validateProduct,
    validatePayment: validatePayment,
    printReqSummary: printReqSummary
}
