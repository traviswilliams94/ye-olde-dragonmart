import {useState} from 'react';

function ItemCard({ item }){
    return(
        <div>
            <img className='ui small centered image' src={item.img_url} alt={item.title} />
            <div>{item.title}</div>
            <div>Description: {item.description}</div>
            <div>Price: {item.price}</div>
            <button id='addtocart'>Add to Cart</button>
            <button id='addtowishlist'>Add to Wishlist</button>
        </div>
    )
}

export default ItemCard;