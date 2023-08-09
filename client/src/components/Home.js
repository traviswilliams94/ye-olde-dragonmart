import React from "react";
import {useState, useEffect} from 'react';
import FeaturedList from './FeaturedList'

function Home({ items, addToCart, removeFromCart }){
    



    return(
        <div>
            <br />
            <h2>Welcome to the Ye Olde Dragonmart!</h2>
            <p>Shop weapons, armor, tools, and magic items til your pockets run dry. You'll never find a better deal in all of Brittania!</p>
            <br />
            <h3>Featured Items:</h3>
            <FeaturedList items={items} addToCart={addToCart} removeFromCart={removeFromCart}/>
            <div></div>
        </div>
    )
}

export default Home;