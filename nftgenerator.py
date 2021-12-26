import os
import numpy as np
from PIL import Image

class layer:

    def __init__(self, image_path):
        self.image_path = image_path

    def list_entities(image_path):
        files = [file for file in os.listdir(image_path) if file.endswith('.png')]
        count = 0
        for file in files:
            count+=1
        default_rarity = 100/count
        entities = []
        for file in files:
            rarity = input('Wich percentage should ' + file + ' appear ? (default : ' + str(default_rarity) + ' %): ')
            if rarity == '':
                rarity = default_rarity
            rarity = float(rarity)/100
            entities.append([file, float(rarity)])
        return entities

    def choose_entity(list, nft_count):
        entities = []
        probabilties = []        
        for element in list:
            entities.append(element[0])
            probabilties.append(element[1])
        if round(sum(probabilties), 4) < 1:
            mod = input('The Sum of probabilities isn\'t equal to 100%, should we replace the missing percentage by nothing ? (y/n) (default : y): ')
            if mod == 'y' or mod == 'Y' or mod == '':
                blank = 1 - sum(probabilties)
                probabilties.append(blank)
                entities.append('')
            else:
                exit()
        if round(sum(probabilties), 4) > 1:
            print('The total percentage might be equal to 100%.')
            exit()
        choices = np.random.choice(entities, nft_count, p=probabilties)
        return choices

    def create_nft_list(array):
        i=0
        y=0
        temp_list = []
        nfts = []
        while i<len(array[0]):
            for list in array:
                temp_list.append(Image.open(list[y]))
            nfts.append(temp_list)
            temp_list = []
            y+=1
            i+=1
        return nfts

    def edit_and_save(nfts):
        save_dir = input('\nWhere should I save the generated NFTs ? (default : Generated_NFTs) : ')

        if save_dir == "":
            save_dir = "Generated_NFTs"

        if not os.path.isdir(save_dir):
            try:
                os.mkdir(save_dir)
            except:
                print('Couldn\'t create a folder to save NFTs. Please create one by yourself.')
                exit()

        print('\nCreating NFTs... This might take few seconds (it depends of the volume generated).\n')

        id = 1
        for nft in nfts:
            i=0
            while i<len(nft):
                nft[0].paste(nft[i], nft[i])
                i+=1
            nft[0].save(save_dir + '/nft#'+str(id)+'.png', quality=100)
            id+=1
  
i=0

nft_count = input('How many NFT would you like to generate ? (default : 1) : ')
if nft_count == '':
    nft_count = '1'
try:
    nft_count = int(nft_count)
except:
    print('The entered value is not a valid number.')
    exit()

layers_count = input('How many layers should we have ? : ')
try:
    layers_count = int(layers_count)
except:
    print('The entered value is not a valid number.')
    exit()

array_full = []
while i < layers_count:
    folder = input('Layer ' + str(i+1) + ' , wich folder should I look for this layer items ? : ')
    if os.path.isdir(folder):
        choices = layer.choose_entity(layer.list_entities(layer(folder).image_path),nft_count)
        id = 1
        current_nft_list = []
        for choice in choices:
            if choice != '':
                current_nft_list.append(folder + '/' + choice)
                id+=1
            else:
                current_nft_list.append('void.png')
        array_full.append(current_nft_list)
    else:
        print(folder + ' doesn\'t exists.')
        exit()
    i+=1

layer.edit_and_save(layer.create_nft_list(array_full))