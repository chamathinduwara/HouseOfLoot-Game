



house = {
    'main_door':{
        'north':None,
        'east':'living_room',
        'south':None,
        'west':None,
    },
    'living_room':{
        'north':'office',
        'east':'gallery',
        'south':None,
        'west':'main_door',
        'item':'remote'
    },
    'office':{
        'north':'office_bathroom',
        'east':'library',
        'south':'living_room',
        'west':None,
        'item':'pen'
    },
    'office_bathroom':{
        'north':None,
        'east':None,
        'south':'office',
        'west':None,
        'item':'perfume'

    },
    'gallery':{
        'north':'library',
        'east':'sun_room',
        'south':'dining_room',
        'west':'living_room',
        'item':'photo_album'
    },
    'dining_room':{
        'north':'gallery',
        'east':'gym',
        'south':None,
        'west':'kitchen',
        'item':'spoon'
    },
    'kitchen':{
        'north':None,
        'east':'dining_room',
        'south':None,
        'west':None,
        'item':'knife'
    },
    'gym':{
        'north':'sun_room',
        'east':None,
        'south':None,
        'west':'dining_room',
        'item':'year_buds'
    },
    'sun_room':{
        'north':'master_bedroom',
        'east':'end',
        'south':'gym',
        'west':'gallery',
        'item':'cream_bottle'

    },
    'master_bedroom':{
        'north':'master_bathroom',
        'east':None,
        'south':'sun_room',
        'west':'library',
        'item':'glass'

    },
    'master_bathroom':{
        'north':None,
        'east':None,
        'south':'master_bedroom',
        'west':None,
        'item':'soap'

    },
    'library':{
        'north':None,
        'east':'office',
        'south':'gallery',
        'west':'master_bedroom',
        'item':'book'
    },
    'end':{
        'north':None,
        'east':None,
        'south':None,
        'west':'sun_room'
    }

}