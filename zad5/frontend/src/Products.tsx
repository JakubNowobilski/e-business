import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Products.css';

interface Product {
    id: number;
    name: string;
    price: number;
    description: string;
    image_url: string;
}

const Products: React.FC = () => {
    const [products, setProducts] = useState<Product[]>([]);

    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const response = await axios.get<Product[]>('http://localhost:9000/products');
                setProducts(response.data);
            } catch (error) {
                console.error('Failed to fetch products', error);
            }
        };
        fetchProducts().then(() => {
            console.log('Products fetched');
        })
    }, []);

    return (
        <div className="products-grid">
            {products.map((product) => (
                <div key={product.name} className="product-card">
                    <h2>{product.name}</h2>
                    <img src={product.image_url} alt={product.name} />
                    <p>{product.description}</p>
                    <p>${product.price}</p>
                </div>
            ))}
        </div>
    );
};

export default Products;
