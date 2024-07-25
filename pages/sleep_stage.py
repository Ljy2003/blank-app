import streamlit as st
import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.header('睡眠分期', divider='rainbow')
if st.button('运行睡眠分期模型',use_container_width=True):
    stage = ['Wake','REM','N1','N2','N3']
    bar=st.progress(0)
    a = st.markdown('正在运行脉冲神经网络，请稍后')
    for i in range(100):
        time.sleep(0.03)
        bar.progress(i)
    bar=st.progress(0)
    a.markdown('完成')
    time.sleep(0.2)
    a = st.markdown('正在运行睡眠分期模型，请稍后')
    for i in range(100):
        time.sleep(0.07)
        bar.progress(i)
    a.markdown('分期完成')
    fig = plt.figure(figsize=[10,5])
    ax = fig.add_subplot(1,1,1)
    stages = 4-pd.read_csv('./data/stage1.csv').to_numpy()[:,0]
    ax.plot(stages)
    ax.set_yticks([4,3,2,1,0],stage)
    st.markdown('## 睡眠分期结果')
    st.pyplot(fig)
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.pie([np.sum(stages==4),np.sum(stages==3),np.sum(stages==2),np.sum(stages==1),np.sum(stages==0)],labels=stage)
    st.markdown('## 睡眠阶段占比')
    st.pyplot(fig)
    