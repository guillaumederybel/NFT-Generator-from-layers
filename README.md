# NFT-Generator-from-layers
 This repo permits you to create an NFT from various layers you have chosen. You can custom the apparition rate of a layer, or of a layer entity.

1. Install requirements

> pip install -r requirements


2. Create layers folders

It is important to create a folder for each layer you will use.

> e.g. : /background/, /head/, ...


3. Start program

> python3 nftgenerator.py

> Choose how many NFTs you would like to generate (default is 1)

> Choose the number of layers you will use

For each layer,

> Indicate the layer folder (e.g. : background, head, ...)

The program will now list all image files (png, jpg, jpeg) present in the layer folder, we will call them 'entities'.

For each entity,

> Indicate the probability for this entity to appear (in %)

If the sum of all probabilities is under 100, the program will ask you if you want to replace the rest by nothing.

For example :

> Wich percentage should brown_eyes.png appear ? (default : 33.3333336 %): 10

> Wich percentage should blue_eyes.png appear ? (default : 33.3333336 %): 20

> Wich percentage should green_eyes.png appear ? (default : 33.3333336 %): 20

The total percentage is 50, so the program will ask :

> The Sum of probabilities isn't equal to 100%, should I replace the missing percentage by nothing ? (y/n) (default : y): y

This corresponds to the chance for a layer to appear, instead of pasting an eye image, it will paste a blank image.

Here, I want to set the layer apparition chance to 1/2 (50%).


Important : The order of the chosen layers is important. The last layer will be pasted on the before last, so it might hide something.