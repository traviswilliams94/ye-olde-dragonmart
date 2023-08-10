import { useState } from 'react';

function Wishlist() {
    const [wishlistItems, setWishlistItems] = useState([]);
    const products = ["Product 1", "Product 2", "Product 3"]; // This is filler

    function addToWishlist(itemName) {
        if (!wishlistItems.includes(itemName)) {
            setWishlistItems(prevItems => [...prevItems, itemName]);
        }
    }

    return (
        <div>
            <div className="products">
                {products.map(product => (
                    <div key={product} className="product">
                        <p>{product}</p>
                        <button onClick={() => addToWishlist(product)}>Add to Wishlist</button>
                    </div>
                ))}
            </div>

            <h2>Your Wishlist</h2>
            <ul>
                {wishlistItems.map(item => (
                    <li key={item}>{item}</li>
                ))}
            </ul>

            <style jsx>{`
                .products {
                    display: flex;
                    justify-content: space-between;
                    padding: 20px;
                }
                
                .product {
                    border: 1px solid black;
                    padding: 20px;
                    width: 150px;
                    text-align: center;
                }
            `}</style>
        </div>
    );
}

export default Wishlist;
