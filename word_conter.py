a_1, a_2 = "A", "a"
b_1, b_2 = "B", "b"
c_1, c_2 = "C", "c"
d_1, d_2 = "D", "d"
e_1, e_2 = "E", "e"
f_1, f_2 = "F", "f"
g_1, g_2 = "G", "g"
h_1, h_2 = "H", "h"
i_1, i_2 = "I", "i"
j_1, j_2 = "J", "j"
k_1, k_2 = "K", "k"
l_1, l_2 = "L", "l"
m_1, m_2 = "M", "m"
n_1, n_2 = "N", "n"
o_1, o_2 = "O", "o"
p_1, p_2 = "P", "p"
q_1, q_2 = "Q", "q"
r_1, r_2 = "R", "r"
s_1, s_2 = "S", "s"
t_1, t_2 = "T", "t"
u_1, u_2 = "U", "u"
v_1, v_2 = "V", "v"
w_1, w_2 = "W", "w"
x_1, x_2 = "X", "x"
y_1, y_2 = "Y", "y"
z_1, z_2 = "Z", "z"
def word_counter(txt):
    count_a, count_b, count_c, count_d = 0, 0, 0, 0
    count_e, count_f, count_g, count_h = 0, 0, 0, 0
    count_i, count_j, count_k, count_l = 0, 0, 0, 0
    count_m, count_n, count_o, count_p = 0, 0, 0, 0
    count_q, count_r, count_s, count_t = 0, 0, 0, 0
    count_u, count_v, count_w, count_x = 0, 0, 0, 0
    count_y, count_z = 0, 0
    for i in txt:
        if ((i == a_1) or (i == a_2)):        # count a
            count_a = count_a + 1
            if(count_a != 0):
                continue
        elif((i == b_1) or (i == b_2)):       # count b
            count_b = count_b + 1
            if(count_b != 0):
                continue
        elif ((i == c_1) or (i == c_2)):      # count c 
            count_c = count_c + 1
            if(count_c != 0):
                continue
        elif ((i == d_1) or (i == d_2)):      # count d
            count_d = count_d + 1
            if(count_d != 0):
                continue
        elif ((i == e_1) or (i == e_2)):      # count e
             count_e = count_e + 1
             if(count_e != 0):
                 continue
        elif ((i == f_1) or (i == f_2)):      # count f
             count_f = count_f + 1
             if(count_f != 0):
                 continue
        elif ((i == g_1) or (i == g_2)):      # count g
             count_g = count_g + 1
             if(count_g != 0):
                 continue
        elif ((i == h_1) or (i == h_2)):      # count h
             count_h = count_h + 1
             if(count_h != 0):
                 continue
        elif ((i == i_1) or (i == i_2)):      # count i
             count_i = count_i + 1
             if(count_i != 0):
                 continue
        elif ((i == j_1) or (i == j_2)):      # count j
             count_j = count_j + 1
             if(count_j != 0):
                 continue
        elif ((i == k_1) or (i == k_2)):      # count k
             count_k = count_k + 1
             if(count_k != 0):
                 continue
        elif ((i == l_1) or (i == l_2)):      # count l
             count_l = count_l + 1
             if(count_l != 0):
                 continue
        elif ((i == m_1) or (i == m_2)):      # count m
             count_m = count_m + 1
             if(count_m != 0):
                 continue
        elif ((i == n_1) or (i == n_2)):      # count n
             count_n = count_n + 1
             if(count_n != 0):
                 continue
        elif ((i == o_1) or (i == o_2)):      # count o
             count_o = count_o + 1
             if(count_o != 0):
                 continue
        elif ((i == p_1) or (i == p_2)):      # count p
             count_p = count_p + 1
             if(count_p != 0):
                 continue
        elif ((i == q_1) or (i == q_2)):      # count q
             count_q = count_q + 1
             if(count_q != 0):
                 continue
        elif ((i == r_1) or (i == r_2)):      # count r
             count_r = count_r + 1
             if(count_r != 0):
                 continue
        elif ((i == s_1) or (i == s_2)):      # count s
             count_s = count_s + 1
             if(count_s != 0):
                 continue
        elif ((i == t_1) or (i == t_2)):      # count t
             count_t = count_t + 1
             if(count_t != 0):
                 continue
        elif ((i == u_1) or (i == u_2)):      # count u
             count_u = count_u + 1
             if(count_u != 0):
                 continue
        elif ((i == v_1) or (i == v_2)):      # count v
             count_v = count_v + 1
             if(count_v != 0):
                 continue
        elif ((i == w_1) or (i == w_2)):      # count w
             count_w = count_w + 1
             if(count_w != 0):
                 continue
        elif ((i == x_1) or (i == x_2)):      # count x
             count_x = count_x + 1
             if(count_x != 0):
                 continue
        elif ((i == y_1) or (i == y_2)):      # count y
             count_y = count_y + 1
             if(count_y != 0):
                 continue
        elif ((i == z_1) or (i == z_2)):      # count z
             count_z = count_z + 1
             if(count_z != 0):
                 continue
    if(count_a != 0):
        print(" number of a : ",count_a)
    if(count_b != 0):
        print(" number of b : ",count_b)
    if(count_c != 0):
        print(" number of c : ",count_c)
    if(count_d != 0):
        print(" number of d : ",count_d)
    if(count_e != 0):
        print(" number of e : ",count_e)
    if(count_f != 0):
        print(" number of f : ",count_f)
    if(count_g != 0):
        print(" number of g : ",count_g)
    if(count_h != 0):
        print(" number of h : ",count_h)
    if(count_i != 0):
        print(" number of i : ",count_i)
    if(count_j != 0):
        print(" number of j : ",count_j)
    if(count_k != 0):
        print(" number of k : ",count_k)
    if(count_l != 0):
        print(" number of l : ",count_l)
    if(count_m != 0):
        print(" number of m : ",count_m)
    if(count_n != 0):
        print(" number of n : ",count_n)
    if(count_o != 0):
        print(" number of o : ",count_o)
    if(count_p != 0):
        print(" number of p : ",count_p)
    if(count_q != 0):
        print(" number of q : ",count_q)
    if(count_r != 0):
        print(" number of r : ",count_r)
    if(count_s != 0):
        print(" number of s : ",count_s)
    if(count_t != 0):
        print(" number of t : ",count_t)
    if(count_u != 0):
        print(" number of u : ",count_u)
    if(count_v != 0):
        print(" number of v : ",count_v)
    if(count_w != 0):
        print(" number of w : ",count_w)
    if(count_x != 0):
        print(" number of x : ",count_x)
    if(count_y != 0):
        print(" number of y : ",count_y)
    if(count_z != 0):
        print(" number of z : ",count_z)
    print("---------------------------------------") 
#-----------------------------------------------------------------       
print("---------------------------------------")    
print("Please enter a text")
txt = input(">>> ")
print("---------------------------------------") 
word_counter(txt)