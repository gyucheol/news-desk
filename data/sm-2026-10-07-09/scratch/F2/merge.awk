BEGIN { FS = "\t"; OFS = "\t"; bad = 0 }
NR == FNR {
    n = split($0, a, /[ \t]+/)
    if (n < 3) next
    code[a[1]] = a[2]
    fld[a[1]] = a[3]
    dupof[a[1]] = (n >= 4) ? a[4] : ""
    next
}
{
    cnt++
    src[cnt] = $0
}
END {
    K_ok = " macro rates geo trade energy power metals agri semis ai tech auto aero pharma fin consumer shipping realestate industrial other "
    D_ok = " sports life politics crime wrap explainer ai-invest dup other "
    if (cnt != 418) { print "input line count " cnt " != 418" > "/dev/stderr"; bad++ }
    for (i = 1; i <= cnt; i++) {
        if (!(i in code)) { print "no decision for line " i > "/dev/stderr"; bad++; continue }
        if (code[i] == "K") {
            if (index(K_ok, " " fld[i] " ") == 0) { print "bad K field, line " i ": " fld[i] > "/dev/stderr"; bad++ }
        } else if (code[i] == "D") {
            if (index(D_ok, " " fld[i] " ") == 0) { print "bad D reason, line " i ": " fld[i] > "/dev/stderr"; bad++ }
        } else { print "bad code, line " i ": " code[i] > "/dev/stderr"; bad++ }
        print code[i], fld[i], src[i]
    }
    for (i = 1; i <= cnt; i++) {
        if (fld[i] == "dup") {
            k = dupof[i]
            if (!(k in code) || code[k] != "K" || fld[k] == "dup") { print "bad dup target, line " i " -> " k > "/dev/stderr"; bad++ }
            split(src[k], p, "\t")
            print i, k, "중복: " p[4] > NOTES
        }
    }
    print "validation problems: " bad > "/dev/stderr"
}
