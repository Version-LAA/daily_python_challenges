def sandwiches(*toppings):
    print("I have a sandwhich with the following toppings:")
    for topping in toppings: print(topping)


sandwiches('tomatoes','onions','peppers')
sandwiches('mayo','hot peppers','sweet peppers')

def make_car(brand,model,**kwargs):
    kwargs['brand'] = brand
    kwargs['model'] = model
    print(kwargs)


make_car('mercedes','a402',color='red',miles=12000)
