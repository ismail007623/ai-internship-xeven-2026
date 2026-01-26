day_1 = {
    "192.168.1.2",
    "192.168.1.3",
    "192.168.1.2",
    "192.168.1.5",
    "10.0.0.2",
    "10.0.0.3",
    "172.16.0.1"
}

day_2 = {
    "192.168.1.2" ,
    "192.168.1.5",
    "10.0.0.2" ,   
    "172.16.0.1",
    "10.0.0.3",
}

day_3 = {
    "192.168.1.6" ,
    "192.168.1.5",
    "10.0.0.8" ,   
    "172.16.0.6",
    "10.0.0.3",
}

# common visitor day 1 to day 3
comman_visitor = day_1 & day_2 & day_3
print("common visitor in day 1 to day 3:",comman_visitor)

# visitor lost day 1
day_1_vistor = day_1 - day_2
print("day 1 visitor :",day_1_vistor)

# visitor lost day 2
day_02_visitor = day_2 - day_3
print("Day 2 lost visitor:",day_02_visitor)

# total unique visitor in day 1 to day 3
total_unique_visitor = day_1 | day_2 | day_3
print("Total unqiue visitor :", len(total_unique_visitor))

# finding growth rate
day1_count = len(day_1)
day3_count = len(day_3)
growth_rate = (( day3_count - day1_count ) / day1_count)  * 100

# finding retention rate
returning_user = day_1 & day_3 
retention_rate = (len(returning_user)/day1_count) * 100 

print(f"growth rate :{growth_rate} And Retention rate :{retention_rate} ")



