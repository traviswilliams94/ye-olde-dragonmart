import React, { useState, useEffect } from 'react';
import Item from './Item';
import Cart from './Cart';

const Store = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch('/api/items')
      .then(response => response.json())
      .then(data => setItems(data));
  }, []);

  return (
    <div className="store">
      <h1>Item Store</h1>
      <div className="items">
        {items.map(item => (
          <Item key={item.id} item={item} />
        ))}
      </div>
    </div>
  );
};

export default Store;