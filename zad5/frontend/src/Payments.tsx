import React from 'react';
import axios from 'axios';

interface Product {
    id: number;
    count: number;
}

interface PaymentsProps {
    products: Product[];
}

const Payments: React.FC<PaymentsProps> = ({ products }) => {
    const handleBuy = async () => {
        try {
            const payment = products.map(product => ({ id: product.id, count: product.count }));
            const response = await axios.post('http://localhost:9000/payments', payment);
            console.log(response.statusText);
            if (response.status === 200) {
                window.alert('Payment successful!');
            }
        } catch (error) {
            console.error('Failed to send payment', error);
        }
    };

    return (
        <button onClick={handleBuy}>Buy</button>
    );
};

export default Payments;
