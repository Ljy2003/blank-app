import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.header('睡眠状况分析', divider='rainbow')

stages = 4-pd.read_csv('./data/stage1.csv').to_numpy()[:,0]
stage = ['Wake','REM','N1','N2','N3']


fig = plt.figure(figsize=[10,5])
ax = fig.add_subplot(1,1,1)
ax.plot(stages)
st.markdown('## 睡眠分期结果')
ax.set_yticks([4,3,2,1,0],stage)
st.pyplot(fig)

col1,col2 = st.columns(2)
with col1:
    fig = plt.figure(figsize=[5,5])
    ax = fig.add_subplot(1,1,1)
    ax.pie([np.sum(stages==4),np.sum(stages==3),np.sum(stages==2),np.sum(stages==1),np.sum(stages==0)],labels=stage)
    st.markdown('## 睡眠阶段占比')
    st.pyplot(fig)
with col2:
    st.markdown('### 觉醒次数：4')
    st.markdown('### 睡眠质量分数：86')
    st.markdown('### 睡眠潜伏期：20分钟')
    st.markdown('### REM潜伏期：{}分钟'.format(np.where(stages==3)[0][0]/2))
st.markdown("## 睡眠建议")
st.markdown('''
- ### 中途觉醒次数过多，注意睡前不要饮酒或喝咖啡。
- ### REM潜伏期过长，需要减少白天酒精摄入量。
- ### 深度睡眠时间较少，平时加强锻炼，控制体重。
''')
