def generate_receipt(name, *prices, **change):
   total= sum(prices)
   for item,value in change.items():
    if "discount" in item.lower() or "coupon"in item.lower():
         total-=value
    elif "tax" in item.lower():
         total+=value
    total=round(total,2)
    print(f"Receipt for: {name}")
    print(f"Final Total: ${total:.2f}")
    return total
generate_receipt("Alice", 10.50, 20.00, 5.25, coupon=5.00, special_discount=2.50)
