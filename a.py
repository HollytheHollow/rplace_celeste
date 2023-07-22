https://github.com/HollytheHollow/rplace_celeste/blob/main/madeline_and_badeline.json
link = "https://github.com/knightlab-analyses/qurro-mackerel-analysis/blob/master/AnalysisOutput/qurro-plot.qzv"

# note: this will break if a repo/organization or subfolder is named "blob" -- would be ideal to use a fancy regex
# to be more precise here
print(link.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/"))

# example output link:
# https://raw.githubusercontent.com/knightlab-analyses/qurro-mackerel-analysis/master/AnalysisOutput/qurro-plot.qzv
