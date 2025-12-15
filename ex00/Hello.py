ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

ft_tuple = ("Hello", "World")

ft_set = {"Hello" if s == "Hello" else "Tokyo!" for s in ft_set}

ft_dict["Hello"] = "42Tokyo!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
