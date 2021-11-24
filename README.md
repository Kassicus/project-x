# project-x

An unnamed roguelike dungeon crawling game written in python and pygame

# TODO

- [x] Create the base game loop
- [x] Create a player class
- [x] Create a basic room class
- [x] Create a basic projectile class

- [ ] Dynamically confine the players movement to each room `(allowing for different room sizes?)`
- [x] Chain rooms together to create a map *(rework in the future)*
- [ ] Create lockable doors `(player has to use keys? explosives?)` **(this may require starting on an inventory system prior to this step)**
- [ ] Create dynamic collision for all projectile items against the boundaries of the rooms

- [ ] Create basic chasing (melee) enemy
- [ ] Create static turret (projectile) enemy
- [ ] Load enemies dynamically based on room
    - [ ] Save enemy locations if they are left alive when a room is exited `(force player to clear room before moving?)`

- [ ] Create a basic player inventory system `(hotbar and extended inventory menu? [minecraft])` **(may be required before lockable doors)**
- [ ] Create basic equippable items to modify movement speed, weapon damage, ect