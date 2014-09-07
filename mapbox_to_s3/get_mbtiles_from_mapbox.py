import os
import urllib
import logging
logging.basicConfig(level=logging.INFO)

import requests
import yaml

tilesets = ['building_areas', 'new_violations', 'construction-spending', 'new_const_permits']
access_token = yaml.load(open('credentials.yml').read())['access_token'] 
mbtiles_dir = 'mbtiles/'

def get_mbtiles_url(tileset):
    'Return mbtiles download URL for tileset from Mapbox API TileJSON endpoint.'
    url = 'https://api.tiles.mapbox.com/v4/jpvelez.%s.json?access_token=%s' % (tileset, access_token)
    response = requests.get(url)
    mbtiles_url = response.json()['download']
    return mbtiles_url

def download_mbtiles(mbtiles_url):
    'Download mbtiles from Mapbox for tileset.'
    # Create mbtiles output directory.
    if not os.path.exists(mbtiles_dir):
        os.makedirs(mbtiles_dir)

    # Save response stream to disk.
    # Useful for downloading large files.
    with open(mbtiles_dir + tileset + '.mbtiles', 'w') as output_file:
        stream = requests.get(mbtiles_url, stream=True)
        for block in stream.iter_content(1024):
            if not block:
                logging.warn('Could not download part of %s tileset!' % tileset) 
            output_file.write(block)

if __name__ == '__main__':
    for tileset in tilesets:
        mbtiles_url = get_mbtiles_url(tileset)
        logging.info('Saving %s to %s' % (tileset + '.mbtiles', mbtiles_dir))
        download_mbtiles(mbtiles_url)

