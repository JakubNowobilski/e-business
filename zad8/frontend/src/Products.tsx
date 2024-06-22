import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Products.css';
import Payments from './Payments';

interface Product {
    id: number;
    name: string;
    price: number;
    description: string;
    image_url: string;
    count: number;
}

const Products: React.FC = () => {
    const [products, setProducts] = useState<Product[]>([]);

    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const response = await axios.get<Product[]>('http://localhost:8080/products');
                const productsWithCount = response.data.map(product => ({ ...product, count: 0 })); // Initialize count to 0
                setProducts(productsWithCount);
            } catch (error) {
                console.error('Failed to fetch products', error);
            }
        };
        fetchProducts();
    }, []);

    const incrementCount = (id: number) => {
        setProducts(products.map(product => product.id === id && product.count < 99 ? { ...product, count: product.count + 1 } : product));
    };

    const decrementCount = (id: number) => {
        setProducts(products.map(product => product.id === id && product.count > 0 ? { ...product, count: product.count - 1 } : product));
    };

    const resetCount = () => {
        setProducts(products.map(product => ({ ...product, count: 0 })));
    };

    const totalPrice = products.reduce((total, product) => total + product.price * product.count, 0);

    return (
        <div>
            <div className="products-grid">
                {products.map((product) => (
                    <div key={product.name} className="product-card">
                        <h2>{product.name}</h2>
                        <img src={product.image_url} alt={product.name} />
                        <p>{product.description}</p>
                        <p>${product.price}</p>
                        <div className="counter-container">
                            <button className={`decrement-button ${product.count === 0 ? 'disabled' : ''}`} onClick={() => decrementCount(product.id)}>-</button>
                            <span>{product.count}</span>
                            <button className={`increment-button ${product.count === 99 ? 'disabled' : ''}`} onClick={() => incrementCount(product.id)}>+</button>
                        </div>
                    </div>
                ))}
            </div>
            <div className="summary">
                <h2>Total Price: ${totalPrice.toFixed(2)}</h2>
            </div>
            <button className="reset-button" onClick={resetCount}>Reset Count</button>
            <Payments products={products.filter(product => product.count > 0)}/>
        </div>
    );
};

export default Products;
