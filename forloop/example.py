import forloop_core


fc=forloop_core.ForloopClient(url="http://127.0.0.1:5000")

nodes=fc.get_nodes("pipeline1.flpl")

analyzed_data=fc.analyze_data("train.csv")

#cleaned_data=fc.clean_data("train.csv")

print(nodes)