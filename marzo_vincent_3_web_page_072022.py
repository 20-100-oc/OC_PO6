import os
from matplotlib import pyplot as plt
import streamlit as st
from PIL import Image
import pandas as pd
import pyLDAvis
import pickle



root_dir = 'D:/OpenClassrooms/projet_6'
imgs_path = root_dir + '/image_projet_6/'



st.title('Customer Reviews')

st.subheader('LDA')

st.write('After processing, determine best number of topics (here it is 4):')
img_path = imgs_path + 'elbow_lda' + '.png'
st.image(Image.open(img_path), caption='elbow graph of LDA')

# pyLDAvis
st.write('Visualisation of predicted groups:')

lda_filename = f'LDAvis_k_4_n_50000'
lda_save_path = root_dir + '/data/lda_vis/' + lda_filename
with open(lda_save_path, 'rb') as f:
    LDAvis = pickle.load(f)
html_string = pyLDAvis.prepared_data_to_html(LDAvis)
from streamlit import components
components.v1.html(html_string, width=1300, height=800, scrolling=True)

st.write('Put LDA results in tsne to see if there is a clear separation between topics:')
img_path = imgs_path + 'tsne_lda' + '.png'
st.image(Image.open(img_path), caption='tsne of LDA')


st.subheader('NMF')
st.write('Same process as with LDA\n(Optimal number of topics is also 4):')

st.write('')
img_path = imgs_path + 'elbow_nmf' + '.png'
st.image(Image.open(img_path), caption='elbow graph of NMF')

st.write('')
img_path = imgs_path + 'tsne_nmf' + '.png'
st.image(Image.open(img_path), caption='tsne of NMF')



st.title('Customer Photos')


st.write('Exemple image:')
img_path = imgs_path + 'test_image_original' + '.png'
st.image(Image.open(img_path), caption='original image')


st.subheader('SIFT')

st.write('Exemple image after preprocessing from SIFT:')
img_path = imgs_path + 'test_image_sift' + '.png'
st.image(Image.open(img_path), caption='preprocessed image with SIFT')

st.write('tsne on SIFT features (colored with true labels):')
img_path = imgs_path + 'tsne_sift_true' + '.png'
st.image(Image.open(img_path), caption='tsne SIFT')
st.write('Resulting groups are not clearly separated, so another method is tried.')


st.subheader('VGG16')

st.write('Exemple image after preprocessing from VGG16:')
img_path = imgs_path + 'test_image_vgg16' + '.png'
st.image(Image.open(img_path), caption='preprocessed image with VGG16')

st.write('tsne on VGG16 features (colored with true labels):')
img_path = imgs_path + 'tsne_vgg16_true' + '.png'
st.image(Image.open(img_path), caption='tsne VGG16 with true labels')
st.write('LABELS:')
st.write('0 : inside')
st.write('1 : outside')
st.write('2 : drink')
st.write('3 : food')
st.write('4 : menu')

st.write(' ')
st.write('Resulting groups are much clearer.')
st.write('However, the predictions are not perfect:')
img_path = imgs_path + 'tsne_vgg16_pred' + '.png'
st.image(Image.open(img_path), caption='tsne VGG16 with predictions')
