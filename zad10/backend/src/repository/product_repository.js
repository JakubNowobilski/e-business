class ProductRepository {

    constructor() {
        this.products = new Map();
    }

    getProductById(id) {
        return this.products.get(id);
    }

    getAllProducts() {
        return Array.from(this.products.values());
    }

    addProduct(product) {
        this.products.set(product.id, product);
    }

    updateProduct(product) {
        this.products.set(product.id, product);
    }

    deleteProduct(id) {
        this.products.delete(id);
    }

}

module.exports = {
    ProductRepository: ProductRepository
}
