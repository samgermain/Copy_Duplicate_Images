# Copy_Duplicate_Images
Python script which recursively searches a directory, finds duplicate images from a set of query images and copies those images to an output folder
Can be used to find higher quality versions of images
Adapted From https://github.com/JohannesBuchner/imagehash/blob/master/find_similar_images.py

Once you download the repository, you must install imagehash with pip 
     
     python -m pip install imagehash

Call the function find_similar_images_like

     find_similar_images('QueryDir', '.', 'OutDir', imagehash.phash)
     
I placed that function call at the bottom of the find_similar_images.py file, you can then run the program with 

     python3 ./find_similar_images.py
     
-----------------------------------------------------------------

I would love if someone added functionality to give the option to only copy the highest quality duplicate to the output directory
