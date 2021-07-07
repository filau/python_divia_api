from divia_api import DiviaAPI


api = DiviaAPI()

x = api.find_stop("T2", "Darcy", "R")

print(x.totem())
