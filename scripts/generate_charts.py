# File: generate_charts.py

import pandas as pd
import plotly.express as px
import os

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# Create output directory if it doesn't exist
output_dir = "visualizations"
os.makedirs(output_dir, exist_ok=True)

# ========== Chart 1: Marks Distribution ==========
df_melted = df.melt(var_name="subject", value_name="score",
                    value_vars=["math score", "reading score", "writing score"])

fig1 = px.histogram(df_melted, x="score", color="subject", barmode="overlay",
                    title="Marks Distribution Across Subjects")
fig1.write_html(f"{output_dir}/marks_distribution.html")

# ========== Chart 2: Gender Comparison ==========
df_gender = df.melt(id_vars="gender",
                    value_vars=["math score", "reading score", "writing score"],
                    var_name="subject", value_name="score")

fig2 = px.bar(df_gender, x="subject", y="score", color="gender", barmode="group",
              title="Gender-based Comparison of Student Performance")
fig2.write_html(f"{output_dir}/gender_comparison.html")

# ========== Chart 3: Test Prep Effect ==========
df_prep = df.melt(id_vars="test preparation course",
                  value_vars=["math score", "reading score", "writing score"],
                  var_name="subject", value_name="score")

fig3 = px.box(df_prep, x="subject", y="score", color="test preparation course",
              title="Effect of Test Preparation on Student Scores")
fig3.write_html(f"{output_dir}/test_prep_effect.html")

print("✅ Charts generated and saved in /visualizations")
