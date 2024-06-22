import React, { useState } from 'react';
import './App.css';
import Products from "../products/Products";
import Login from "../login/Login";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <div className="App">
      <header className="App-header">
        <Login isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} />
        <Products isLoggedIn={isLoggedIn} />
      </header>
    </div>
  );
}

export default App;
