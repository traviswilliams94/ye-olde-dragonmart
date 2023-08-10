import {useState} from 'react';
import { Card, Icon, Image, Button,  CardGroup } from 'semantic-ui-react';

function ItemCard({ item, addToCart, inCart, setInCart, removeFromCart }){

    function handleAddToCart(){
        addToCart(item)
        }

    function handleRemove(){
        removeFromCart(item)
    }


    return(
    
        <div style={{ marginLeft: '5%', paddingBottom: '1%'}}>
        
        <Card style={{ height: '400px'}}>
            <div style={{ height: '60%', overflow: 'hidden' }}>
                <Image
                    src={item.img_url}
                    style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                 />
            </div>
        <Card.Content>
            <Card.Header>{item.title}</Card.Header>
            <Card.Meta>
                <span>Price: ${item.price}</span>
            </Card.Meta>
            <Card.Description>
                {item.description}
            </Card.Description>
        </Card.Content>

            {!inCart ?
            (<Button onClick={handleAddToCart} primary>
                <Button.Content>Add to Cart</Button.Content>
            </Button>)
            : (
            <Button onClick={handleRemove} primary>
                <Button.Content>Remove from Cart</Button.Content>
            </Button>)
            }
            <Button secondary>
                <Button.Content>Add to Wishlist</Button.Content>
            </Button>
        </Card>
        
        </div>
        
    )
}

export default ItemCard;

