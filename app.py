import streamlit as st
import pandas as pd
import sqlite3
from database import create_table, connect_db

# Initialize database
create_table()

st.set_page_config(page_title="My Budget App", page_icon="💰", layout="wide")

st.sidebar.title("💰 Smart Budget")
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigation", ["Dashboard", "Add Transaction", "View Transactions"])
st.sidebar.markdown("---")
st.sidebar.info("Track your income and expenses easily.")

if page == "Add Transaction":
    st.title("➕ Add Transaction")
    
    date = st.date_input("Date")
    transaction_type = st.selectbox("Type", ["Income", "Expense"])
    category = st.text_input("Category")
    amount = st.number_input("Amount", min_value=0.0)
    description = st.text_area("Description")
    
    if st.button("Add"):
        conn = connect_db()
        cursor = conn.cursor()
        
        cursor.execute("""
        INSERT INTO transactions (date, type, category, amount, description)
        VALUES (?, ?, ?, ?, ?)
        """, (str(date), transaction_type.lower(), category, amount, description))
        
        conn.commit()
        conn.close()
        
        st.success("Transaction added successfully!")

if page == "View Transactions":
    st.title("Transaction History")
    
    conn = connect_db()
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()
    
    if not df.empty:
        st.dataframe(df)

        st.subheader("Delete a Transaction")

        transaction_ids = df["id"].tolist()
        selected_id = st.selectbox("Select Transaction ID to Delete", transaction_ids)

        if st.button("Delete"):
            from database import delete_transaction
            delete_transaction(selected_id)
            st.success("Transaction deleted successfully!")
            st.rerun()
    else:
        st.info("No transactions found.")
    
    st.dataframe(df)
if page == "Dashboard":
    st.title("📊 Financial Dashboard")
    
    conn = connect_db()
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()
    
    if not df.empty:
        total_income = df[df["type"]=="income"]["amount"].sum()
        total_expense = df[df["type"]=="expense"]["amount"].sum()
        balance = total_income - total_expense
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Income", f"${total_income:,.2f}")
        col2.metric("Total Expense", f"${total_expense:,.2f}")
        col3.metric("Savings", f"${balance:,.2f}")
        
        st.markdown("---")

        st.subheader("Spending by Category")
        expense_df = df[df["type"]=="expense"]
        category_summary = expense_df.groupby("category")["amount"].sum()
        st.bar_chart(category_summary)
        
        st.subheader("Monthly Trend")
        df["month"] = pd.to_datetime(df["date"]).dt.to_period("M")
        monthly = df.groupby("month")["amount"].sum()
        st.line_chart(monthly)
        
    else:
        st.info("No transactions yet. Add one to see dashboard.")