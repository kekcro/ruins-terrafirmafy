# ruins-terrafirmafy
atomicstryker's ruins tml conversions to tfc blocks


### NOTICE

this is a very rough and shoddy attempt at mapping various vanilla blocks to tfc (1.12) equivalents or closest-partners in color, form, function, etc.
posting this to github not only so i don't lose it but also it will hopefully encourage me to make it better over time

### KNOWN ISSUES

- ~~it sucks~~
- mappings are hardcoded
- rotations are not always respected (i'd say probably 60% of the time because i hate figuring out mojang's godless meta ids and i couldn't find a good "catchall" resource for every single {item_id:meta}, but i didn't look that hard either
- some mappings are more questionable than others
- current hardcoded map relies on addons like firmalife, tfcflorae, chisel, gregtech (why wouldn't you be playing gregtech already lol), etc.
- processing could probably be made more efficient but it works on my machine fast enough

### WIP 
##### (in order of priority)

- move this god awful dict into a csv file of user choice and allow processing using pandas dataframes or whatever
- make a bonafide csv formatting guide for above
- make more accurate rotation / metadata placements for some remaining fringe cases
- add a function that nukes any iteration of silverfish blocks / spawners flawlessly without any external editing because these are the worst fucking stupid mobs in this game fuck you mojang
- clean up documentation
- rebrand to just a general converter / block mapper with TFC as a main focus / example case
