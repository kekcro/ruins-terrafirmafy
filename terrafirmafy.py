# Make sure you backup your ruins .tml files before running in case this explodes them
# Also make sure you remove the "minecraft:" designator from those files - this script relies on that and it's easy enough to do in Notepad++ or some loonix equivalent

import re
from pathlib import Path

# Replace with the target directory containing your .tml ruins files
ruins = list(Path("C:\\testing").rglob("**/*.[tT][mM][lL]"))

map = {}

# Water
map['tfc:fluid/fresh_water'] = ['water', 'water-0', 'water-1', 'flowing_water', 'flowing_water-0', 'water-9']
# Stone
map['tfc:raw/slate'] = ['stone', 'stone-0']
map['tfc:raw/chert'] = ['stone-1']
map['tfc:smooth/chert'] = ['stone-2']
map['tfc:raw/diorite'] = ['stone-3']
map['tfc:smooth/diorite'] = ['stone-4']
map['tfc:raw/andesite'] = ['stone-5']
map['tfc:smooth/andesite'] = ['stone-6']
# Farmland
map['tfcflorae:single/loam_farmland'] = ['farmland', 'farmland-0', 'farmland-7']
# Mycelium
map['tfcflorae:podzol/conglomerate'] = ['mycelium', 'mycelium-0']
# Grass, Dirt
map['tfcflorae:single/loam_grass'] = ['grass', 'grass-0']
map['tfcflorae:single/loam'] = ['dirt', 'dirt-0']
map['tfcflorae:single/coarse_loam'] = ['dirt-1']
map['tfcflorae:single/loam_podzol'] = ['dirt-2']
map['tfcflorae:single/dry_loam_grass'] = ['grass_path', 'grass_path-0']
# Tall Grass
map['tfc:plants/scutch_grass-2'] = ['tallgrass', 'tallgrass-0']
map['tfc:plants/wheatgrass-2'] = ['tallgrass-1']
map['tfc:plants/crowngrass-2'] = ['tallgrass-2']
# Flowers
map['tfc:plants/dandelion'] = ['yellow_flower', 'yellow_flower-0']
map['tfc:plants/poppy'] = ['red_flower', 'red_flower-0']
map['tfc:plants/blue_orchid'] = ['red_flower-1']
map['tfc:plants/allium'] = ['red_flower-2']
map['tfc:plants/houstonia'] = ['red_flower-3']
map['tfc:plants/tulip_red'] = ['red_flower-4']
map['tfc:plants/tulip_orange'] = ['red_flower-5']
map['tfc:plants/tulip_white'] = ['red_flower-6']
map['tfc:plants/tulip_pink'] = ['red_flower-7']
map['tfc:plants/oxeye_daisy'] = ['red_flower-8']
map['tfc:plants/water_lily'] = ['waterlily', 'waterlily-0']
map['tfc:plants/sunflower'] = ['double_plant', 'double_plant-0', 'double_plant-10']
map['tfc:plants/lilac'] = ['double_plant-1']
map['tfc:plants/tall_fescue_grass'] = ['double_plant-2']
map['tfc:plants/cinnamon_fern'] = ['double_plant-3']
map['tfc:plants/rose'] = ['double_plant-4']
map['tfc:plants/peony'] = ['double_plant-5']
# Vines
map['tfcflorae:plants/jungle_vine_creeping'] = ['vine', 'vine-0', 'vine-1', 'vine-2', 'vine-3', 'vine-4', 'vine-5', 'vine-6', 'vine-7', 'vine-8', 'vine-9', 'vine-10', 'vine-11', 'vine-12', 'vine-13', 'vine-14', 'vine-15']
# Mushrooms
map['tfc:plants/porcini'] = ['brown_mushroom','brown_mushroom-0']
map['tfc:plants/amanita'] = ['red_mushroom','red_mushroom-0']
# Cobblestone
map['gregtech:stone_cobble-4'] = ['cobblestone', 'cobblestone-0']
map['gregtech:stone_cobble_mossy-4'] = ['mossy_cobblestone', 'mossy_cobblestone-0']
# Planks
map['tfc:wood/planks/oak'] = ['planks', 'planks-0']
map['tfc:wood/planks/spruce'] = ['planks-1']
map['tfc:wood/planks/birch'] = ['planks-2']
map['tfc:wood/planks/yew'] = ['planks-3']
map['tfc:wood/planks/acacia'] = ['planks-4']
map['tfc:wood/planks/blackwood'] = ['planks-5']
# Sand, Gravel
map['tfc:sand/sandstone'] = ['sand', 'sand-0']
map['tfc:sand/claystone'] = ['sand-1']
map['tfc:gravel/slate'] = ['gravel', 'gravel-0']
# Sandstone
map['tfc:bricks/sandstone'] = ['sandstone', 'sandstone-0']
map['tfc:smooth/sandstone'] = ['sandstone-1', 'sandstone-2']
map['tfc:bricks/claystone'] = ['red_sandstone', 'red_sandstone-0']
map['tfc:smooth/claystone'] = ['red_sandstone-1', 'red_sandstone-2']
# Ores
map['minecraft:gold_block'] = ['gold_ore', 'gold_ore-0']
map['minecraft:iron_block'] = ['iron_ore', 'iron_ore-0']
map['minecraft:coal_block'] = ['coal_ore', 'coal_ore-0']
map['minecraft:lapis_block'] = ['lapis_ore', 'lapis_ore-0']
map['minecraft:diamond_block'] = ['diamond_ore', 'diamond_ore-0']
map['minecraft:redstone_block'] = ['redstone_ore', 'redstone_ore-0']
map['minecraft:emerald_block'] = ['emerald_ore', 'redstone_ore-0']
map['minecraft:quartz_block'] = ['quartz_ore', 'redstone_ore-0']
# Logs
map['tfc:wood/log/oak-4'] = ['log-4']
map['tfc:wood/log/oak-5'] = ['log', 'log-0', 'log-12']
map['tfc:wood/log/oak-6'] = ['log-8']
map['tfc:wood/log/spruce-4'] = ['log-5']
map['tfc:wood/log/spruce-5'] = ['log-1', 'log-13']
map['tfc:wood/log/spruce-6'] = ['log-9']
map['tfc:wood/log/birch-4'] = ['log-6']
map['tfc:wood/log/birch-5'] = ['log-2']
map['tfc:wood/log/birch-6'] = ['log-10']
map['tfc:wood/log/yew-4'] = ['log-7']
map['tfc:wood/log/yew-5'] = ['log-3', 'log-15']
map['tfc:wood/log/yew-6'] = ['log-11']
map['tfc:wood/log/acacia-4'] = ['log2-4']
map['tfc:wood/log/acacia-5'] = ['log2', 'log2-0', 'log2-12']
map['tfc:wood/log/acacia-6'] = ['log2-8']
map['tfc:wood/log/blackwood-4'] = ['log2-5']
map['tfc:wood/log/blackwood-5'] = ['log2-1', 'log2-13']
map['tfc:wood/log/blackwood-6'] = ['log2-9']
# Leaves
map['tfc:wood/leaves/oak'] = ['leaves', 'leaves-0', 'leaves-4', 'leaves-8', 'leaves-12']
map['tfc:wood/leaves/spruce'] = ['leaves-1', 'leaves-5', 'leaves-9', 'leaves-13']
map['tfc:wood/leaves/birch'] = ['leaves-2', 'leaves-6', 'leaves-10', 'leaves-14']
map['tfc:wood/leaves/yew'] = ['leaves-3', 'leaves-7', 'leaves-11', 'leaves-15']
map['tfc:wood/leaves/acacia'] = ['leaves2', 'leaves2-0']
map['tfc:wood/leaves/blackwood'] = ['leaves2-1']
# Slabs
map['tfc:double_slab/smooth/marble'] = ['double_stone_slab', 'double_stone_slab-0', 'double_stone_slab-8']
map['tfc:double_slab/cobble/sandstone'] = ['double_stone_slab-1', 'double_stone_slab-9']
map['tfc:double_slab/cobble/claystone'] = ['double_stone_slab2', 'double_stone_slab2-0', 'double_stone_slab2-8']
map['tfc:double_slab/wood/oak'] = ['double_stone_slab-2', 'double_wooden_slab', 'double_wooden_slab-0']
map['tfc:double_slab/wood/spruce'] = ['double_wooden_slab-1']
map['tfc:double_slab/wood/birch'] = ['double_wooden_slab-2']
map['tfc:double_slab/wood/yew'] = ['double_wooden_slab-3']
map['tfc:double_slab/wood/acacia'] = ['double_wooden_slab-4']
map['tfc:double_slab/wood/blackwood'] = ['double_wooden_slab-5']
map['tfc:double_slab/cobble/slate'] = ['double_stone_slab-3']
map['tfc:double_slab/bricks/slate'] = ['double_stone_slab-5']
map['tfc:double_slab/bricks/basalt'] = ['double_stone_slab-6']
map['tfc:slab/smooth/marble'] = ['stone_slab', 'stone_slab-0']
map['tfc:slab/smooth/marble-8'] = ['stone_slab-8']
map['tfc:slab/cobble/sandstone'] = ['stone_slab-1']
map['tfc:slab/cobble/sandstone-8'] = ['stone_slab-9']
map['tfc:slab/cobble/claystone'] = ['stone_slab2', 'stone_slab2-0']
map['tfc:slab/cobble/claystone-8'] = ['stone_slab2-8']
map['tfc:slab/wood/oak'] = ['stone_slab-2', 'wooden_slab', 'wooden_slab-0']
map['tfc:slab/wood/oak-8'] = ['wooden_slab-8']
map['tfc:slab/wood/spruce'] = ['wooden_slab-1']
map['tfc:slab/wood/spruce-8'] = ['wooden_slab-9']
map['tfc:slab/wood/birch'] = ['wooden_slab-2']
map['tfc:slab/wood/birch-8'] = ['wooden_slab-10']
map['tfc:slab/wood/yew'] = ['wooden_slab-3']
map['tfc:slab/wood/yew-8'] = ['wooden_slab-11']
map['tfc:slab/wood/acacia'] = ['wooden_slab-4']
map['tfc:slab/wood/acacia-8'] = ['wooden_slab-12']
map['tfc:slab/wood/blackwood'] = ['wooden_slab-5']
map['tfc:slab/wood/blackwood-8'] = ['wooden_slab-13']
map['tfc:slab/cobble/slate'] = ['stone_slab-3']
map['tfc:slab/cobble/slate-8'] = ['stone_slab-11']
map['tfc:slab/bricks/slate'] = ['stone_slab-5']
map['tfc:slab/bricks/slate-8'] = ['stone_slab-13']
map['tfc:slab/bricks/basalt'] = ['stone_slab-6']
map['tfc:slab/bricks/basalt-8'] = ['stone_slab-14']
# Stairs
map['tfc:stairs/cobble/conglomerate'] = ['stone_stairs', 'stone_stairs-0']
map['tfc:stairs/cobble/conglomerate-1'] = ['stone_stairs-1']
map['tfc:stairs/cobble/conglomerate-2'] = ['stone_stairs-2']
map['tfc:stairs/cobble/conglomerate-3'] = ['stone_stairs-3']
map['tfc:stairs/cobble/conglomerate-4'] = ['stone_stairs-4']
map['tfc:stairs/cobble/conglomerate-5'] = ['stone_stairs-5']
map['tfc:stairs/cobble/conglomerate-6'] = ['stone_stairs-6']
map['tfc:stairs/cobble/conglomerate-7'] = ['stone_stairs-7']
map['tfc:stairs/wood/oak'] = ['oak_stairs', 'oak_stairs-0']
map['tfc:stairs/wood/oak-1'] = ['oak_stairs-1']
map['tfc:stairs/wood/oak-2'] = ['oak_stairs-2']
map['tfc:stairs/wood/oak-3'] = ['oak_stairs-3']
map['tfc:stairs/wood/oak-4'] = ['oak_stairs-4']
map['tfc:stairs/wood/oak-5'] = ['oak_stairs-5']
map['tfc:stairs/wood/oak-6'] = ['oak_stairs-6']
map['tfc:stairs/wood/oak-7'] = ['oak_stairs-7']
map['tfc:stairs/wood/spruce'] = ['spruce_stairs', 'spruce_stairs-0']
map['tfc:stairs/wood/spruce-1'] = ['spruce_stairs-1']
map['tfc:stairs/wood/spruce-2'] = ['spruce_stairs-2']
map['tfc:stairs/wood/spruce-3'] = ['spruce_stairs-3']
map['tfc:stairs/wood/spruce-4'] = ['spruce_stairs-4']
map['tfc:stairs/wood/spruce-5'] = ['spruce_stairs-5']
map['tfc:stairs/wood/spruce-6'] = ['spruce_stairs-6']
map['tfc:stairs/wood/spruce-7'] = ['spruce_stairs-7']
map['tfc:stairs/wood/birch'] = ['birch_stairs', 'birch_stairs-0']
map['tfc:stairs/wood/birch-1'] = ['birch_stairs-1']
map['tfc:stairs/wood/birch-2'] = ['birch_stairs-2']
map['tfc:stairs/wood/birch-3'] = ['birch_stairs-3']
map['tfc:stairs/wood/birch-4'] = ['birch_stairs-4']
map['tfc:stairs/wood/birch-5'] = ['birch_stairs-5']
map['tfc:stairs/wood/birch-6'] = ['birch_stairs-6']
map['tfc:stairs/wood/birch-7'] = ['birch_stairs-7']
map['tfc:stairs/wood/yew'] = ['jungle_stairs', 'jungle_stairs-0']
map['tfc:stairs/wood/yew-1'] = ['jungle_stairs-1']
map['tfc:stairs/wood/yew-2'] = ['jungle_stairs-2']
map['tfc:stairs/wood/yew-3'] = ['jungle_stairs-3']
map['tfc:stairs/wood/yew-4'] = ['jungle_stairs-4']
map['tfc:stairs/wood/yew-5'] = ['jungle_stairs-5']
map['tfc:stairs/wood/yew-6'] = ['jungle_stairs-6']
map['tfc:stairs/wood/yew-7'] = ['jungle_stairs-7']
map['tfc:stairs/wood/acacia'] = ['acacia_stairs', 'acacia_stairs-0']
map['tfc:stairs/wood/acacia-1'] = ['acacia_stairs-1']
map['tfc:stairs/wood/acacia-2'] = ['acacia_stairs-2']
map['tfc:stairs/wood/acacia-3'] = ['acacia_stairs-3']
map['tfc:stairs/wood/acacia-4'] = ['acacia_stairs-4']
map['tfc:stairs/wood/acacia-5'] = ['acacia_stairs-5']
map['tfc:stairs/wood/acacia-6'] = ['acacia_stairs-6']
map['tfc:stairs/wood/acacia-7'] = ['acacia_stairs-7']
map['tfc:stairs/wood/blackwood'] = ['dark_oak_stairs', 'dark_oak_stairs-0']
map['tfc:stairs/wood/blackwood-1'] = ['dark_oak_stairs-1']
map['tfc:stairs/wood/blackwood-2'] = ['dark_oak_stairs-2']
map['tfc:stairs/wood/blackwood-3'] = ['dark_oak_stairs-3']
map['tfc:stairs/wood/blackwood-4'] = ['dark_oak_stairs-4']
map['tfc:stairs/wood/blackwood-5'] = ['dark_oak_stairs-5']
map['tfc:stairs/wood/blackwood-6'] = ['dark_oak_stairs-6']
map['tfc:stairs/wood/blackwood-7'] = ['dark_oak_stairs-7']
map['tfc:stairs/bricks/slate'] = ['stone_brick_stairs', 'stone_brick_stairs-0']
map['tfc:stairs/bricks/slate-1'] = ['stone_brick_stairs-1']
map['tfc:stairs/bricks/slate-2'] = ['stone_brick_stairs-2']
map['tfc:stairs/bricks/slate-3'] = ['stone_brick_stairs-3']
map['tfc:stairs/bricks/slate-4'] = ['stone_brick_stairs-4']
map['tfc:stairs/bricks/slate-5'] = ['stone_brick_stairs-5']
map['tfc:stairs/bricks/slate-6'] = ['stone_brick_stairs-6']
map['tfc:stairs/bricks/slate-7'] = ['stone_brick_stairs-7']
map['tfc:stairs/cobble/sandstone'] = ['sandstone_stairs', 'sandstone_stairs-0']
map['tfc:stairs/cobble/sandstone-1'] = ['sandstone_stairs-1']
map['tfc:stairs/cobble/sandstone-2'] = ['sandstone_stairs-2']
map['tfc:stairs/cobble/sandstone-3'] = ['sandstone_stairs-3']
map['tfc:stairs/cobble/sandstone-4'] = ['sandstone_stairs-4']
map['tfc:stairs/cobble/sandstone-5'] = ['sandstone_stairs-5']
map['tfc:stairs/cobble/sandstone-6'] = ['sandstone_stairs-6']
map['tfc:stairs/cobble/sandstone-7'] = ['sandstone_stairs-7']
map['tfc:stairs/cobble/claystone'] = ['red_sandstone_stairs', 'red_sandstone_stairs-0']
map['tfc:stairs/cobble/claystone-1'] = ['red_sandstone_stairs-1']
map['tfc:stairs/cobble/claystone-2'] = ['red_sandstone_stairs-2']
map['tfc:stairs/cobble/claystone-3'] = ['red_sandstone_stairs-3']
map['tfc:stairs/cobble/claystone-4'] = ['red_sandstone_stairs-4']
map['tfc:stairs/cobble/claystone-5'] = ['red_sandstone_stairs-5']
map['tfc:stairs/cobble/claystone-6'] = ['red_sandstone_stairs-6']
map['tfc:stairs/cobble/claystone-7'] = ['red_sandstone_stairs-7']
map['tfc:stairs/bricks/basalt'] = ['nether_brick_stairs', 'nether_brick_stairs-0']
map['tfc:stairs/bricks/basalt-1'] = ['nether_brick_stairs-1']
map['tfc:stairs/bricks/basalt-2'] = ['nether_brick_stairs-2']
map['tfc:stairs/bricks/basalt-3'] = ['nether_brick_stairs-3']
map['tfc:stairs/bricks/basalt-4'] = ['nether_brick_stairs-4']
map['tfc:stairs/bricks/basalt-5'] = ['nether_brick_stairs-5']
map['tfc:stairs/bricks/basalt-6'] = ['nether_brick_stairs-6']
map['tfc:stairs/bricks/basalt-7'] = ['nether_brick_stairs-7']
# Crafting Table, Furnace, Chest
map['tfc:wood/workbench/oak'] = ['crafting_table', 'crafting_table-0']
map['firmalife:oven-10'] = ['furnace-2']
map['firmalife:oven-8'] = ['furnace-3']
map['firmalife:oven-9'] = ['furnace-4']
map['firmalife:oven-11'] = ['furnace-5']
map['tfc:wood/chest/oak'] = ['chest', 'chest-0', 'trapped_chest', 'trapped_chest-0', 'chest-1', 'chest-2', 'chest-3', 'chest-4', 'chest-5', 'chest-6', 'chest-7']
# Crops
map['tfc:crop/wheat'] = ['wheat', 'wheat-0', 'wheat-1', 'wheat-2', 'wheat-3', 'wheat-4', 'wheat-5', 'wheat-6', 'wheat-7']
map['tfc:plant/giant_cane-2'] = ['reeds', 'reeds-0']
map['firmalife:pumpkin_fruit'] = ['pumpkin', 'pumpkin-0', 'pumpkin_stem-7']
map['firmalife:lit_pumpkin_face'] = ['lit_pumpkin', 'lit_pumpkin-0', 'lit_pumpkin-1', 'lit_pumpkin-2']
map['firmalife:melon_fruit'] = ['melon', 'melon-0', 'melon_stem-7']
map['tfc:crop/carrots'] = ['carrots', 'carrots-0', 'carrots-1', 'carrots-2', 'carrots-3', 'carrots-4', 'carrots-5']
map['tfc:crop/potatoes'] = ['potatoes', 'potatoes-0', 'potatoes-1', 'potatoes-2', 'potatoes-3', 'potatoes-4', 'potatoes-5']
# Door, Trapdoor, Pressure Plate, Button, Fence, Wall, Gate, Bookshelf
map['tfc:wood/door/oak'] = ['wooden_door', 'wooden_door-0']
map['tfc:wood/door/oak-1'] = ['wooden_door-1']
map['tfc:wood/door/oak-2'] = ['wooden_door-2']
map['tfc:wood/door/oak-3'] = ['wooden_door-3']
map['tfc:wood/door/oak-4'] = ['wooden_door-4']
map['tfc:wood/door/oak-5'] = ['wooden_door-5']
map['tfc:wood/door/oak-6'] = ['wooden_door-6']
map['tfc:wood/door/oak-7'] = ['wooden_door-7']
map['tfc:wood/door/oak-8'] = ['wooden_door-8']
map['tfc:wood/door/oak-9'] = ['wooden_door-9']
map['tfc:wood/door/spruce'] = ['spruce_door', 'spruce_door-0']
map['tfc:wood/door/spruce-1'] = ['spruce_door-1']
map['tfc:wood/door/spruce-2'] = ['spruce_door-2']
map['tfc:wood/door/spruce-3'] = ['spruce_door-3']
map['tfc:wood/door/spruce-4'] = ['spruce_door-4']
map['tfc:wood/door/spruce-5'] = ['spruce_door-5']
map['tfc:wood/door/spruce-6'] = ['spruce_door-6']
map['tfc:wood/door/spruce-7'] = ['spruce_door-7']
map['tfc:wood/door/spruce-8'] = ['spruce_door-8']
map['tfc:wood/door/spruce-9'] = ['spruce_door-9']
map['tfc:wood/door/birch'] = ['birch_door', 'birch_door-0']
map['tfc:wood/door/birch-1'] = ['birch_door-1']
map['tfc:wood/door/birch-2'] = ['birch_door-2']
map['tfc:wood/door/birch-3'] = ['birch_door-3']
map['tfc:wood/door/birch-4'] = ['birch_door-4']
map['tfc:wood/door/birch-5'] = ['birch_door-5']
map['tfc:wood/door/birch-6'] = ['birch_door-6']
map['tfc:wood/door/birch-7'] = ['birch_door-7']
map['tfc:wood/door/birch-8'] = ['birch_door-8']
map['tfc:wood/door/birch-9'] = ['birch_door-9']
map['tfc:wood/door/yew'] = ['jungle_door', 'jungle_door-0']
map['tfc:wood/door/yew-1'] = ['jungle_door-1']
map['tfc:wood/door/yew-2'] = ['jungle_door-2']
map['tfc:wood/door/yew-3'] = ['jungle_door-3']
map['tfc:wood/door/yew-4'] = ['jungle_door-4']
map['tfc:wood/door/yew-5'] = ['jungle_door-5']
map['tfc:wood/door/yew-6'] = ['jungle_door-6']
map['tfc:wood/door/yew-7'] = ['jungle_door-7']
map['tfc:wood/door/yew-8'] = ['jungle_door-8']
map['tfc:wood/door/yew-9'] = ['jungle_door-9']
map['tfc:wood/door/acacia'] = ['acacia_door', 'acacia_door-0']
map['tfc:wood/door/acacia-1'] = ['acacia_door-1']
map['tfc:wood/door/acacia-2'] = ['acacia_door-2']
map['tfc:wood/door/acacia-3'] = ['acacia_door-3']
map['tfc:wood/door/acacia-4'] = ['acacia_door-4']
map['tfc:wood/door/acacia-5'] = ['acacia_door-5']
map['tfc:wood/door/acacia-6'] = ['acacia_door-6']
map['tfc:wood/door/acacia-7'] = ['acacia_door-7']
map['tfc:wood/door/acacia-8'] = ['acacia_door-8']
map['tfc:wood/door/acacia-9'] = ['acacia_door-9']
map['tfc:wood/door/blackwood'] = ['dark_oak_door', 'dark_oak_door-0']
map['tfc:wood/door/blackwood-1'] = ['dark_oak_door-1']
map['tfc:wood/door/blackwood-2'] = ['dark_oak_door-2']
map['tfc:wood/door/blackwood-3'] = ['dark_oak_door-3']
map['tfc:wood/door/blackwood-4'] = ['dark_oak_door-4']
map['tfc:wood/door/blackwood-5'] = ['dark_oak_door-5']
map['tfc:wood/door/blackwood-6'] = ['dark_oak_door-6']
map['tfc:wood/door/blackwood-7'] = ['dark_oak_door-7']
map['tfc:wood/door/blackwood-8'] = ['dark_oak_door-8']
map['tfc:wood/door/blackwood-9'] = ['dark_oak_door-9']
map['tfc:wood/trapdoor/oak'] = ['trapdoor', 'trapdoor-0', 'trapdoor-1', 'trapdoor-2', 'trapdoor-3', 'trapdoor-4', 'trapdoor-5', 'trapdoor-6', 'trapdoor-7', 'trapdoor-8', 'trapdoor-9', 'trapdoor-10', 'trapdoor-11', 'trapdoor-12', 'trapdoor-13', 'trapdoor-14', 'trapdoor-15']
map['tfc:wood/pressure_plate/oak'] = ['wooden_pressure_plate', 'wooden_pressure_plate-0']
map['tfc:stone/pressure_plate/slate'] = ['stone_pressure_plate', 'stone_pressure_plate-0']
map['tfc:wood/button/oak'] = ['wooden_button', 'wooden_button-0', 'wooden_button-1', 'wooden_button-2', 'wooden_button-3', 'wooden_button-4']
map['tfc:stone/button/slate'] = ['stone_button', 'stone_button-0', 'stone_button-1', 'stone_button-2', 'stone_button-3', 'stone_button-4']
map['tfc:wood/fence/oak'] = ['fence', 'fence-0']
map['tfc:wood/fence/spruce'] = ['spruce_fence', 'spruce_fence-0']
map['tfc:wood/fence/birch'] = ['birch_fence', 'birch_fence-0']
map['tfc:wood/fence/yew'] = ['jungle_fence', 'jungle_fence-0']
map['tfc:wood/fence/acacia'] = ['acacia_fence', 'acacia_fence-0']
map['tfc:wood/fence/blackwood'] = ['dark_oak_fence', 'dark_oak_fence-0']
map['tfc:wood/fence_gate/oak'] = ['fence_gate', 'fence_gate-0', 'fence_gate-1', 'fence_gate-2', 'fence_gate-3', 'fence_gate-4', 'fence_gate-5']
map['tfc:wood/fence_gate/spruce'] = ['spruce_fence_gate', 'spruce_fence_gate-0', 'spruce_fence_gate-1', 'spruce_fence_gate-2', 'spruce_fence_gate-3', 'spruce_fence_gate-4', 'spruce_fence_gate-5', 'spruce_fence_gate-6', 'spruce_fence_gate-7']
map['tfc:wood/fence_gate/birch'] = ['birch_fence_gate', 'birch_fence_gate-0', 'birch_fence_gate-1', 'spruce_fence_gate-5']
map['tfc:wood/fence_gate/yew'] = ['jungle_fence_gate', 'jungle_fence_gate-0', 'jungle_fence_gate-1']
map['tfc:wood/fence_gate/acacia'] = ['acacia_fence_gate', 'acacia_fence_gate-0', 'acacia_fence_gate-1']
map['tfc:wood/fence_gate/blackwood'] = ['dark_oak_fence_gate', 'dark_oak_fence_gate-0', 'dark_oak_fence_gate-1', 'dark_oak_fence_gate-2', 'dark_oak_fence_gate-3', 'dark_oak_fence_gate-4', 'dark_oak_fence_gate-5']
map['tfc:wall/cobble/slate'] = ['cobblestone_wall', 'cobblestone_wall-0', 'cobblestone_wall-1']
map['tfc:wood/bookshelf/oak'] = ['bookshelf', 'bookshelf-0']
# Nether
map['tfcflorae:coarse_dirt/conglomerate'] = ['netherrack', 'netherrack-0']
map['tfcflorae:coarse_dirt/mudstone'] = ['soul_sand', 'soul_sand-0']
map['gregtech:stone_bricks-1'] = ['red_nether_brick', 'red_nether_brick-0']
map['tfc:bricks/basalt'] = ['nether_brick', 'nether_brick-0']
map['tfc:wall/bricks/basalt'] = ['nether_brick_fence', 'nether_brick_fence-0']
map['tfc:stairs/bricks/basalt'] = ['nether_brick_stairs', 'nether_brick_stairs-0']
# Stone Bricks
map['tfc:bricks/slate'] = ['stonebrick', 'stonebrick-0', 'stonebrick-2', 'stonebrick-3']
map['tfcflorae:mossy_raw/slate'] = ['stonebrick-1']

def analyze(rule, blocks):
    leftoverBlocks = blocks
    deconstructedRule = rule.split(',')
    for block in deconstructedRule[2:]:
        if 'tfc:' not in block \
        and 'tfcflorae:' not in block \
        and 'firmalife:' not in block \
        and 'gregtech:' not in block \
        and 'chisel:' not in block \
        and 'CommandBlock:' not in block:
            leftoverBlocks.append(block)
    return leftoverBlocks

def terrafirmafy(rule, map):
    converted = False
    deconstructedRule = rule.split(',')
    reconstructedRule = deconstructedRule[0]+","+deconstructedRule[1]
    for block in deconstructedRule[2:]:
        for tfc, minecraft in zip(map.keys(), map.values()):
            if block in minecraft:
                reconstructedRule += ","+tfc
                converted = True
                break
        if not converted:
            reconstructedRule += ","+block
    return reconstructedRule+"\n"
    
def emptyInventory(rule):
    converted = False
    deconstructedRule = rule.split(',')
    reconstructedRule = deconstructedRule[0]+","+deconstructedRule[1]
    for block in deconstructedRule[2:]:
        if "IInventory;chest;" in block:
            reconstructedRule += ","+'tfc:wood/chest/oak'+"\n"
            converted = True
            break
        elif "ChestGenHook:" in block:
            reconstructedRule += ","+'tfc:wood/chest/oak'+"\n"
            converted = True
            break
        elif "IInventory;furnace;" in block:
            reconstructedRule += ","+'firmalife:oven-10'+"\n"
            converted = True
            break
        elif "IInventory;hopper;" in block:
            reconstructedRule += ","+'minecraft:hopper'+"\n"
            converted = True
            break
        elif "IInventory;dropper;" in block:
            reconstructedRule += ","+'minecraft:dropper'+"\n"
            converted = True
            break
    if not converted:
        reconstructedRule += ","+block
    return reconstructedRule

blocks = []
newBlocks = []
for ruin in ruins:
    update = ""
    with open(ruin, 'r') as ruinfile:
        for line in ruinfile.readlines():
            for line in re.findall('^rule\d\d?=\d,\d+,\D.*', line, re.MULTILINE):
                line = terrafirmafy(line, map)
                line = emptyInventory(line)
                # Uncomment "#2" to get analytics on blocks used that don't match the "analyze" criteria
                #2 newBlocks = []
                #2 newBlocks = analyze(line, newBlocks)
                #2 blocks += newBlocks
            update += line
    with open(ruin, 'w') as ruinfile:
        ruinfile.write(update)

#2 for block in set(blocks):
    #2 print(block)