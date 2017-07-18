def create_dictionaries(rats, orcs, ghosts, swords, potions):

    enemies = {
            # replaced by the for loops below, which add connections from x, y positions to monsters
            # (rats[0].pos_y, rats[0].pos_x): rats[0],
            # (orcs[0].pos_y, orcs[0].pos_x): orcs[0],
        }

    items = {
            # same as above
            # (swords[0].pos_y, swords[0].pos_x): swords[0],
            # (potions[0].pos_y, potions[0].pos_x): potions[0],
        }


    for i in range(len(rats)):
        enemies.update({(rats[i].pos_y, rats[i].pos_x): rats[i]})

    for i in range(len(orcs)):
        enemies.update({(orcs[i].pos_y, orcs[i].pos_x): orcs[i]})

    for i in range(len(ghosts)):
        enemies.update({(ghosts[i].pos_y, ghosts[i].pos_x): ghosts[i]})


    for i in range(len(swords)):
        items.update({(swords[i].pos_y, swords[i].pos_x): swords[i]})

    for i in range(len(potions)):
        items.update({(potions[i].pos_y, potions[i].pos_x): potions[i]})

    return(enemies, items)
