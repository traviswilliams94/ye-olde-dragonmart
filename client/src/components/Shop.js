import {useState, useEffect } from 'react'
import Inventory from './Inventory'

function Shop({ items }){

    const [filterBy, setFilterBy] = useState("weapon")
    const [searchState, setSearchState] = useState("")

    const filteredItems = items.filter(
        (item) => item.category === filterBy
    );

    function handleFilterChange(e){
        setFilterBy(e.target.value)
      }

    function handleSearch(e) {
        setSearchState(e.target.value)
    }

    return(
        <div>
            <label>
            <strong>Filter by Category:</strong>
            <select onChange={handleFilterChange} value={filterBy}>
                <option value="weapon">Weapons</option>
                <option value="armor">Armor</option>
                <option value="tool">Tools</option>
                <option value="magic_item">Magic Items</option>
            </select>
            </label>
        <br />
            <div className='searchbar'>
            <input className="prompt" value={searchState}  onChange={handleSearch}/>
            </div>
        <br />
            <h2>Inventory: </h2>
            <Inventory filteredItems={filteredItems} searchState={searchState}/>

        </div>
    )

}

export default Shop;