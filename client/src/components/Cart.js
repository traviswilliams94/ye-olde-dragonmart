import React from 'react';

const Cart = ({ cartItems }) => {
  return (
    <div className="cart">
      <h2>Cart</h2>
      {cartItems.map((item, index) => (
        <div key={index}>
          <p>{item.title}</p>
          <p>Price: {item.price} gp</p>
        </div>
      ))}
    </div>
  );
};

export default Cart;