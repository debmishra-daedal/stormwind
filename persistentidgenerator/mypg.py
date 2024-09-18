from persistentidgenerator import seqguidgen as idgen

val = idgen.guidgen()
fn = val.generate_id("rand")
mid = [fn.masterId, fn.numericId, fn.category]
print(mid)
print("--checking log output and errors--")
print(val.logout)
print(val.logerr)
