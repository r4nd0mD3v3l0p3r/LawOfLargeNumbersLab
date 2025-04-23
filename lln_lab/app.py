import logging

import numpy as np
import streamlit as st
import plotly.graph_objects as go

from lln_lab.distributions.distributions import get_expected_value, generate_samples
from lln_lab.distributions.distributions_definitions import Distribution

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

st.set_page_config(page_title="Law of Large Numbers Lab", layout="wide")
st.title("Law of Large Numbers Lab")

st.sidebar.header("Simulation Settings")

distribution = st.sidebar.selectbox("Choose a distribution", options=list(Distribution))
num_simulations = st.sidebar.slider("Number of simulations", min_value=1, max_value=10, value=3)
sample_size = st.sidebar.slider("Sample size", min_value=10, max_value=2000, step=10)

if st.sidebar.button("Run Simulation"):
    with st.spinner("Generating simulations..."):
        expected_value = get_expected_value(distribution)
        formatted_expected_value = f"{expected_value:.2f}".rstrip("0").rstrip(".")

        sample_means = []

        fig = go.Figure()

        for i in range(num_simulations):
            samples = generate_samples(distribution, sample_size)
            running_mean = np.cumsum(samples) / np.arange(1, sample_size + 1)
            sample_means.append(running_mean[-1])

            fig.add_trace(go.Scatter(
                y=running_mean,
                mode="lines",
                name=f"Simulation {i + 1}",
                opacity=0.6
            ))

        fig.add_trace(go.Scatter(
            x=[0, sample_size - 1],
            y=[expected_value, expected_value],
            mode="lines",
            name=rf"μ = {formatted_expected_value}",
            line=dict(color="red", dash="dash")
        ))

    fig.update_layout(
        title="Convergence of sample means to expected value",
        xaxis_title="n (sample size)",
        yaxis_title="X̄ₙ (sample mean)",
        showlegend=True,
        margin=dict(t=60, r=20, l=20, b=40),
        xaxis=dict(
            showgrid=True
        ),
        yaxis=dict(
            showgrid=True
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    if expected_value == 0:
        formatted_mu = "0"
    else:
        formatted_mu = f"{expected_value:.4f}".rstrip("0").rstrip(".")

    st.latex(rf"\mu = {formatted_mu}")

    st.markdown(
        "### Sample Means  \nEach entry shows the sample mean $\\bar{X}_n^{(i)}$ from the $i^\\text{th}$ simulation of size $n$.")

    for i in range(num_simulations):
        st.latex(rf"\bar{{X}}_{{{sample_size}}}^{{({i + 1})}} = {{{sample_means[i]:.4f}}}")
