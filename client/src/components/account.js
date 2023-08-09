import {useState, useEffect } from 'react'
import { NavLink } from "react-router-dom";

function Account({ wallet, setWallet }){

    const [ordersArray, setOrdersArray] = useState([])
    const [amount, setAmount] = useState(0)
    const [formData, setFormData] = useState({
        title: "",
        img_url: "",
        description: "",
        category: "",
        price: "",
    });

// functions to handle changes and submissions to the add money form
    function handleMoneySubmit(event) {
        event.preventDefault();
        addMoney(amount);
        setAmount(0);
    }

    function handleMoneyChange(event) {
        const amount = parseInt(event.target.value)
        setAmount(amount);
    }

    function addMoney(amount) {
        setWallet((wallet) => wallet + amount)
    }

    // functions to handle submitting a new item form
    function handleItemChange(event){
        const name = event.target.name;
        let value = event.target.value

        setFormData({
            ...formData,
            [name]: value,
        });
    }

    function handleItemSubmit(event) {
        event.preventDefault();
        // const data = event.target;

        // let formData = {
        //     title: data.title.value,
        //     img_url: data.img_url.value,
        //     description: data.description.value,
        //     category: data.category.value,
        //     price: data.price.value
        // }
        
        fetch('/items', {
            method: 'POST',
            mode: "no-cors",
            headers: {
                "Content-Type": 'application/json',
            },
            body:  JSON.stringify(formData),
        })
        .then((res) => res.json())
        .then((newItem) => console.log(newItem));
    }

    return (
        <div>
            <div id="wallet">
                <h3>Wallet: {wallet} GP</h3>
                <form onSubmit={handleMoneySubmit}>
                    <input onChange={handleMoneyChange}
                        type='number'
                        name='addmoney'
                        value={amount}
                        placeholder='Type amount to add'
                    />
                    <button type='submit' id="addmoney">Add Money</button>
                </form>
            </div>
            <div>
                <h3>Your Orders:</h3>
                <p>list of orders here</p>
            </div>
            <div className='newitemform'>
                <h3>Add New Item - Admin Only:</h3>
                <form id="addnewitem" onSubmit={handleItemSubmit}>
                    <label>Title: </label>
                    <input 
                    type='text'
                    name='title'
                    onChange={handleItemChange}
                    value={formData.title}
                    placeholder='Enter New Item Title'
                    />
                <br />
                    <label>Image Url: </label>
                    <input
                    type='text'
                    name='img_url'
                    onChange={handleItemChange}
                    value={formData.img_url}
                    placeholder='Enter New Item Image URL'
                    />
                <br />
                    <label>Description: </label>
                    <input 
                    type='text'
                    name='description'
                    onChange={handleItemChange}
                    value={formData.description}
                    placeholder='Enter New Item Description'/>
                <br />
                    <label>Category: </label>
                    <select name='category' onChange={handleItemChange} value={formData.category}>
                        <option value='weapon'>weapon</option>
                        <option value='armor'>armor</option>
                        <option value='tool'>tool</option>
                        <option value='magic_item'>magic_item</option>
                    </select>
                <br />
                    <label>Price: </label>
                    <input 
                    type='number'
                    name='price'
                    onChange={handleItemChange}
                    value={formData.price}
                    placeholder='Enter New Item Price'
                    />
                <br />
                    <button type='submit' id="newItem">Add Item to Inventory</button>
                </form>
            </div>
            <div className='itemupdateform'>
                <form id='updateform'>


                </form>
            </div>
            

        </div>
    )
}

export default Account;