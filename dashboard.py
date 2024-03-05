import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


day_df = pd.read_csv("day.csv")


def main():
    st.title("Dashboard Analisis Pengguna Sepeda")


    option = st.sidebar.selectbox(
        "Pilih Analisis:",
        ("Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca",
         "Jumlah Pengguna Sepeda berdasarkan Hari Kerja, Hari Libur, dan Hari dalam Seminggu",
         "Jumlah total sepeda yang disewakan berdasarkan Bulan dan Tahun")
    )

    if option == "Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca":
        plot_weather_condition()

    elif option == "Jumlah Pengguna Sepeda berdasarkan Hari Kerja, Hari Libur, dan Hari dalam Seminggu":
        plot_working_holiday_weekday()

    elif option == "Jumlah total sepeda yang disewakan berdasarkan Bulan dan Tahun":
        plot_monthly_counts()



def plot_weather_condition():
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x='weathersit',
        y='cnt',
        data=day_df
    )
    plt.title('Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(plt.gcf())  # Use the current figure



def plot_working_holiday_weekday():
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(15, 10))


    sns.barplot(
        x='workingday',
        y='cnt',
        data=day_df,
        ax=axes[0]
    )
    axes[0].set_title('Jumlah Pengguna Sepeda berdasarkan Hari Kerja')
    axes[0].set_xlabel('Hari Kerja')
    axes[0].set_ylabel('Jumlah Pengguna Sepeda')


    sns.barplot(
        x='holiday',
        y='cnt',
        data=day_df,
        ax=axes[1]
    )
    axes[1].set_title('Jumlah Pengguna Sepeda berdasarkan Hari Libur')
    axes[1].set_xlabel('Hari Libur')
    axes[1].set_ylabel('Jumlah Pengguna Sepeda')

    sns.barplot(
        x='weekday',
        y='cnt',
        data=day_df,
        ax=axes[2]
    )
    axes[2].set_title('Jumlah Pengguna Sepeda berdasarkan Hari dalam Seminggu')
    axes[2].set_xlabel('Hari dalam Seminggu')
    axes[2].set_ylabel('Jumlah Pengguna Sepeda')

    plt.tight_layout()
    st.pyplot(plt.gcf()) 


def plot_monthly_counts():
    day_df['mnth'] = pd.Categorical(day_df['mnth'], categories=
    ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                                      ordered=True)

    monthly_counts = day_df.groupby(by=["mnth", "yr"]).agg({
        "cnt": "sum"
    }).reset_index()

    sns.lineplot(
        data=monthly_counts,
        x="mnth",
        y="cnt",
        hue="yr",
        palette="rocket",
        marker="o"
    )

    plt.title("Jumlah total sepeda yang disewakan berdasarkan Bulan dan tahun")
    plt.xlabel(None)
    plt.ylabel(None)
    plt.legend(title="Tahun", loc="upper right")
    plt.tight_layout()
    st.pyplot(plt.gcf())  



if __name__ == "__main__":
    main()
