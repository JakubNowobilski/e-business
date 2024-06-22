import React, { useState } from 'react';
import './Login.css';

const Login: React.FC = () => {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <div className="login-container">
            <button className="login-button" onClick={() => setIsOpen(!isOpen)}>Login</button>
            {isOpen && (
                <form className="login-form">
                    <input type="text" placeholder="Login" />
                    <input type="password" placeholder="Password" />
                    <button type="submit">Submit</button>
                </form>
            )}
        </div>
    );
};

export default Login;
