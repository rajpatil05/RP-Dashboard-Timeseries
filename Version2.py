# Import required libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration for better layout and icon
st.set_page_config(page_title="Business Dashboard", page_icon="📊", layout="wide")

# 1.0 Title and Introduction with background color and larger fonts
st.markdown("<div style='background-color:#1f77b4; padding:10px; border-radius:5px;'><h1 style='color:white;text-align:center;'>📊 Business Dashboard</h1></div>", unsafe_allow_html=True)
st.write("""
### Get insights into sales, customer demographics, and product performance. Upload your data to get started!
""")

# 2.0 Data Input Section with styling
st.markdown("<h2 style='color:#4CAF50;'>📂 Upload Business Data</h2>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose a CSV File", type="csv", accept_multiple_files=False)

# 3.0 Main Content: Check if data is uploaded and then show insights
if uploaded_file:
    # Read the uploaded data
    data = pd.read_csv(uploaded_file)
    st.markdown("<h3 style='color:#FF6347;'>🔍 Data Preview</h3>", unsafe_allow_html=True)
    st.write(data.head())

    # 3.1 Sales Insights with a colorful line plot
    st.markdown("<h3 style='color:#FF6347;'>📈 Sales Insights</h3>", unsafe_allow_html=True)
    if 'sales_date' in data.columns and 'sales_amount' in data.columns: 
        st.write("Sales Over Time")
        fig = px.line(data, x='sales_date', y='sales_amount', title="Sales Over Time", color_discrete_sequence=['#FF4500'])
        fig.update_layout(plot_bgcolor="#f5f5f5", title_font=dict(size=20))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Please ensure your data has 'sales_date' and 'sales_amount' columns for sales visualization.")

    # 3.2 Customer Segmentation by Region with colorful pie chart
    st.markdown("<h3 style='color:#FF6347;'>🌎 Customer Segmentation</h3>", unsafe_allow_html=True)
    if 'region' in data.columns and 'sales_amount' in data.columns:
        fig = px.pie(data, names='region', values='sales_amount', title="Customer Segmentation by Region", color_discrete_sequence=px.colors.sequential.RdBu)
        fig.update_layout(plot_bgcolor="#f5f5f5", title_font=dict(size=20))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Please ensure your data has a 'region' column for customer segmentation.")

    # 3.3 Product Analysis with colorful bar chart
    st.markdown("<h3 style='color:#FF6347;'>📦 Product Analysis</h3>", unsafe_allow_html=True)
    if 'product' in data.columns and 'sales_amount' in data.columns:
        top_products_df = data.groupby('product').sum('sales_amount').nlargest(10, 'sales_amount')
        fig = px.bar(top_products_df, x=top_products_df.index, y='sales_amount', title="Top Products By Sales", color_discrete_sequence=['#4169E1'])
        fig.update_layout(plot_bgcolor="#f5f5f5", title_font=dict(size=20), xaxis_title="Product", yaxis_title="Sales Amount")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Please ensure your data has 'product' and 'sales_amount' columns for product analysis.")

    # 3.4 Feedback Form with colorful text area and submit button
    st.markdown("<h3 style='color:#FF6347;'>💬 Feedback (Your Opinion Counts)</h3>", unsafe_allow_html=True)
    feedback = st.text_area("Please provide any feedback or suggestions.")
    if st.button("Submit Feedback"):
        st.success('Thank you for your feedback!')

# 4.0 Footer
st.markdown("---")
st.markdown("<p style='text-align:center; color:#808080;'>This business dashboard template is flexible and can be expanded upon based on your specific business needs.</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    pass
