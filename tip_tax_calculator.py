import streamlit as st

def tip_tax_calculator():
    st.title("💸 Tip & Tax Calculator")

    # Input section
    subtotal = st.number_input("Enter Subtotal ($)", min_value=0.0, step=0.01)
    tip_prcnt = st.number_input("Enter Tip Percentage (%)", min_value=0.0, step=0.1)
    tax_prcnt = st.number_input("Enter Tax Percentage (%)", min_value=0.0, step=0.1)

    if st.button("Calculate Total"):
        tip_amount = subtotal * (tip_prcnt / 100)
        tax_amount = subtotal * (tax_prcnt / 100)
        total = subtotal + tip_amount + tax_amount

        st.subheader("🧾 Bill Summary")
        st.write(f"💁 Tip Amount: **${tip_amount:.2f}**")
        st.write(f"🏛 Tax Amount: **${tax_amount:.2f}**")
        st.write(f"💰 Total Bill: **${total:.2f}**")

# Call the function
tip_tax_calculator()
