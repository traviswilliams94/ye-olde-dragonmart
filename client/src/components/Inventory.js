import {useState, useEffect } from 'react';
import ItemCard from "./ItemCard.js";

function Inventory({ filteredItems, searchState, addToCart }){
    const displayItems = filteredItems.filter(item => item.title.toLocaleLowerCase().includes(searchState)).map((item) => (
        <ItemCard key={item.id} item={item} addToCart={addToCart}/>
    ))

    return (
        <div>
            {displayItems}
        </div>
    )
}


export default Inventory;