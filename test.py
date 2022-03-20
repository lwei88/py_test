# Q1
A = ["Ali","Hamza","Usman"]
B = [[23, 29, 32], [5.8, 5.9, 6.1]]

for i in range(len(A)):
    print(f"{A[i]} is {B[0][i]} years old and his height is {B[1][i]}ft")

# Q2
def remove_duplicates(word_list):
    return list(dict.fromkeys(word_list))
print(remove_duplicates(['a', 'b', 'd', 'd', 'a', 'c', 'e', 'z', 'b']))

# Q3
def extract_email(email):
    print(f"username: {email[0:email.index('@')]}")
    print(f"company name: {email[email.index('@') + 1: email.index('.')]}")
extract_email("liang_wei88@hotmail.com")


# Q4
A = [1,3,6,78,35,55] 
B = [12,24,35,55,88,78,155]
print(list(set(A).intersection(set(B))))

# Q5
def sum_recursive(start, end):
    if start == end:
        return start
    return start + sum_recursive(start + 1, end)
print(sum_recursive(1, 10))