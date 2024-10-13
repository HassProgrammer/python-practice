# WAF to convert USD to BDT.
usd = int(input("Enter USD:\t"))


def usd_to_bdt(usd):
    bdt = usd * 119.35
    print(f"{usd} USD = {bdt} BDT")

usd_to_bdt(usd)