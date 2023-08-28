import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


def main():
    st.title("Matplotlib in Streamlit")

    # データの生成
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # プロットの作成
    fig, ax = plt.subplots()
    ax.plot(x, y, label='sin(x)')
    ax.set_title("A simple plot")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()

    # Streamlit にプロットを表示
    st.pyplot(fig)


if __name__ == "__main__":
    main()