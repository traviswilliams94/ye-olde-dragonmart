import {useState} from 'react';

function ItemCard({ item, addToCart, inCart, setInCart, removeFromCart }){

    function handleAddToCart(){
        addToCart(item)
        }

    function handleRemove(){
        removeFromCart(item)
    }


    return(
        <div>
            <img className='ui small centered image' src={item.img_url} alt={item.title} />
            <div>{item.title}</div>
            <div>Description: {item.description}</div>
            <div>Price: {item.price}</div>
            <div>
            {!inCart ?
            <button className='cartbutton' onClick={handleAddToCart}>Add to Cart</button>
            : <button className='cartbutton' onClick={handleRemove}>Remove from Cart</button>
            }
            </div>
            <button id='addtowishlist'>Add to Wishlist</button>
        </div>
    )
}

export default ItemCard;

