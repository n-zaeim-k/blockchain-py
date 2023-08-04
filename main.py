from chain import Chain

chain=Chain(10)
i=0

while(True):
    data=input("Add sumething to the chain: ")
    chain.add_to_pool(data)
    chain.mine()
    print(chain.blocks[i])
   