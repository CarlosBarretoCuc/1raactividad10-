import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="University Student Dashboard",
    page_icon="🎓",
    layout="wide",
)

# ── Team members ─────────────────────────────────────────────────────────────
TEAM_MEMBERS = ["Team Member 1", "Team Member 2", "Team Member 3", "Team Member 4"]

# ── Load data ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    import io
    raw = """Year,Term,Applications,Admitted,Enrolled,Retention Rate (%),Student Satisfaction (%),Engineering Enrolled,Business Enrolled,Arts Enrolled,Science Enrolled
2015,Spring,2500,1500,600,85,78,200,150,125,125
2015,Fall,2500,1500,600,85,78,200,150,125,125
2016,Spring,2600,1550,625,86,79,210,160,130,125
2016,Fall,2600,1550,625,86,79,210,160,130,125
2017,Spring,2700,1600,650,87,80,225,165,135,125
2017,Fall,2700,1600,650,87,80,225,165,135,125
2018,Spring,2800,1650,675,86,82,235,175,140,125
2018,Fall,2800,1650,675,86,82,235,175,140,125
2019,Spring,3000,1750,700,88,83,250,185,145,120
2019,Fall,3000,1750,700,88,83,250,185,145,120
2020,Spring,2900,1700,690,85,81,240,180,140,130
2020,Fall,2900,1700,690,85,81,240,180,140,130
2021,Spring,3100,1800,725,87,84,260,195,150,120
2021,Fall,3100,1800,725,87,84,260,195,150,120
2022,Spring,3250,1900,750,88,85,275,200,160,115
2022,Fall,3250,1900,750,88,85,275,200,160,115
2023,Spring,3350,2000,775,89,86,285,210,165,115
2023,Fall,3350,2000,775,89,86,285,210,165,115
2024,Spring,3500,2100,800,90,88,300,225,175,100
2024,Fall,3500,2100,800,90,88,300,225,175,100"""
    return pd.read_csv(io.StringIO(raw))

df = load_data()

# ── Sidebar filters ───────────────────────────────────────────────────────────
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/University_logo_placeholder.png/120px-University_logo_placeholder.png", width=80)
st.sidebar.title("🎓 Filters")

years = sorted(df["Year"].unique())
selected_years = st.sidebar.multiselect("Academic Year", years, default=years)

terms = df["Term"].unique().tolist()
selected_terms = st.sidebar.multiselect("Term", terms, default=terms)

departments = ["Engineering", "Business", "Arts", "Science"]
selected_depts = st.sidebar.multiselect("Department", departments, default=departments)

st.sidebar.markdown("---")
st.sidebar.markdown("**Team members:**")
for m in TEAM_MEMBERS:
    st.sidebar.markdown(f"- {m}")

# ── Filter dataframe ──────────────────────────────────────────────────────────
filtered = df[df["Year"].isin(selected_years) & df["Term"].isin(selected_terms)]

if filtered.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

# ── Title ─────────────────────────────────────────────────────────────────────
st.title("🎓 University Student Analytics Dashboard")
st.markdown("*Data Mining · Universidad de la Costa · Department of Computer Science and Electronics*")
st.markdown("---")

# ── KPI Cards ─────────────────────────────────────────────────────────────────
k1, k2, k3, k4 = st.columns(4)

avg_retention   = filtered["Retention Rate (%)"].mean()
avg_satisfaction = filtered["Student Satisfaction (%)"].mean()
total_enrolled  = filtered["Enrolled"].sum()
total_apps      = filtered["Applications"].sum()
admission_rate  = (filtered["Admitted"].sum() / total_apps * 100) if total_apps else 0

k1.metric("📈 Avg. Retention Rate",    f"{avg_retention:.1f}%")
k2.metric("😊 Avg. Satisfaction",      f"{avg_satisfaction:.1f}%")
k3.metric("🎓 Total Enrolled",         f"{total_enrolled:,}")
k4.metric("📋 Admission Rate",         f"{admission_rate:.1f}%")

st.markdown("---")

# ── Row 1: Line charts ────────────────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("📉 Retention Rate Trend Over Time")
    ret = filtered.groupby("Year")["Retention Rate (%)"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(6, 3.5))
    sns.lineplot(data=ret, x="Year", y="Retention Rate (%)", marker="o", color="#2196F3", ax=ax)
    ax.set_ylim(80, 95)
    ax.fill_between(ret["Year"], ret["Retention Rate (%)"], alpha=0.1, color="#2196F3")
    ax.set_xlabel("Year"); ax.set_ylabel("Retention Rate (%)")
    ax.set_title("Average Retention Rate by Year")
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

with col2:
    st.subheader("😊 Student Satisfaction Scores by Year")
    sat = filtered.groupby("Year")["Student Satisfaction (%)"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(6, 3.5))
    sns.lineplot(data=sat, x="Year", y="Student Satisfaction (%)", marker="s", color="#4CAF50", ax=ax)
    ax.set_ylim(70, 95)
    ax.fill_between(sat["Year"], sat["Student Satisfaction (%)"], alpha=0.1, color="#4CAF50")
    ax.set_xlabel("Year"); ax.set_ylabel("Satisfaction (%)")
    ax.set_title("Average Student Satisfaction by Year")
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

# ── Row 2: Bar chart + Pie chart ─────────────────────────────────────────────
col3, col4 = st.columns(2)

with col3:
    st.subheader("🌿 Spring vs Fall Comparison")
    term_data = filtered.groupby("Term")[["Enrolled", "Retention Rate (%)", "Student Satisfaction (%)"]].mean().reset_index()
    x = np.arange(len(term_data))
    width = 0.25
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.bar(x - width, term_data["Enrolled"], width, label="Enrolled (avg)", color="#FF9800")
    ax2 = ax.twinx()
    ax2.bar(x,       term_data["Retention Rate (%)"],     width, label="Retention %",    color="#2196F3", alpha=0.8)
    ax2.bar(x + width, term_data["Student Satisfaction (%)"], width, label="Satisfaction %", color="#4CAF50", alpha=0.8)
    ax.set_xticks(x); ax.set_xticklabels(term_data["Term"])
    ax.set_ylabel("Enrolled Students"); ax2.set_ylabel("Percentage (%)")
    ax.set_title("Spring vs Fall – Key Metrics")
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=7)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

with col4:
    st.subheader("🏫 Department Enrollment Distribution")
    dept_cols = {
        "Engineering": "Engineering Enrolled",
        "Business":    "Business Enrolled",
        "Arts":        "Arts Enrolled",
        "Science":     "Science Enrolled",
    }
    active_cols = {k: v for k, v in dept_cols.items() if k in selected_depts}
    if active_cols:
        totals = {k: filtered[v].sum() for k, v in active_cols.items()}
        fig, ax = plt.subplots(figsize=(5, 3.5))
        colors = ["#2196F3", "#FF9800", "#4CAF50", "#9C27B0"]
        wedges, texts, autotexts = ax.pie(
            totals.values(),
            labels=totals.keys(),
            autopct="%1.1f%%",
            colors=colors[:len(totals)],
            startangle=140,
            wedgeprops=dict(width=0.6),  # donut
        )
        ax.set_title("Total Enrollment by Department")
        fig.tight_layout()
        st.pyplot(fig)
        plt.close(fig)
    else:
        st.info("Select at least one department.")

# ── Row 3: Stacked bar – enrollment by year & dept ───────────────────────────
st.subheader("📊 Enrollment by Department Over the Years")
dept_year = filtered.groupby("Year")[
    [dept_cols[d] for d in selected_depts if d in dept_cols]
].sum()
dept_year.columns = [c.replace(" Enrolled", "") for c in dept_year.columns]

if not dept_year.empty:
    fig, ax = plt.subplots(figsize=(12, 4))
    dept_year.plot(kind="bar", stacked=True, ax=ax,
                   color=["#2196F3", "#FF9800", "#4CAF50", "#9C27B0"][:len(dept_year.columns)])
    ax.set_xlabel("Year"); ax.set_ylabel("Students Enrolled")
    ax.set_title("Stacked Enrollment by Department and Year")
    ax.legend(loc="upper left")
    plt.xticks(rotation=45)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

# ── Row 4: Applications vs Enrolled ─────────────────────────────────────────
st.subheader("📥 Applications vs Admitted vs Enrolled")
funnel = filtered.groupby("Year")[["Applications", "Admitted", "Enrolled"]].mean().reset_index()
fig, ax = plt.subplots(figsize=(12, 3.5))
ax.plot(funnel["Year"], funnel["Applications"], marker="o", label="Applications", color="#E91E63")
ax.plot(funnel["Year"], funnel["Admitted"],    marker="s", label="Admitted",     color="#FF9800")
ax.plot(funnel["Year"], funnel["Enrolled"],    marker="^", label="Enrolled",     color="#2196F3")
ax.set_xlabel("Year"); ax.set_ylabel("Number of Students")
ax.set_title("Admissions Funnel Over Time")
ax.legend(); fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

st.markdown("---")
st.caption("Dashboard developed for Data Mining · Universidad de la Costa · " + " | ".join(TEAM_MEMBERS))
