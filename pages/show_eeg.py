import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.header('睡眠脑电分析', divider='rainbow')
file = st.file_uploader('请上传EEG文件',type=['edf'])

if file is not None:
    channel_name = ['EEG Fpz-Cz', 'EEG Pz-Oz']
    raw = np.load('data/eeg.npy')
    x0,x1 = raw[:3000,0],raw[:3000,1]
    x0,x1 = (x0-x0.mean())/x0.std(),(x1-x1.mean())/x1.std()
    fig = plt.figure()
    t = np.linspace(0,30,3000)
    ax0 = fig.add_subplot(2,1,1)
    ax0.plot(t,x0,'r',linewidth=0.3)
    ax0.plot(t,x1+5,'b',linewidth=0.3)
    ax0.set_yticks([0,5],['Fpz-Cz', 'Pz-Oz'])
    ax1 = fig.add_subplot(2,1,2)
    ax1.bar(['Delta','Theta','Alpha','Sigma','Beta'],[0.4,0.5,0.7,0.78,0.77])

    st.pyplot(fig)
