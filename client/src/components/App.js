import React, { useEffect, useState } from "react";
import { Route, Routes } from "react-router-dom";
import NavBar from './NavBar';
import Account from './account';
import Home from './Home';
import Shop from './Shop'
import Cart from './Cart'

function App() {
  const [page, setPage] = useState('/')
  const [items, setItems] = useState([])
  const [wallet, setWallet] = useState(0)
  const [inCart, setInCart] = useState([])

  function addToCart(addedItem){
    const cartItems = inCart.find(
      (item) => item.id === addedItem.id
    );

    if (!cartItems){
      setInCart([...inCart, addedItem]);
    }
  }

  function removeFromCart(removedItem){
    const editedCart = inCart.filter(item => item.title !== removedItem.title);
    setInCart(editedCart);
}
  

  useEffect(() => {
    fetch('http://127.0.0.1:5555/items')
    .then(res => res.json())
    .then(data => {
      setItems(data)
    });
  }, []);

  // useEffect(() => {
  //   const featured = items.
  // })

  return (
    <div className='App'>
      <NavBar onChangePage={setPage}/>
      <Routes>
        <Route path='/shop' element={<Shop items={items} addToCart={addToCart}/>}></Route>
        {/* <Route path='/wishlist' element={<Wishlist />}></Route> */}
        <Route path='/cart' element={<Cart inCart={inCart} setInCart={setInCart} removeFromCart={removeFromCart}/>}></Route>
        <Route path='/account' element={<Account wallet={wallet} setWallet={setWallet}/>}></Route>
        <Route path='/' element={<Home items={items} addToCart={addToCart} removeFromCart={removeFromCart}/>}></Route>
      </Routes>
    </div>
  )
}

export default App;
