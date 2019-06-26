fa = open ("./Dictionary/chr21", "r+")
print "open file "
seq = fa.read ()
length = len(seq)
print "get seq",length
fa.close ()
print "seq[32636549:32636648]",seq[32636549:32636648]
print "seq[31721978:31722075]",seq[31721978:31722075]
print "seq[-32636549:-32636648]",seq[-32636648:-32636549]
print "seq[-31721978:-31722075]",seq[-31722075:-31721978]

