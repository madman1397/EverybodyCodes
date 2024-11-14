PotionChart = {
    'A':0,
    'B':1,
    'C':3,
    'D':5
}
Part1 = "AABBBCBABCBBABCBAAACABCAACBCBCBCABACAABCBCBAABCCABBCCACABBCBAAABAACCAACCAACCBBAAABBBBACCBCBBBCBAAAAABAABBACBCBBABAABCABBCBBCABBBCBBCACBBCCBCAAACABAABABAAACBBCACCCCCBAACCCCAACABBBABBBCABCACAAABCCCAACCCCAABBCBBCCBAABBAABCBABAAAACACBABCCCBACCCBBABACAACBACCACCAABAACABCACCAAABBCCAAAAABAABCCACBCBCCCAABCBABBCBACAAAABBCBCCCCCAABCCBCABACACAAAACCABCCAABAACCABBACBAAACCAAACBCBCACBCBBCABAABACCACBCCAAAABABAAABCBBBBCBACACABABBCAACBAACABBCACBCBBBACCBBBCCABACACBBACAACBACAAACCACBACCBAABBABCBABBCCBCACCBAACBABBAABBABCABAABABBABBACCABAAACBBCBCAAACACABBAAACCABBBACCCBBCCABBBCCCAABCCBAABACBACCBCCCABCBABAAACCACCCCCCCABCBAAABBABABBACABBCBACAABBCCBAACBCACABBACBCACCAABBACABBACCAAAAABBCAACABAACBBBBAABAABCBBCCBCCACCBCCCBACCCBAAAABBACCAABABCACCCAABACACCAACBCBBABCACBCBBCBBACBCAAABACCABACBBBBACBBCCBCABCCABACBCAAABAAABCCAACACCCCBCABACACBACBACCBABACACCACCAABCCACCCBCCCCBAACAABBAACCBABCAABCABACCCAABBCCABACACCBCAACACAACBCBCBCCAABAACCABAABBABBAABBBACBABBBCCBAACAABCCACBCBCCCCCBCBACCCCBACCBBCBBBABCACBBBACACCACBBCBCCBBCACACCCC"
Part2 = "DABCxDBBDAABCBDBDBDDBACDCBADxBBDDxAABxxAACBCABDADABBBDBxCxAACACxCAAADxAACDCAxAACAxCBABDDxCAAAxCCBBDBDBBAADCAADADDBCDDAABDBDADBAADACABCBDAADDxCCBDADAAAADCBxAABDCADxBxADCADBxxDCDBCDDBDBAAACxAADBACCDABxCCBABDBBDBCBCxCCCAADBBDDCxBDBADBACABBCCxADDBxAxDDDBDBxxCDCBAxDDACCCCABADBAABCBABDCxCxDDBBDDBDxAABABBBACCCBBCBCBCBCAADADBDCDBCCDABDDDACAAABDBDDDDxBBxCCBDBDDAxDDCAAxACDCBCCAAAxCBADBBCBAADDCCACBxCCAxCBDCDBDBACBDADACCAACAxBAxDCCBBDxAACCBDxxACDABBDDABDCDBBBCACAABCBxCxxBDBBBAxCCDDxCBDBDDBxAxxDBCBBBDDACxDxAxDACxDCAAACCBADBAABCCxDAABADxAACBACDCDDAACDBBCAADDDDAADDBxxCACACxDAxAxDDABBxAACxBCBACCCDBACCBACDxBxBAABACBBDAAxCCxABCxCACCCCxxBAxCCxDBDDACBDxBAABABDACABCxCxCxCCDxxBCDBBBDABCADABCADDAACCxCADCCACAAxABDxDCCAABBCxCBDDDDCAAACADDCABCDBDACAABACDBDCDBAABxAABCCAxCAABABCDBACBDDABACBAxCDCDAAxBDDCAABBABABBxCDAABDBCDDDDDDDCCACCCACCDAABBACDBACBDDxABAADAxCDCABCADDADDDBxBBCCABACxCCDDBCACABCBAACxBxBBDDCDCAxCBCBCDADDCBDAAACCDCxBxCACDACBDxxDBCCBxBBAAABDAAxCCCCDCCBBDDDCCADBCBDDBABBBCCCBBAAAACADAADBACACADDxBBCCBDxCCBCCAxxCAACBBCBxxCCBAACCxAADCBCBCDBCAAACDCCDCDxCADCCDBABDBCABCBDDABAACADDxDAxBBACABACDCDxAxDDCAAxAABBADxDxBCxBxACDBACCADDCBBCDAAADBABCxABCxACBDABBDBACCABDDxxCDABAxBDBBBDDDCDxxBDDBDDCDBDxBCCBBDxADDBAABCCxACAxBCBxDxDDDDABBxCADBADDAACDBACCBxxCAAxDDDADDDBDDACBDDBCCDBACDBAACxDBDACBCDDxAACDDxCBDCAxxDBxBDBDDDxCDAACBDDDCAACBADCxDABBBDAAAADBABAxABBADBBBDDABCACCAAADADDDBCxCBDDACDBACCCCCAAxBBBCBxDCBxxBBCCDxAxBAxBADDCBCADDCACxBAxBCCCCCBDCCAADBDCAADBAxBBCDABACDACxACCCxCADCBACBBDAxxxABxBDCxCBCABADCCCxADCAABBCDBACCxDAACDDxDCCAAACCCBADDCCBDDAxACADACBCDBACxCACBCBCDCDBDDAADADDxxxBDCCxDBDDCADCCCCxAAAxCDACCBDAxxDCDCCCxCxBAxBxDBACBDDDACACDDAACxxCBCACADDCBBxBBABCxCCAABAAAxACCABDCxACACBBDDADDDDACBBBBDDCDDBxBCDxAAACxCBDBCADBBACBBDCACDABCDxCBDABACCCDDBADDBCACACxDxBACBCAxCACAAxCADBDABDACADABAxBDADBxBDDCBADADCAxADCCxBCDxxBxADDAAxDDBBDxCAACDDBBBCADCBDCDAADBDACCCDCxBDDxBBCCCADABCCDDCDBBxDBBBxCBABDABBDACBBCBDxDDBCxCACDDADACxDBCCCACDDDxAAADAAADxBCCDCxADAAADDCDBAACBDCACBCBCADDCDCDBDDDxDCACADCCBDDAxBDBxAABBCADBxDCACABC"
Part3 = "CxDCBCADBAACAxDCAxBCABBxxCDxDBxBxxBDCBAAxCABxDBBCxCCBCAAxBDDABAxxDBCAxxCDxxBBBDxBDDABBxBDADADxBDADxDAxxxxADCACCBxxDDCBCDxCCBBCBxDDxCCCCDxCBCCxABAxDxDDxDDAxCCACxDxDDxxADBDADDDxCDBAxCCBxACACCDCxxBBACCDACCDACDxDAxxABCDxACDDADCCBBCBxCCDCCxACBCCDCADAACCxDCBxCACDxxACxCCxxDBADADCDADBCBAxABACCCxBBBBAACDAxDAADBDCCBCCxADDCCxxDxDxDDCxAxxACDBDBxBCDACDCxCCBCBxAACxDDCDBBBxBADCDxxACxxAADDCCDBxCCBDDABAAxACDDACADBBCBxxDACBABDxxxAAACDCBADDDDBBAADBCACCAAABACxAxCAxBDBDBCBDAxCxCCCCABDBDDADCxxxCDxCxDBxxxBxxBxxACxCBBACDACxxCABCDBDBCABBxxBxCxBACxBABCDDDABDDBAAxADxDCBDxDxDABxBDxAxxDxxBBACxDBxAABxBxACCCCDAADBDDxxDDxDBBAADxxDBDAABABDBCDCxBxxCDABDCAAADCADDADxCDxxDBAxDDBxACxDAADCCBCBACAAABACDBADxCBxAxDAAxCDCDCBBDDBDBCxxxxAAADACBxCBCxCCAAAACCADxBCBDADBACADBxABDBADACCBxCCBDCAxBCxADxDCDDBABBDCCDCxDAABxABCBxDBAAABCDxACCxAAABBADxAAxCDABCxxBBDACABxDxBDCxCxxBCAxCAABCxDxDBCBxxCCDCxxDBxxBxBCBxADAxCCDACABDCDBDxDAxDCCBAAxCBCDCAAxBBAxxBACCBADCDCxxDAxCBADxBABBDCAADCBDxACBxBCxDDDDABDDCADBADCxADxABxCCCDCCxCAACBDCBxDACCCADDxBxDAxBBxCCBxCBCxCCBBBBABCBCxABACCCDxACCBBDCAAxAAxCCDAxxAABABDDACxCDDBCBAACCDxxBCCxCxDAAAxCCDAADBDDACACBxxxAxACBADCAAxxCBBCAxBBAABCCDDBDBBCCBCBABADADCCAxDCxBBCADAACxADCDAxBxBCAADCxBCCCABBDDCxACCBDDCBDBDDBDxCDxCxAxAADxxABADCABDCCACBDDxAxDBxDAxCDAAAxAxDDDxAABCBCDBBxBCxxAABDBBDCACACCBDABCDCDCxDxxBxDxDACCCBxCCDxCBBCABDACBBACxBBDDBDABDCABAAxCDDACBABCCBDxDADACDBCAABDACBBCBDCBDDAxxxxCxCBCDxxCACCDBDAxxDCBBCBxBCADCCCxCxBACxACDDxCBBDxCCCBxDBAxBCCDBAAADDDDDAxDDxxCDDAxBACxABxDCCCDDACDDDABCxDBCDDDBBxCDDBCBCACAxABBDBACBDBCxDCCAADxCCxBCxxBCBCxBxBCDCxADxxAAxxBBDxBxxACAACxACBADDAxBxADCDBBCAAAxxDDxDxxADCCADBADBCDDAxxDCCBABAADDDACAABCBADCABDCCCDBABxBDDxAxxBDCDCDCxCBCDDxxCCBDACDCBCCBCBDxxBBAADxAxAACCxBDBABDCxDCBCDDCDDxBxAxxADBCAAACxACDDDCAxACDxADxABBBxCABCCBCxxBBBACBDDxDxxCDBxABxDDADxCBCxDBDDBCDxDCCxCBCxBBxDBCACADxxxxxDxDxAABDCxADAAxBxxABCAAADCCxADBBCDBAxDAxDAxxCBCxACDxxADxxCCxDBDACDBCBBACADBADxxCDDCBDxCBCBCCBAxDxxADCBACCBAxADxDCDACADDABxDxxABxADCADDBAxCADBCBDBxDDAxAADxxBADCBCxDACDxBBDxDDxBBCxxCDBxxADAxBDDxAxxxAxBBxCADAxDADAxDDAAxADxBCDAADCCCAACBCCDBABBDADBBxDADCDBBAACxCBBxCCBAxDxCDADCxBDDxCDxxxACCCCDDBxAxDxBBCxxxDDCBxBAADADCxADBDCBBCBDCCxDDDBBAxCDDABxCAxACDxDCAACBCxCADxDDxxDCDDCxBADCABBBAACAACBCxxxCxCDCBAxDxCxBACCDDABACxBBBACDCDAAABxCBDBBBDCDAADACDCDDBDBAxCAADxBDAACCDACDBACxCBADCCABxACCBAxCADDxDDAABAABCAxDACxADBDCBADDDBACDBDxCxxCAABDBBBBxAAABDAAABBDDDxxBCDDBADxxxDxDCADACxxxDABxDxBABxDAADABBBBBxDABACxBDxCDBxBCCBAxADxDCCBBDDDACAxxxDCABBBCADxxDBABBCxxDDCCABxCxDADxCBBACxCBxDBDCCCxDCDBBBABAACAxAAxDBBACBADCBCxxCAxxAABAxAxCDDCBAADABBCxDxCCCBABxBBxxAAxxAADDDCCCCDDDxDDBCCABABxxBABCxCDxABABCBBxCABCABxxAADxCABxxAAAxDAxDxBCBDxxDAxBDxBCxAxxBABBBBBCCCCAABAxAADxBDBxAxCABCBBAxxABxxBBDDCCxABxBxADDBBAADxDxxBxACADBCCxCBDBACAACCxCBCCDACBCDxDxxCADABCxBBAACDBxACABxADBxDBxAAxDxAADDxCAAxBAxDxBxCABDBBCBDDCCDACBDCADDBBCxCDCDCxCCxBCBCBCAACADBxBxBCAxDAAAxADxBBDBxBCACCCCxDxCxBCBABADBBBBCxBxDxDxACDBCDCxCxxADDCACCDxBCDACBDAxAxxBBxxBBBxBxAxBBxAACxDCAAxxCDBxxBBAACBDCDDADACCADDDDxxAxxCCAxADxxBADxDDABxBDCxxBBCBxBABBxCxCBAxAAxDCACACBAxAxxAxBDCAAAxxDBDADCDxCDBCCBBBADDCBAAAxDCxBDCAxACADCCBDBBADBBDACBxBCABBCBDDxxADBABDxDxDDADDBBBBxBADDBDDxCxCCDACBADCBxxBAxxCxABCADxDxxAxCADDBAxxADBDxABDCABxDxDABDDBACxCBCBDxBDDxDCAAACAxxBAADAACxBCDBACCCDAxDDAAxxDACBBDDCAAxxCBACBAABxDBDDAxDxxCDDBBDCxxxAxxAxxACCACAABDBxCAxAADCCxBBDxAxDABBBAxACAAAxCAxBACCxDCCxxCAxBDAABDxCBDBBADCDCAxDCBxACAxDDCxAxCCBxDxBBCBxCBDCAADACxCACACCCxDDCADBBCCCDDACDCCBxBxCBxAxDABxCAxBCBDxBxCBxADDDxDABCBACxCDDBxDBDCxDCBxxAACAxDDxBDABDADDCxACADBADCxBAACBDBDCBBxxABxCxDxCAxCBBADDDABCBBADDDBxABAxxBAAAAxBDDABCCABBxxBxCCxAABBBDACAADDDCDDACDAAxBCBBBBADDCxDBBxxBADxxxBDCxxAxCxBBDBBCDACDxBCxDCBBDADDBxDCABCBDxDDxBBDACBCDDAxDCDCAxDxCDCBCxBACBxBBCxCCADCDDDCDxDBCDABDCDDxDCAABBBBCADAxDABAAADCBCDADDABxxxCDBxBACxCDBAAADCDxACxDDABDCDxDBCCBCCBDCDAxDCDABCDDBBADDDBDCBxCxACxCCADxBCABxADxDDBABxxBCCxxACCxxCxxCCDCAxxDxCxBBCCBBDDBDAAxDxBBxDxDDxACDCDADxxDBDDDCCAACDCBCCACABBAADAAAxDADAxCBxAxBCACBADDAxxCDAABxACAACDBBBBABBDxBCxADxxACxACxDBDBDBxBxDxBCxxBBCCAxCDDxAAxBDABCBxDCABADDACxBxAABCxDxxCBABCCBCxxABxDCACDxxxBxCDxxCCBDAxAAxACADxBCxCAAABDBCxAACDBxxDDCDBxCABAACCABxxCDCxxDxCDBDABDDCDCCCCBADBDABxBDACDxDDADACDDxBCCxDABBAxBABDDCxDDADxCxCBDDBCDxCDxxDADCDADxCAABDCBDCDxBAACxBCBCDAxxCAxCCxDADDxBBDxAxAACCCxBABCBDDCCxBCABDxAxDBCCDxBDBCAABBAABCxABBDxxCBABDxAADBDBBDDxDAAAxDDxDAAxxDDCxCBDCBDDDDxCxDBBDAxBCDBxAAADACBBxCBAxABABxABDABxBxxAADDDCxACxCABDDDxDBDDBCADCCxxxBCCxDBCCAAADxxACACAxxACBCDxABCCBABBBxBDCDCBxAxxBABAxxAAACxDCCDCAxxAAADBDAAABBxxCBABADDACDDCBxBCDCAxCBDAAxBDDxDxDCCxxACBACCDCBCCBCCxACxAxBCADACxBBxBxCDCAxCDCxBDCxCDCDCAxAAxADDCxAxBxxAACBDCCBDACBDCCDxxBBCAxCDxBxAxxCBCBDBCBBDADDBCBCBxBDCAxCxBDBBDBBBBxBxAxACCxDBCBxCDBDAxCACxDDCBAADDDxxAxDAxCCDxDCBxCBBACDADCDCxxCBDAADCDBBxDBCDDxACACACDCxDAxxDDAAADABxDCBDCDCDAxAADAAxBxCCxxAABCBxxCxDCxADCACBCCCAxxxAABABADADxxCDBxABBDCxAxDABBxxxADDBDCCDCxCCACxxAADxCBBxDCDBBDBBDxCxxCCCACDCABBCBCBADABxCCCCBAxCDCBBBDxCBCxADABxDCxCCCACCADAABABDCxxCCCxAxCBCxABADBCCDADBxADAxxCAACADxDxCBBACDxBABxxDAxDDDBDBxCCCBAADACCCADADxDBCxBCBCCBDDxCBBCAADCABDCDADBDBxCBDDxBxDAxxDDBDBBCDDDACDDCDDACxDABxDxAAADDDAAAxACBBAxCxAxBDAxDxCxxABBCDAxBAxDADAAAAACCCCCCDABCCBxDCBDDBxBDCDxBxCBAxDCxBxABDDBAABBBCABDBBxBDxBADBDDBCBBDDCDBxBxBDCABCCBxDxCxBBDxxDBBBBBxDBCCCBCCACACADxCAABACCABBADBAACAxxADCxCADDADBxABBCBCCDCCBDAxxAxCBBAABACDBBABxxxBDxBCDCCBCxADCAxBACDCBCCDCBDDDCADBBxCBxxCDACBADxxDDCACABCxxxxBCDDCxBAABxCxBDCCADDCDBxBABxBAxBDAABDDABADDABDCCAxDxxDCAABxxCxDBCBABxBxBAxxAAxADADCBCABBCDxBBABBCBCCBCxDxCCACCDxBBDCxBDDAACxACDCAABADCABACCDxABADDxCCDxCACDCDBAADxBCAxABxDBxDBABxDDADBCxCxABBBBBABxDBBDDxCBADBDCADDCCDDCDBDBCCCDDDCCDCDADCABDACBAxDxCDBABBCBDDBBBDCBDBCBBADxxCDDDAABABADAADCxAADBADxxBCCADBCCCCxxADBCCADAADADCBABAxCxBACBxADCBBCCCCCDAxAxABBAxxDDBDxxxBADAxBxADADADCxDxxAxxCBABCDCxBADBCCBCDxAAxDxCCAxCCDCCBDBBDBCCBABAxDDDxAADDDBxCxCxCDBCxxxCBDDxxxBBADBDDADDBACxxxxBxAABxCxCDBBCACCDDCCCxDCAxCCBxDCCDDDABBCDDxDBxAAxDDCCCACDxBCAAxxDxxBBABBACCABACBxBDABADCCABxCCAAxBAABDDCADBACDxCADADBDAxBBDBxCxxAxAxDxBBCxAxBAAACxBBCCDCxDBCDACDxBCxAAADADBBAAADDxAAxDADACxDAAAADxAADCxCCDCAADAABABBxxDCDDBACAxxBABDBBBxBxBxABxBxDDxBDBBAADBxxDDxBDABxABxBABBBDADDCABBxAADBDACxBAABABDCCDDACBxCxxBxDBCCxAxCAxBCAACxDCCCBBCCBBCACDAxCxxDABxxAxDABxDDBCCDABDAxADACxxDCAADABCCCBBAxAxBxCADxABDCBDACCBABABxBxAxDBCBACCDxDBBDBCABCDxxxAxAADBBBxBAAxxBxADAxACAxBBBxBCDxAxDDCCxDxBCABBxBBAxDxCADxBxBAAxxBxBDAAAxCABCxDBCBBCBBAxxCBBDDxxCABDxDAADxCAACxAABACDACACDBDBABxACDADxCCCABDCAxCCDAxABDABBxACAxCCBDDxADCCADCxBCxDAxxxAxCCAxxxDADACxxBCBCxDABCBBAxBDBxxCCAxxCxCCDBCABDxBADDxBxACDxAxCxBDBAxxCxDBDDxABDDCCABCxCxxBBxAADCxBCDCABCAxDxxCxxCBDACACAACxDCBCDxCDACACDBCxABDACDxBBDABCCCDDCDCBAxAAxDBDxDDDxDxACBAxxDBADDxBBBACBBBxABAACDBxDxDDBxABxADBxACABBxCBACAxAAAxBxCABCCxABBBCxDAxCDBADAxDDDCDCAAxAABDCCBBxxBxxBBBDxxADxACBxxAxxBBxCxCxBCxCACBxCDBBCDDDAxDDBxCCxxBCDBxAxAxCDxDxDCADCADCxxxAxCxCCxxAxAAxDDAAAADxxDADxAxBADxxADCBDxxDDBADDDBBCxDDxDxDDCDAxDDAxBDDBAAAAxCBCBDDBBDCCxCADDxCCDxADBxAxDCCBAADCBDBDADBxAxACBAxxDDABDxABCCDCxDDBAADDADADAxxAxCxxCCDABDBBDxBDxxCBxADxxDADCBxCxxCDDABCCxDABBDDCxxDxxxADDAABAABDCABDCBxABBxACBCxDBxBBDABDABCAxCBAAADAAxxADxDBCDABBBBxBBxBCAxBDxBDCBxBDCCxCDCBxCABAxADCBDBDBCCBCCBBCACBxxCxBDBDCAxAxxCADxxxCACCABDBCBABDxBCDACCxxCDADxBBCxBCCBxDxDDBxBAxBBAAAxAABBDCxxACBBBCxABBABBCxACBxCABBCADCCADAxADBAxDCADBDDCACCxCBDxABCDDBxCxBBAxABDCCADBCBBBxBxCxADACCxxACDAxxxCACDBDBBDACCDBBBDxCCBDBDxBDDBxBACADBxABBDCBBADDBDxCAxxCCBBCDxCxCACABxBCCBxBCBBxDABxCDDxCACCDDABxCADxCBBDDBBxADCDBCBBxxCDxCCADxDxxxCCxBCBxxBABxACBDDCCADxABDDxxCDAADDDCDCCDADxCADBADADDBBCDAxABBDxAxDDxCAxxBBBxxxBCxDCxABxCDBADAACxxDBBDxDDBDCxADDxDCDBDDxxAxACCAxDBxBDxDCxBAABABAAAxDABDDCABCDBBCDxxDBCBxDABACxBDxCDBBDxBDBDCCCAABBAAAACCDBxDAABCCACDDADDABxCAxDBBxxAxAACABxAABCxxxBDAxCCBxCCBAADxCBACBBCCBxAxCDDABBDxDBDBxDBCxDACBBxAABBABCBDBBDDBABDAxBDAABAxCCCCDCDDCACADxDCAxBDxCxCBxBxDDxACBCCAxAxDCBBxxxCCDCCxDAABBxBBDADACBCBBBCBxDDCxBACDABxADDDDBBxAAxBCABCBxBAADCBBACABADABxCBCAxABCACACCBxDAACDDxADDABxBDDDDCDDCCDDBDDACAxBBDCxCCBDDAxDCCCxBBCDACADBxBADxDDBxCDDAABDDxADAACBxCxDxxCCAAxCACDCABDCCBxDBBDCABCDDxBBBABxDBDDDCBDxBBBCBAxCADADCxAxBBADCxABxCDDDDCADxCBCBxAxCCAxBBxCDDDDxCBDDAxAxxBxBDAAACDxBxCABADADBBxxxDCDCBCBDDCCBBDBxxDxAABADDxBCABxxCAxABAADDxDDACAABBBCCBDAADABDDCCBxDADBBDACBxCAABCxCDBCAxADDCABDCxADBDDDBAxBDACBxBBxBxBADCDAADACCBBDxDABxCAAxCxCCCCCDCDCBxxADDxBADACxBDxBDAxCxACDADBCBDCCCDDxxCDADDxCxACAAADBDCDxBADAxCABAxxAxADDxDxBxCCBBACADxBBDBDDABCBCxCxBBDxBADDBAxDDCDxxABADCDBCBBCCCDDDBBACCxDAACDDAAAxACxxCxxACxBxDDxBxCBAxxCBBABCxAAxBABDACBxBxxCxDAxxCxCABDBBBxCDCCDBABDDCxBCBDCDCAxxBCxBCBBACADAxBABBCCCACAxxCDCBCDDxCBCCBxDxCCDADxxBCBADBDDCACABxBxCBCAAxDCDBABBABBBBDxxxBDBBxAxDBBxCxDABAAxDDxCxCxDxBACBBxDxADDACACDCAAAxxBCDBCAADCBBCBCxDBBCxBCCDDxDCxBBxCAAAAABACBABCBACBDBDxBDDAAxAAxCCBDACxBDBDABADBBADxBCxBBDAADABBDBABCAABxCCDABxAADCADDxABCBBAADBBCBCADCCxBBxAxBBDAAxDDBBxDADCCBDACCCDCADBDADxBCCxxDAxBABACCCxBACxDBBADxCxACBCCACBBABACBBDAxBDDBADCDDAxCAACBBABDABxDCBBxCDAxDACxxDAAAAAAACCxACCAAACBDDBxDxDxBADDADADADxDAxxBBBBADCBBADBCCAAACxBBACBBxBxxBAABCxxxAxCDDCAxxBDACxCADBBxDADCDCCABBxDDBBCBBAADACCxCBxxBADBBxCCBDDxAACDBxBADADxBBBCxxDAxDBBCABAB"

def fight(partNum):
    enemySequence = f"Part{partNum}"
    potions = 0
    pairs = [globals()[enemySequence][i:i+partNum] for i in range(0, len(globals()[enemySequence]), partNum)]
    for pair in pairs:
        enemies = sum(1 for enemy in pair if enemy in PotionChart)
        potions += (enemies-1)*enemies
        for enemy in pair:
            if enemy in PotionChart:
                potions += PotionChart[enemy]
    return potions

for partNum in range(1,4):
    print(fight(partNum))


# ----------------------------------------------- LEGACY CODE BELOW ------------------------------------------------------------

# def partOne(potions):
#     for enemy in Part1:
#         potions += PotionChart[enemy]
#     return potions

# def partTwo(potions):
#     pairs = [Part2[i:i+2] for i in range(0, len(Part2), 2)]
#     for pair in pairs:
#         enemies = sum(1 for enemy in pair if enemy in PotionChart)
#         potions += (enemies-1)*enemies
#         for enemy in pair:
#             if enemy in PotionChart:
#                 potions += PotionChart[enemy]
#     return potions


# def partThree(potions):
#     pairs = [Part3[i:i+3] for i in range(0, len(Part3), 3)]
#     for pair in pairs:
#         enemies = sum(1 for enemy in pair if enemy in PotionChart)
#         potions += (enemies-1)*enemies
#         for enemy in pair:
#             if enemy in PotionChart:
#                 potions += PotionChart[enemy]
#     return potions

# print(partOne(0))
# print(partTwo(0))
# print(partThree(0))