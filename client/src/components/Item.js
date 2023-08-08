import React from 'react';

const Item = ({ item }) => {
    return (
      <div className="item">
        <h3>{item.title}</h3>
        <p>{item.description}</p>
        <p>Price: {item.price} gp</p>
        {/*"Add to Cart" button*/}
      </div>
    );
  };
  
  export default Item;