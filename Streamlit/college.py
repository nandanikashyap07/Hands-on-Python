import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import numpy as np

def make_data():
    rng = pd.date_range('2023-01-01', '2023-12-31', freq='D')
    names = ["Aarav", "Vivaan", "Aditya", "Vihaan", "Ishaan",
             "Kritika", "Ananya", "Nandini", "Riya", "Sanya"]
    rows = []

    for name in names:
        base = np.random.randint(60, 90)
        for d in rng:
            att = np.random.choice(["Present", "Absent"], p=[0.88, 0.12])
            perf = base + np.random.randint(-15, 15)
            perf = max(0, min(perf, 100))
            rows.append([d, name, att, perf])

    return pd.DataFrame(rows, columns=["Date", "Student", "Attendance", "Performance"])

df = make_data()

st.set_page_config(page_title="Smart Attendance & Performance Dashboard", layout="wide")
st.title("Smart Attendance & Performance Dashboard")

st.sidebar.header("Filters")

picked_student = st.sidebar.selectbox("Select Student", df["Student"].unique())
d1 = st.sidebar.date_input("Start Date", df["Date"].min())
d2 = st.sidebar.date_input("End Date", df["Date"].max())
att_sel = st.sidebar.multiselect("Attendance Filter", ["Present", "Absent"], ["Present", "Absent"])

part = df[
    (df["Student"] == picked_student) &
    (df["Date"] >= pd.to_datetime(d1)) &
    (df["Date"] <= pd.to_datetime(d2)) &
    (df["Attendance"].isin(att_sel))
]

c1, c2, c3, c4 = st.columns(4)

count_all = len(part)
count_present = len(part[part["Attendance"] == "Present"])
att_pct = (count_present / count_all * 100) if count_all else 0
avg_score = part["Performance"].mean()
hi = part["Performance"].max() if count_all else 0
lo = part["Performance"].min() if count_all else 0

c1.metric("Attendance Rate", f"{att_pct:.1f}%")
c2.metric("Average Score", f"{avg_score:.1f}")
c3.metric("Best Score", hi)
c4.metric("Lowest Score", lo)

att_cnt = part.groupby("Attendance").size().reset_index(name="Count")
pie = px.pie(att_cnt, names="Attendance", values="Count", title="Attendance Distribution", hole=0.4)
st.plotly_chart(pie, use_container_width=True)

line_perf = px.line(part, x="Date", y="Performance", title="Performance Progress Over Time", markers=True)
st.plotly_chart(line_perf, use_container_width=True)

st.subheader("Monthly Performance Heatmap")

tmp = part.copy()
tmp["Month"] = tmp["Date"].dt.strftime("%b")
m_avg = tmp.groupby("Month")["Performance"].mean().reset_index()

bar_m = px.bar(m_avg, x="Month", y="Performance", title="Average Performance per Month", text="Performance")
st.plotly_chart(bar_m, use_container_width=True)

st.subheader("Weekly Attendance Trend")

tmp2 = part.copy()
tmp2["Week"] = tmp2["Date"].dt.isocalendar().week
wk = tmp2.groupby("Week")["Attendance"].apply(lambda x: (x == "Present").mean() * 100).reset_index(name="Attendance %")

line_w = px.line(wk, x="Week", y="Attendance %", title="Weekly Attendance Percentage", markers=True)
st.plotly_chart(line_w, use_container_width=True)

st.subheader("Detailed Student Activity Log")
st.dataframe(part)
