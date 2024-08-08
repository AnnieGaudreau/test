import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def upload_and_read_excel(label):
    uploaded_file = st.file_uploader(label)
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write(df.head())
        return df
    return None

# Celtics Regular Season Player Stats
st.header("Celtics Regular Season Player Stats")
file1 = upload_and_read_excel("Upload Celtics Regular Season Player Stats (Celt_Reg_P_Stats.xlsx)")
if file1 is not None:
    st.write(file1.head(19))

# Team Stats
st.header("Team Stats")
file2 = upload_and_read_excel("Upload Team Stats (Team_Stats.xlsx)")
if file2 is not None:
    st.write(file2.head())

# Worst and Best Game Performances
st.header("Team’s Performance in Worst vs Best Regular Season Game")
file3a = upload_and_read_excel("Upload Worst Game Stats (CvsB.xlsx)")
file3b = upload_and_read_excel("Upload Best Game Stats (CvsW.xlsx)")
if file3a is not None and file3b is not None:
    st.write("Worst Game Stats:")
    st.write(file3a.head(2))
    st.write("Best Game Stats:")
    st.write(file3b.head(2))

# NBA All Player Stats
st.header("NBA All Player Stats")
file4 = upload_and_read_excel("Upload NBA All Player Stats (NBA_All_Stats.xlsx)")
if file4 is not None:
    st.write(file4.head(2))

# Thunder Team Stats
st.header("Thunder Team Stats")
file5 = upload_and_read_excel("Upload Thunder Team Stats (Thndr.xlsx)")
if file5 is not None:
    st.write(file5.head())

# Minutes Played vs Points Made
st.header("Minutes Played vs Points Made")
if file1 is not None:
    minutes = file1[['MP', 'PTS']]
    st.write(minutes.head(19))
    
    plt.figure(figsize=(10, 6))
    plt.scatter(file1['MP'], file1['PTS'], alpha=0.6, color='g', edgecolor='k', linewidth=0.5)
    plt.title('Minutes Played Versus Points Made')
    plt.xlabel('Minutes Played')
    plt.ylabel('Number of Points')
    plt.grid(True)
    st.pyplot(plt)

# Celtics vs Opponents Stats
st.header("Celtics vs Opponents Stats")
if file2 is not None:
    file2_cleaned = file2.drop([1,2,3,5,6,7],axis=0)
    f2_melted = pd.melt(file2_cleaned, id_vars=['Unnamed: 0'], value_vars=['FG', '3P', '2P', 'AST', 'FT', 'ORB', 'DRB', 'TOV', 'PTS'],
                        var_name='Variable', value_name='Value')
    st.write(f2_melted.head(36))
    
    palette = sns.color_palette('YlGn')
    sns.set_palette(palette)
    sns.catplot(data=f2_melted, x='Variable', y='Value', hue='Unnamed: 0', kind='bar', height=6, aspect=2)
    plt.xlabel('Stats')
    plt.ylabel('Value')
    plt.title('Eastern vs Opponents: Stats')
    st.pyplot(plt.gcf())

# Eastern vs Western Seed 1
st.header("Eastern vs Western Seed 1")
file6 = upload_and_read_excel("Upload Eastern vs Western Seed 1 Stats (EvW_S1.xlsx)")
if file6 is not None:
    f6_melted = pd.melt(file6, id_vars=['Team'], value_vars=['FG', '3P', '2P', 'AST', 'FT', 'ORB', 'DRB', 'TOV', 'PTS'],
                        var_name='Variable', value_name='Value')
    st.write(f6_melted.head(36))
    
    palette = sns.color_palette('YlGn')
    sns.set_palette(palette)
    sns.catplot(data=f6_melted, x='Variable', y='Value', hue='Team', kind='bar', height=6, aspect=2)
    plt.xlabel('Stats')
    plt.ylabel('Value')
    plt.title('Eastern vs Western Seed 1: Stats')
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())
