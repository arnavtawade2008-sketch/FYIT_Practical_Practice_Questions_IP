# Q3
amount = float(input("Enter Bill Amount: "))
discount_pct = float(input("Enter discount%: "))
gst_pct = float(input("Enter GST%: "))
after_discount = amount - amount * discount_pct / 100
net_bill = after_discount + after_discount * gst_pct / 100
print(f"Discount: Rs. {amount * discount_pct / 100}, GST: Rs. {after_discount * gst_pct} NetBill: Rs. {net_bill}")
