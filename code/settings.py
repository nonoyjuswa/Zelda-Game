WIDTH = 1280
HEIGHT = 720
FPS = 60
TILE_SIZE = 64
HIT_BOX_OFFSET = {
    'player': -26,
    'object': -40,
    'grass': -10,
    'invisible': 0}

BAR_HEIGHT = 30
ENERGY_BAR_HEIGHT = 10
HEALTH_BAR_WIDTH = 300
ENERGY_BAR_WIDTH = 300
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

WATER_COLOR = '#71ddee'
UI_BG_COLOR = 'black'
UI_BORDER_COLOR = 'grey23'
TEXT_COLOR = '#EEEEEE'

HEALTH_COLOR = 'limegreen'
ENERGY_COLOR = 'darkturquoise'
UI_BORDER_COLOR_ACTIVE = 'gold'

TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': '../graphics/weapons/sword/full.png'},
    'sai': {'cooldown': 80, 'damage': 10, 'graphic': '../graphics/weapons/sai/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic': '../graphics/weapons/rapier/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'graphic': '../graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic': '../graphics/weapons/axe/full.png'}}

magic_data = {
    'flame': {'strength': 5, 'cost': 20, 'graphic': '../graphics/particles/flame/fire.png'},
    'heal': {'strength': 20, 'cost': 10, 'graphic': '../graphics/particles/heal/heal.png'}}

monster_data = {
    'frog': {'health': 100, 'exp': 100, 'damage': 20, 'attack_type': 'pounce', 'attack_sound': '../audio/attack/pounce.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'tengu': {'health': 300, 'exp': 250, 'damage': 40, 'attack_type': 'thunder', 'attack_sound': '../audio/attack/thunder.wav', 'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 100, 'exp': 110, 'damage': 8, 'attack_type': 'fire', 'attack_sound': '../audio/attack/fire.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'giant_slime': {'health': 70, 'exp': 120, 'damage': 6, 'attack_type': 'sparkle', 'attack_sound': '../audio/attack/sparkle.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}