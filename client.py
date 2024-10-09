import Pyro4

name = input("Who would you like to search for? (Use First Name): ").strip()

tax_payers_maker = Pyro4.Proxy("PYRONAME:example.tax_payers")
print(tax_payers_maker.get_tax_payer(name))
