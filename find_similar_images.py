#!/usr/bin/env python
#Searches a directory and finds duplicate images from a set of query images.
#Install imagehash with pip (python -m pip install imagehash)
#Adapted From https://github.com/JohannesBuchner/imagehash/blob/master/find_similar_images.py

from __future__ import (absolute_import, division, print_function)
from PIL import Image
from shutil import copyfile
import six
import sys, os

import imagehash

def is_image(filename):
    f = filename.lower()
    return f.endswith(".png") or f.endswith(".jpg") or \
        f.endswith(".jpeg") or f.endswith(".bmp") or \
        f.endswith(".gif") or '.jpg' in f or  f.endswith(".svg")

'''
Recursively searches a directory to find all the image files
@param (string) direc: The directory to be searched
@param ([string]) skip: The sub directory's that will not be searched
'''
def imagesInDir(direc, skip = []):
    imagePaths = []
    subDirs = [os.path.join(direc, path) for path in os.listdir(direc) if os.path.isdir(direc + '/' + path)]
    for subDir in subDirs:
#        print(subDir)
        if subDir in skip:
            continue
        imagePaths = imagePaths + imagesInDir(subDir)
    return imagePaths + [os.path.join(direc, path) for path in os.listdir(direc) if is_image(path)]

'''
Searches a directory recursively to see if said directory contains duplicate images(of varying sizes) of any image from a set of query images. Copies those images to a new directory.
@param (string) querydir: The directory of original images, which will be used as the queries to search for duplicates
@param (string) searchdir: The directory that will be searched in to find duplicate images
@param (string) outdir: The name of the directory that will contain the higher quality image copies
@param hashfunc: The hashing method. Options include
    imagehash.average_hash
    imagehash.phash
    imagehash.dhash
    imagehash.whash
    lambda img: imagehash.whash(img, mode='db4')
@Return: None
'''
def find_similar_images(querydir, searchdir, outdir, hashfunc = imagehash.average_hash):
    
    def createOutDir(direc):                
        subDirs = [os.path.join(direc, path) for path in os.listdir(direc) if os.path.isdir('./' + direc + '/' + path)]
        for subDir in subDirs:
            createOutDir(subDir)
            dirPath = './' + outdir + '/' + os.path.relpath(subDir, querydir)
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)

    if not os.path.exists(outdir):
        os.makedirs(outdir)
    createOutDir(querydir)

    #Returns the hash for an image, or False if there's a problem generating the hash
    def get_hash(img):
        try:
            return hashfunc(Image.open(img))
        except Exception as e:
            print('Problem:', e, 'with', img)
            return False

    #Finds the names of all image files that will be searched for duplicates, not the query images
    query_image_filenames = imagesInDir(querydir, ['./.git'])
    search_image_filenames = imagesInDir(searchdir, ['./.git', './' + querydir, './' + outdir])

    images = {} #The query images
    for img in query_image_filenames:
        hash = get_hash(img)
        if not hash: continue
        images[hash] = images.get(hash, []) + [img]

    for img in sorted(search_image_filenames):
        hash = get_hash(img)
        if not hash: continue
        if hash in images:
            print('Duplicate of ', images[hash], 'found at ', img)
            images[hash] = images.get(hash, []) + [img]
            cnt = 1
            cpyFileName = outdir + '/' +  os.path.relpath(images[hash][0], querydir)
            pth, extension = os.path.splitext(cpyFileName)
            while (os.path.exists(cpyFileName)):
                cnt += 1
                cpyFileName = pth + '_' + str(cnt) + extension
            copyfile(img, cpyFileName)



find_similar_images('QueryDir', '.', 'OutDir', imagehash.phash)
