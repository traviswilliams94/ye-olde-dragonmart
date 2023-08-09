import {useState, useEffect } from 'react';
import ItemCard from './ItemCard';

function Cart({ inCart, setInCart, removeFromCart }){
    
    const cart = inCart.map((item) => (
        <ItemCard key={item.id} item={item} inCart={inCart} setInCart={setInCart} removeFromCart={removeFromCart}/>
    ))
    return(
        <div>
            <h2>Your Cart:</h2>
            {cart.length > 0 ?
            <div>{cart}
            <p></p>
            <p></p>
            <button className='checkout'>Checkout</button>
            </div>
            : "No items in cart"}
            
            
        </div>
    )
}

export default Cart;