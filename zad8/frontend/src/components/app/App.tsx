import React from 'react';
import './App.css';
import Products from "../products/Products";
import Login from "../login/Login";

function App() {
  return (
      <div className="App">
        <header className="App-header">
          <Login />
          <Products />
        </header>
      </div>
  );
}

export default App;
