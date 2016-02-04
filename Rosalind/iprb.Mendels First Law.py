# IPRB: Mendel's First Law
# 12.01.15
# @totallygloria

k, m, n = 24.0, 15.0, 27.0
total = k + m + n

print total

kk = (k/total) * ((k-1)/(total-1)) * 1.0
km = (k/total) * (m/(total-1)) * 1.0
kn = (k/total) * (n/(total-1)) * 1.0

mk = (m/total) * (k/(total-1)) * 1.0
mm = (m/total) * ((m-1)/(total-1)) * 0.75
mn = (m/total) * (n/(total-1)) * 0.50

nk = (n/total) * (k/(total-1)) * 1.0
nm = (n/total) * (m/(total-1)) * 0.50
nn = (n/total) * ((n-1)/(total-1)) * 0.0

total_poss = kk + km + kn + mk + mm + mn + nk + nm + nn

print total_poss





