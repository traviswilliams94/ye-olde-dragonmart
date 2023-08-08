#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Item, Customer, Order, OrderItem

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():

        Item.query.delete()
        Customer.query.delete()
        Order.query.delete()
        OrderItem.query.delete()

        print("Starting seed...")

        #weapons
        weapon_1 = Item(title = "Short Sword", description="A quick and light weapon.\nDamage: 1d6 piercing\nProperties: Finesse, Light", category="weapon", price=10, img_url="")
        weapon_2 = Item(title = "Long Sword", description="A versatile blade with good reach.\nDamage: 1d8 slashing\nProperties: Versatile (1d10)", category="weapon", price=15, img_url="")
        weapon_3 = Item(title = "Great Sword", description="A massive two-handed sword for heavy damage.\nDamage: 2d6 slashing\nProperties: Heavy, Two-Handed", category="weapon", price=50, img_url="")
        weapon_4 = Item(title = "Short Bow", description="A compact ranged weapon with a relatively short range, ideal for swift attacks.\nDamage: 1d6 piercing\nProperties: Ammunition (range 80/320), two-handed", category="weapon", price=25, img_url="")
        weapon_5 = Item(title = "Long Bow", description="A large and powerful ranged weapon with great range and accuracy.\nDamage: 1d8 piercing\nProperties: Ammunition (range 150/600), heavy, two-handed", category="weapon", price=50, img_url="")
        weapon_6 = Item(title="Dagger", description="A small, versatile weapon for close combat.\nDamage: 1d4 piercing\nProperties: Finesse, Light, Thrown (range 20/60)", category="weapon", price=2, img_url="")
        weapon_7 = Item(title="Warhammer", description="A versatile weapon for bludgeoning damage.\nDamage: 1d8 bludgeoning\nProperties: Versatile (1d10)", category="weapon", price=15, img_url="")
        weapon_8 = Item(title="Rapier", description="A slender, agile weapon designed for precision.\nDamage: 1d8 piercing\nProperties: Finesse", category="weapon", price=25, img_url="")
        weapon_9 = Item(title="Battleaxe", description="A heavy weapon for chopping and slashing.\nDamage: 1d8 slashing\nProperties: Versatile (1d10)", category="weapon", price=10, img_url="")
        weapon_10 = Item(title="Crossbow, Light", description="A small, handheld crossbow for ranged attacks.\nDamage: 1d8 piercing\nProperties: Ammunition (range 80/320), loading, two-handed", category="weapon", price=25, img_url="")


        #armor
        armor_1 = Item(title = "Leather Armor", description="Light and flexible armor made from leather.\nAC: 11 + DEX ", category="armor", price=10, img_url="")
        armor_2 = Item(title = "Chain Shirt", description="A shirt made of interlocking metal rings.\nAC:13 + DEX (MAX +2)", category="armor", price=50, img_url="")
        armor_3 = Item(title = "Scale Mail", description="Armor made of overlapping metal scales.\nAC:AC:14 + DEX (MAX +2)\nThis armor gives you disadvantage on stealth rolls.", category="armor", price=50, img_url="")
        armor_4 = Item(title = "Chain Mail", description="Heavy armor made of interlocking metal rings.\nAC: 16\nThis armor gives you disadvantage on stealth rolls.", category="armor", price=75, img_url="")
        armor_5 = Item(title = "Plate Armor", description="Full body armor made of large metal plates.\nAC: 18\nThis armor gives you disadvantage on stealth rolls.", category="armor", price=1500, img_url="")
        armor_6 = Item(title="Studded Leather Armor", description="Leather armor reinforced with small metal studs.\nAC: 12 + DEX", category="armor", price=45, img_url="")
        armor_7 = Item(title="Hide Armor", description="A suit of thick and durable hide.\nAC: 12 + DEX (MAX +2)", category="armor", price=10, img_url="")
        armor_8 = Item(title="Breastplate", description="A fitted plate covering the torso.\nAC: 14 + DEX (MAX +2)", category="armor", price=400, img_url="")
        armor_9 = Item(title="Half Plate Armor", description="A combination of plate and chainmail.\nAC: 15 + DEX (MAX +2)\nThis armor gives you disadvantage on stealth rolls.", category="armor", price=750, img_url="")
        armor_10 = Item(title="Ring Mail", description="Chainmail with interlocking metal rings and leather padding.\nAC: 14\nThis armor gives you disadvantage on stealth rolls.", category="armor", price=30, img_url="")


        #tools
        tool_1 = Item(title = "Brewer Supplies", description="Tools and ingredients for brewing alcoholic beverages.", category="tool", price=10, img_url="")
        tool_2 = Item(title = "Carpenters Tools", description="Tools for woodworking and carpentry.", category="tool", price=8, img_url="")
        tool_3 = Item(title = "Cooks Utensils", description="Utensils and tools for cooking and preparing food.", category="tool", price=3, img_url="")
        tool_4 = Item(title = "Dice Set", description="A set of dice used for various games and chance-based activities.", category="tool", price=1, img_url="")
        tool_5 = Item(title = "Bagpipes", description="A musical instrument that produces sound through enclosed reeds.", category="tool", price=30, img_url="")
        tool_6 = Item(title = "Flute", description="A musical instrument that produces sound by blowing air through an opening.", category="tool", price=2, img_url="")
        tool_7 = Item(title = "Thieves Tools", description="Tools used by thieves and rogues for lockpicking and other skills.", category="tool", price=25, img_url="")
        tool_8 = Item(title="Alchemist's Supplies", description="Tools and materials for alchemical experimentation and potion-making.", category="tool", price=50, img_url="")
        tool_9 = Item(title="Calligrapher's Supplies", description="Tools for creating elegant and artistic writing.", category="tool", price=10, img_url="")
        tool_10 = Item(title="Navigator's Tools", description="Instruments for navigation and mapping.", category="tool", price=25, img_url="")
        tool_11 = Item(title="Smith's Tools", description="Tools for metalworking and blacksmithing.", category="tool", price=20, img_url="")
        tool_12 = Item(title="Weaver's Tools", description="Tools for creating textiles and fabrics.", category="tool", price=5, img_url="")


        #magic items
        magic_item_1 = Item(title = "Bag of Holding", description="A magical bag with an interior larger than its exterior, allowing it to hold a vast amount of items.", category="magic_item", price=500, img_url="")
        magic_item_2 = Item(title = "Boots of Elvenkind", description="Magical boots that enhance stealth and agility, making the wearer move quietly.", category="magic_item", price=250, img_url="")
        magic_item_3 = Item(title = "Headband of Intellect", description="A magical headband that increases the wearer's intelligence.", category="magic_item", price=500, img_url="")
        magic_item_4 = Item(title = "Efficient Quiver", description="A magical quiver that can produce any type of ammunition the user desires.", category="magic_item", price=300, img_url="")
        magic_item_5 = Item(title = "Cloak of Protection", description="A magical cloak that provides enhanced protection and resistance against various threats.", category="magic_item", price=400, img_url="")
        magic_item_6 = Item(title="Gloves of Missile Snaring", description="Magical gloves that allow the wearer to catch and deflect projectiles.", category="magic_item", price=300, img_url="")
        magic_item_7 = Item(title="Helm of Telepathy", description="A magical helm that allows the wearer to communicate telepathically.", category="magic_item", price=800, img_url="")
        magic_item_8 = Item(title="Ring of Jumping", description="A magical ring that enhances the wearer's jumping ability.", category="magic_item", price=150, img_url="")
        magic_item_9 = Item(title="Ring of Water Walking", description="A magical ring that allows the wearer to walk on water surfaces.", category="magic_item", price=200, img_url="")
        magic_item_10 = Item(title="Pearl of Power", description="A magical pearl that allows a spellcaster to regain expended spell slots.", category="magic_item", price=450, img_url="")

        print('Committing Item data')
        dnd_items = [weapon_1, weapon_2, weapon_3, weapon_4, weapon_5, weapon_6, weapon_7, weapon_8, weapon_9, weapon_10, armor_1, armor_2, armor_3, armor_4, armor_5, armor_6, armor_7, armor_8, armor_9, armor_10, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11, tool_12, magic_item_1, magic_item_2, magic_item_3, magic_item_4, magic_item_5, magic_item_6, magic_item_7, magic_item_8, magic_item_9, magic_item_10]

        for item in dnd_items:
            db.session.add(item)

        db.session.commit()

        print('Seeding customer data')
        customer_1 = Customer(name = 'Travis Williams', username = 'traviswiliiams', wallet = 100000.00, admin = True)
        customer_1.password_hash = 'password1234'

        print('Seeding orderitem data')
        order_item_1 = OrderItem(quantity = 1, order_id = 1, item_id = 7)
        order_item_2 = OrderItem(quantity = 2, order_id = 1, item_id = 6)
        order_item_3  = OrderItem(quantity = 1, order_id = 1, item_id = 4)

        print('Seeding order data')
        order_1  = Order(customer_id = 1, total = 49.00 )

        print('Commiting customer seed')
        db.session.add_all([customer_1])
        db.session.commit()

        print('Committing orderitem seeds')
        db.session.add_all([order_item_1, order_item_2, order_item_3])
        db.session.commit()

        print('Committing order seed')
        db.session.add_all([order_1])
        db.session.commit()
