from turtle import home
import streamlit as s
import pandas

s.set_page_config(layout="wide")


col1 ,col2 =s.columns(2)

with col1:
    s.image("images/photo.jpg",width=400)

with col2:
    s.title("Vishal S")
    content="""
        hi there,I am Vishal S ! I am a computer science student at CIT from coimbatore.I am an active programmer like to work with python,java,c,c++,JavaScript,R,Web development and Django.
        \n Currently working with Python to upskill in the Field of Artificial Intelligence and Machine Learning (AI & ML).
        \n This Page is used to link the source code of the projects,I developed so far and going to do the in upcoming future as well.
        \n Happy coding coders !
    """
    s.info(content)

s.subheader("Here with attached the projects i have worked along with their Source links below:")

col3,mar_col,col4 =s.columns([1.5,0.5,1.5])

df=pandas.read_csv("data.csv",sep=",")


toggle = True

for index,row in df.iterrows():

    if toggle:

        with col3:
            s.header(row["title"])
            s.write(row["description"])
            s.image(f'images/{row["image"]}',width=400)
            s.write(f"[Source code]({row['url']})")
            s.write('---')


    else:

        with col4:
            s.header(row["title"])
            s.write(row["description"])
            s.image(f'images/{row["image"]}',width=400)
            s.write(f"[Source code](rows['url'])")
            s.write('---')

    toggle = not toggle




