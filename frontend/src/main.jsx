import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import Navbar from './Navbar.jsx';
import Footer from './Footer.jsx';
import './style.css'; 
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <div className="page-wrapper">
      <Navbar />
      <main className="content">
        <App />
      </main>
      <Footer />
    </div>
  </React.StrictMode>
  
);
