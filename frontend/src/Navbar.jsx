import React from "react";
import "./style.css";

const Navbar = () => {
  return (
    <nav>
      <li className="nav-container">
        <span className="logo">STUDY MATE</span>
        <button className="hamburger" id="menu-toggle">&#9776;</button>
      </li>
      <ul id="nav-links">
        <li><a href="/">Home</a></li>
        <li><a href="/note">Class notes</a></li>
        <li><a href="/pyq">Semester PYQ</a></li>
        <li><a href="/cp">CP Practice</a></li>
        <li><a href="/makenote">AI Summarizer</a></li>
        <li><a href="/interview">Interview Tips</a></li>
        <li><a href="/doubt">Ask Doubts</a></li>
        <li><a href="/contact">Contact Us</a></li>
        <li><a href="/login">Login/SignUp</a></li>
      </ul>
    </nav>
  );
};

export default Navbar;
