import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class LocalBinaryPattern:

	def __init__(self, src_img, radius, pts):

		self.src_img = src_img
		self.radius = radius
		self.pts = pts
		self.gray_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
		self.out_img = np.zeros(self.gray_img.shape, dtype=(self.gray_img).dtype)
		self.Y, self.X = self.gray_img.shape[0], self.gray_img.shape[1]
		self.featureVector = np.zeros(256)
	
	# this method returns the LBP value
	def getLBPValue(self, cell, x, y):
		# the 8 neighbouring cells
		pos = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
		
		binStr = '' # a binary number storage string
		
		for i in range(len(pos)):
			if cell < self.gray_img[y + pos[i][0], x + pos[i][1]]:
				binStr += '1'
			else:
				binStr += '0'
				
		
		return int(binStr, 2)
	
	def makeHistogram(self):
		plt.hist(self.out_img)
		plt.show()

	def show(self):
		cv2.imshow('Source', self.src_img)
		cv2.imshow('Source Grayscale', self.gray_img)
		cv2.imshow('Output', self.out_img)

		print('X =', self.X, ':: Y =', self.Y)

		cv2.waitKey(0)
		cv2.destroyAllWindows()
		print('Feature Vector: ', self.featureVector)
		self.makeHistogram()

	def makeFeatureVector(self):
		for y in range(self.Y):
			for x in range(self.X):				
				# ignoring border elements for LBP calculation
				if x == 0 or x == self.X-1 or y == 0 or y == self.Y-1:
					self.out_img[y, x] = self.gray_img[y, x]
				else:
					self.out_img[y, x] = self.getLBPValue(self.gray_img[y, x], x, y)

		#making the feature vector
		for i in range(0,256):
			self.featureVector[i] = np.count_nonzero(self.out_img == i)

#-----------------------------------------------------------------		

def addTextureFeature(df_texture, img):	
	Img = LocalBinaryPattern(img, 1, 8)
	Img.makeFeatureVector()

	df_texture = df_texture.append(pd.Series(Img.featureVector), ignore_index=True)

	return df_texture

df_texture = pd.DataFrame(columns=list(range(0, 256))) # initializing dataframe

while True:
	img_path = input('Enter image path(respective to current directory and exact image format): ')
	img = cv2.imread(img_path)
	try:
		df_texture = addTextureFeature(df_texture, img)
	except Exception as e:
		print(e)

	choice = input('Enter another?(Y/N): ')
	if choice[0] == 'Y':
		continue
	else:
		break

print(df_texture)