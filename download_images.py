import requests
import os
import re

# Create assets directory if it doesn't exist
os.makedirs('assets', exist_ok=True)

# Character data from the HTML file
characters = [
    {'name': 'Mario', 'image': 'https://mario.wiki.gallery/images/a/af/MvDK_NS_Mario.png'},
    {'name': 'Luigi', 'image': 'https://mario.wiki.gallery/images/7/76/SMPJ_Luigi.png'},
    {'name': 'Princess Peach', 'image': 'https://mario.wiki.gallery/images/7/7c/Peach_Posing_Alt_3D_Artwork.png'},
    {'name': 'Bowser', 'image': 'https://mario.wiki.gallery/images/c/c7/SMBW_Artwork_Bowser.png'},
    {'name': 'Yoshi', 'image': 'https://mario.wiki.gallery/images/5/5f/SMPJ_Yoshi.png'},
    {'name': 'Toad', 'image': 'https://mario.wiki.gallery/images/8/89/MPS_Toad_Artwork.png'},
    {'name': 'Donkey Kong', 'image': 'https://mario.wiki.gallery/images/8/84/MPS_Donkey_Kong_Artwork.png'},
    {'name': 'Diddy Kong', 'image': 'https://mario.wiki.gallery/images/6/64/MK8D_BCP_Diddy_Kong_Artwork.png'},
    {'name': 'Wario', 'image': 'https://mario.wiki.gallery/images/2/29/SMPWario.png'},
    {'name': 'Waluigi', 'image': 'https://mario.wiki.gallery/images/2/27/SuperMarioParty_Waluigi.png'},
    {'name': 'Rosalina', 'image': 'https://mario.wiki.gallery/images/5/56/Rosalina-MPTop100-Transparent.png'},
    {'name': 'Daisy', 'image': 'https://mario.wiki.gallery/images/b/b5/Daisy_Render_MP6_2.png'},
    {'name': 'Bowser Jr.', 'image': 'https://mario.wiki.gallery/images/f/f5/SMBW_Bowser_Jr_Artwork_1.png'},
    {'name': 'Koopa Troopa', 'image': 'https://mario.wiki.gallery/images/5/5c/SuperMarioParty_KoopaTroopa.png'},
    {'name': 'Shy Guy', 'image': 'https://mario.wiki.gallery/images/b/b2/MPS_Shy_Guy_Artwork.png'},
    {'name': 'Boo', 'image': 'https://mario.wiki.gallery/images/3/3f/MPS_Boo_Artwork.png'},
    {'name': 'Dry Bones', 'image': 'https://mario.wiki.gallery/images/3/33/MPSR_Dry_Bones.png'},
    {'name': 'Birdo', 'image': 'https://mario.wiki.gallery/images/e/ed/MP9_Birdo_Main_Artwork.png'},
    {'name': 'Kamek', 'image': 'https://mario.wiki.gallery/images/3/3c/SMPJ_Kamek_Artwork.png'},
    {'name': 'Lakitu', 'image': 'https://mario.wiki.gallery/images/8/87/NSMBU_Lakitu_Artwork.png'},
    {'name': 'Piranha Plant', 'image': 'https://mario.wiki.gallery/images/d/d1/NSMBU_Piranha_Plant_in_Pipe_Artwork.png'},
]

def sanitize_filename(name):
    # Remove special characters and replace spaces with underscores
    return re.sub(r'[^\w\s-]', '', name).strip().replace(' ', '_').lower()

def download_image(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Successfully downloaded: {filename}")
        return True
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")
        return False

# Download all images
for character in characters:
    filename = f"assets/{sanitize_filename(character['name'])}.png"
    download_image(character['image'], filename) 