import random
import streamlit as st
from PIL import Image
destiny_subclasses = {
    "Warlock": {
        "Stormcaller": {
            "Super": ["Stormtrance", "Chaos Reach"],
            "Grenade": ["Arcbolt Grenade", "Flux Grenade", "Skip Grenade", "Flashbang Grenade", "Lightning Grenade", "Pulse Grenade", "Storm Grenade"],
            "Melee": ["Chain Lightning", "Ball Lightning"],
            "Class Ability": ["Healing Rift", "Empowering Rift"]
            
        },
        "Dawnblade": {
            "Super": ["Well of Radiance", "Daybreak"],
            "Grenade": ["Incendiary Grenade", "Swarm Grenade", "Tripmine Grenade", "Fusion Grenade", "Incendiary Grenade", "Thermite Grenade", "Firebolt Grenade", "Healing Grenade"],
            "Melee": ["Celestial Fire", "Incinerator Snap"],
            "Class Ability": ["Healing Rift", "Empowering Rift"]
        },
        "Voidwalker": {
            "Super": ["Vortex", "Cataclysm", "Nova Warp"],
            "Grenade":  ["Spike Grenade", "Vortex Grenade", "Voidwall Grenade", "Magnetic Grenade", "Suppressor Grenade", "Axion Bolt"],
            "Melee": ["Pocket Singularity"],
            "Class Ability": ["Healing Rift", "Empowering Rift"]
        },
        "Shadebinder":{
            "Super": ["Winter's Wrath"],
            "Grenade": ["Glacial Grenade", "Duskfield Grenade", "Coldsnap Grenade"],
            "Melee": ["Penumbral Blast"],
            "Class Ability": ["Healing Rift", "Empowering Rift"]
        },
        "Broodweaver":{
            "Super": ["Needlestorm"],
            "Grenade": ["Shackle Grenade", "Threadling Grenade", "Grapple Grenade"],
            "Melee": ["Arcane Needle"],
            "Class Ability": ["Healing Rift", "Empowering Rift"]
            
        }
    },
    "Titan": {
        "Striker": {
            "Super": ["Fists of Havoc", "Thundercrash"],
            "Grenade": ["Arcbolt Grenade", "Flux Grenade", "Skip Grenade", "Flashbang Grenade", "Lightning Grenade", "Pulse Grenade", "Storm Grenade"],
            "Melee": ["Seismic Strike", "Ballistic Slam", "Thunderclap"],
            "Class Ability": ["Towering Barricade", "Rally Barricade", "Thruster"]
        },
        "Sunbreaker": {
            "Super": ["Burning Maul", "Hammer of Sol"],
            "Grenade": ["Incendiary Grenade", "Swarm Grenade", "Tripmine Grenade", "Fusion Grenade", "Incendiary Grenade", "Thermite Grenade", "Firebolt Grenade", "Healing Grenade"],
            "Melee": ["Hammer Strike", "Throwing Hammer"],
            "Class Ability": ["Towering Barricade", "Rally Barricade"]
        },
        "Sentinel": {
            "Super": ["Sentinel Shield", "Ward of Dawn"],
            "Grenade":  ["Spike Grenade", "Vortex Grenade", "Voidwall Grenade", "Magnetic Grenade", "Suppressor Grenade", "Axion Bolt"],
            "Melee": ["Shield Bash", "Shield Throw"],
            "Class Ability": ["Towering Barricade", "Rally Barricade"]
        },
        "Behemoth":{
            "Super": ["Glacial Quake"],
            "Grenade": ["Glacial Grenade", "Duskfield Grenade", "Coldsnap Grenade"],
            "Melee": ["Shiver Strike"],
            "Class Ability": ["Towering Barricade", "Rally Barricade"]
        },
        "Berserker":{
            "Super": ["Bladefury"],
            "Grenade": ["Shackle Grenade", "Threadling Grenade", "Grapple Grenade"],
            "Melee": ["Frenzied Blades"],
            "Class Ability": ["Towering Barricade", "Rally Barricade"]
        }
    },
    "Hunter": {
        "Arcstrider": {
            "Super": ["Arc Staff", "Gathering Storm"],
            "Grenade": ["Arcbolt Grenade", "Flux Grenade", "Skip Grenade", "Flashbang Grenade", "Lightning Grenade", "Pulse Grenade", "Storm Grenade"],
            "Melee": ["Combination Blow", "Disorienting Blow"],
            "Class Ability": ["Marksman's Dodge", "Gambler's Dodge"],
        },
        "Gunslinger": {
            "Super": ["Deadshot", "Marksman", "Blade Barrage"],
            "Grenade": ["Incendiary Grenade", "Swarm Grenade", "Tripmine Grenade", "Fusion Grenade", "Incendiary Grenade", "Thermite Grenade", "Firebolt Grenade", "Healing Grenade"],
            "Melee": ["Knife Trick", "Lightweight Knife", "Weighted Throwing Knife", "Proximity Explosive Knife"],
            "Class Ability": ["Marksman's Dodge", "Gambler's Dodge", "Acrobat's Dodge"]
        },
        "Nightstalker": {
            "Super": ["Moebius Quiver", "Deadfall", "Spectral Blades"],
            "Grenade": ["Spike Grenade", "Vortex Grenade", "Voidwall Grenade", "Magnetic Grenade", "Suppressor Grenade", "Axion Bolt"],
            "Melee": ["Smoke Bomb"],
            "Class Ability": ["Marksman's Dodge", "Gambler's Dodge"]
        },
        "Revenant":{
            "Super": ["Silence and Squall"],
            "Grenade": ["Glacial Grenade", "Duskfield Grenade", "Coldsnap Grenade"],
            "Melee": ["Withering Blade"],
            "Class Ability": ["Marksman's Dodge", "Gambler's Dodge"]
        },
        "Threadrunner":{
            "Super": ["Silkstrike"],
            "Grenade": ["Shackle Grenade", "Threadling Grenade", "Grapple Grenade"],
            "Melee": ["Threaded Spike"],
            "Class Ability": ["Marksman's Dodge", "Gambler's Dodge"]
        }
    }
}
# st.set_page_config(layout="wide")

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = True

st.title("Random Subclass Generator")
choice = st.selectbox("Which Class?",
            ('Warlock','Titan','Hunter'))
            # label_visibility=st.session_state.visibility,
            # disabled=st.session_state.disabled,)

col1, col2, col3 = st.columns(3)
default = True
with col1:
    grenade_box = st.checkbox('Grenade', value=default)
with col2:
    melee_box = st.checkbox('Melee', value=default)
with col3:
    class_ability_box = st.checkbox('Class Ability', value=default)


if st.button('Randomize'):
    subclass_abilities = []
    class_selected = destiny_subclasses[str(choice)]
    subclass = random.choice(list(class_selected.keys()))
    if grenade_box:
        grenade = random.choice(class_selected[subclass]['Grenade'])
        subclass_abilities.append(grenade)
    if melee_box:
        melee = random.choice(class_selected[subclass]['Melee'])
        subclass_abilities.append(melee)
    if class_ability_box:
        class_ability = random.choice(class_selected[subclass]['Class Ability'])
        subclass_abilities.append(class_ability)

    # Images
    subclass_images = {
        'Stormcaller': 'images/warlock/Stormcaller.png',
        'Dawnblade': 'images/warlock/Dawnblade.png',
        'Voidwalker': 'images/warlock/Voidwalker.png',
        'Shadebinder': 'images/warlock/Shadebinder.png',
        'Broodweaver': 'images/warlock/Broodweaver.png',

        'Striker': 'images/titan/Striker.png',
        'Sunbreaker': 'images/titan/Sunbreaker.png',
        'Sentinel': 'images/titan/Sentinel.png',
        'Behemoth': 'images/titan/Behemoth.png',
        'Berserker': 'images/titan/Berserker.png',

        'Arcstrider': 'images/hunter/Arcstrider.png',
        'Gunslinger': 'images/hunter/Gunslinger.png',
        'Nightstalker': "images/hunter/Nightstalker.png",
        'Revenant': 'images/hunter/Revenant.png',
        'Threadrunner': 'images/hunter/Threadrunner.png'
    }
    # print(class_selected.keys())
    st.subheader(f"{subclass} | {' | '.join(subclass_abilities)}")
    if subclass in subclass_images:
        image_path = subclass_images[subclass]
        image = Image.open(image_path)
        st.image(image)