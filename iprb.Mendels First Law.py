# IPRB: Mendel's First Law
# 11.30.15
# @totallygloria

k, m, n = 27.0, 21.0, 17.0
total_poss = (k + m + n - 1) * 3.0

k_poss = ((k-1)*(1.0)) + (m*(1.0)) + (n*(1.0))
m_poss = (k*(4.0/4)) + ((m-1)*(3.0/4)) + (n*(2.0/4))
n_poss = (k*(4.0/4)) + (m*(2.0/4)) + ((n-1)*(0.0/4))

print k_poss, m_poss, n_poss
print (k_poss + m_poss + n_poss) / total_poss




