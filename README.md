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

Right now, if you use a cropped image, and try to find the original, this repo will not work. You need to add the `crop_resistant_hashref` in order for this to work

> There is crop_resistant_hashref now, which I think addresses this. If still an issue, please reopen.

* Originally posted by @JohannesBuchner in https://github.com/JohannesBuchner/imagehash/issues/107#issuecomment-880626547_

-----------------------------------------------------------------

I would also love if someone added functionality to give the option to only copy the highest quality duplicate to the output directory
