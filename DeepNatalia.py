
# coding: utf-8

import pandas as pd
import numpy as np
from sklearn import linear_model
import seaborn
from datetime import datetime
from matplotlib import pyplot as plt
from scipy import stats
from scipy.stats import mstats
from scipy.stats import pearsonr
from scipy.stats import norm
#get_ipython().magic(u'matplotlib inline')

BUCKET_NAME = 'bucket_name'
AWS_ACCESS_KEY_ID = ...
AWS_SECRET_ACCESS_KEY = ...

class DeepNatalia(object):
	def __init__(self):
		print "Natalia's Deep Learning utils"



	def push_picture_to_s3(id):
	  try:
	    import boto
	    from boto.s3.key import Key
	    # set boto lib debug to critical
	    logging.getLogger('boto').setLevel(logging.CRITICAL)
	    bucket_name = settings.BUCKET_NAME
	    # connect to the bucket
	    conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID,
	                    settings.AWS_SECRET_ACCESS_KEY)
	    bucket = conn.get_bucket(bucket_name)
	    # go through each version of the file
	    key = '%s.png' % id
	    fn = '/var/www/data/%s.png' % id
	    # create a key to keep track of our file in the storage
	    k = Key(bucket)
	    k.key = key
	    k.set_contents_from_filename(fn)
	    # we need to make it public so it can be accessed publicly
	    # using a URL like http://s3.amazonaws.com/bucket_name/key
	    k.make_public()
	    # remove the file from the web server
	    os.remove(fn)
	  except:

	def download_from_S3(LOCAL_PATH, bucket_name):
		#As you saw, you can access the file using the URL: http://s3.amazonaws.com/bucket_name/key but you can also use the boto library to download the files. I do that to create a daily backup of the bucket’s files on my local machine.
		import boto
		import sys, os
		from boto.s3.key import Key

		#LOCAL_PATH = '/backup/s3/'
		# connect to the bucket
		conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
		bucket = conn.get_bucket(bucket_name)
		# go through the list of files
		bucket_list = bucket.list()
		for l in bucket_list:
		  keyString = str(l.key)
		  # check if file exists locally, if not: download it
		  if not os.path.exists(LOCAL_PATH+keyString):
		    l.get_contents_to_filename(LOCAL_PATH+keyString)

	def test_library_path_issues():
	    import os, sys
	    os.getcwd()
	    print sys.path
	    #sys.path.append('')
	    from jupyter_core.paths import jupyter_data_dir
	    print(jupyter_data_dir())
	    print "exec ",sys.executable
	    import numpy
	    numpy.get_include()
	    import keras
	    keras.get_include()
	    # in notebook:
		sys.path.append('~/tensorflow/lib/python2.7/site-packages/Keras-1.1.1-py2.7.egg/keras/')

	    #export PATH=~/tensorflow/lib/python2.7/site-packages/Keras-1.1.1-py2.7.egg/keras/:$PATH
		#export PYTHONPATH='/miniconda2/lib/python2.7/site-packages/theano'
		#sys.path.append('/miniconda2/lib/python2.7/site-packages/theano')
		import theano
		theano.test()
		# Obviously theano doesn't seem to be in the search path of your Python installation.
		# Check out sys.path and verify that the module is located in one of the listed locations

		

test_library_path_issues()
