import React, { useEffect, useState } from "react";
import { Route, Routes } from "react-router-dom";
import NavBar from './NavBar';
import Account from './account';
import Home from './Home';
import Shop from './Shop'

function App() {
  const [page, setPage] = useState('/')
  const [items, setItems] = useState([])
  const [wallet, setWallet] = useState(0)
  

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
        <Route path='/shop' element={<Shop items={items}/>}></Route>
        {/* <Route path='/wishlist' element={<Wishlist />}></Route>
        <Route path='/cart' element={<Cart />}></Route> */}
        <Route path='/account' element={<Account wallet={wallet} setWallet={setWallet}/>}></Route>
        <Route path='/' element={<Home items={items} />}></Route>
      </Routes>
    </div>
  )
}

export default App;
