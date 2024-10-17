from ecommerce.customer import contact

def calculate_tax():
    print("Tax Calculation")


def calculate_shipping():
    print("Shipping Cost Calculation")

def get_customer_for_order():
    details=contact.get_customer_contact()
    print(f"Details : {details}")
