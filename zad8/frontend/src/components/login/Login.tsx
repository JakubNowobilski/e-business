import React, { useState } from 'react';
import './Login.css';
import axios from 'axios';
import SHA256 from 'crypto-js/sha256';

interface LoginProps {
  isLoggedIn: boolean;
  setIsLoggedIn: React.Dispatch<React.SetStateAction<boolean>>;
}

const Login: React.FC<LoginProps> = ({ isLoggedIn, setIsLoggedIn }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    try {
      const hashedPassword = SHA256(password).toString();

      const response = await axios.post('http://localhost:8080/login', {
        login: username,
        password: hashedPassword
      });

      if (response.status === 200) {
        setIsLoggedIn(true);
        setIsOpen(false);
        setUsername('');
        setPassword('');
      }
    } catch (error) {
      window.alert('Failed to login!');
      console.error('Failed to login', error);
    }
  };

  return (
    <div className="user-panel">
      {!isLoggedIn && (
        <div className="login-container">
          <button className="login-button" onClick={() => setIsOpen(!isOpen)}>Login</button>
          {isOpen && (
            <form className="login-form" onSubmit={handleSubmit}>
              <input type="text" placeholder="Login" value={username} onChange={e => setUsername(e.target.value)}/>
              <input type="password" placeholder="Password" value={password}
                     onChange={e => setPassword(e.target.value)}/>
              <button type="submit">Submit</button>
            </form>
          )}
          {isLoggedIn && <p>User is logged in</p>}
        </div>
      )}
      {isLoggedIn && (
        <button className="logout-button" onClick={() => setIsLoggedIn(false)}>Logout</button>
      )}
    </div>
  );
};

export default Login;
