# def Winner(d,s):
#     total_d = 0
#     total_s = 0
#     for i in d:
#         total_d = total_d + i
#     for j in s:
#         total_s = total_s + j

#     if total_d != total_s:
#         if total_d > total_s:
#             print('Dragon')
#         else:
#             print('Sloth')

#     else:
#         pass

    


# t = int(input())
# for _ in range(t):
#     while True:
#         dragon = list(map(int, input().split()))
#         if len(dragon) == 3:
#             break
#         print('Error: Length of dragon list does not match 3. Please enter again.')

#     while True:
#         sloth = list(map(int, input().split()))
#         if len(sloth) == 3:
#             break
#         print('Error: Length of sloth list does not match 3. Please enter again.')

#     Winner(dragon,sloth)

# cook your dish here
T = int(input().strip())
# print(T)

for _ in range(T):
    D1, D2, D3 = list(map(int,input().split()))
    S1, S2, S3 = list(map(int,input().split()))
    T_Dragon = D1 + D2 + D3
    T_Sloth = S1 + S2 + S3
    # print(D1,D2,D3)
    # print(S1,S2,S3)
    # print(f'T_Dragon {T_Dragon}')
    # print(f'T_Sloth {T_Sloth}')
    
    if T_Dragon <= 300 and T_Sloth <= 300:
        if T_Dragon == T_Sloth:
            if D1 == S1:
                if D2 == S2:
                    print('Tie')
                elif D2 > S2:
                    print('DRAGON')
                else:
                    print('SLOTH')
            elif D1 > S1:
                print('DRAGON')
            else:
                print('SLOTH')
        elif T_Dragon > T_Sloth:
            print('DRAGON')
        else:
            print('SLOTH')
    # else:
    #     print('Wrong Total')

#Correct