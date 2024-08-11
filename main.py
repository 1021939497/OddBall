import numpy as np
import networkx as nx
from Load_Data import *
from Oddball import *

def main():
    lof = 0
    anomaly_type = 0
    #Input a weighted undirected graph which format is 'a b weight'
    input_path = args.input
    output_path = args.output
    G = load_data(input_path)
    featureDict = get_feature(G)
    if lof == 0:
        if anomaly_type == 1:
            star_or_clique_score = star_or_clique(featureDict)
            star_or_clique_array = []
            for key in star_or_clique_score.keys():
                star_or_clique_array.append(np.array([key, star_or_clique_score[key]]))
            star_or_clique_array = np.array(star_or_clique_array)
            star_or_clique_array = star_or_clique_array[star_or_clique_array[:, 1].argsort()[::-1]]  # Sort by score from large to small
              for key in star_or_clique_array:
                  print(str(int(key[0])) + ' ' + str(key[1]))
        elif anomaly_type == 2:
            heavy_vicinity_score = heavy_vicinity(featureDict)
            heavy_vicinity_array = []
            for key in heavy_vicinity_score.keys():
                heavy_vicinity_array.append(np.array([key, heavy_vicinity_score[key]]))
            heavy_vicinity_array = np.array(heavy_vicinity_array)
            heavy_vicinity_array = heavy_vicinity_array[heavy_vicinity_array[:, 1].argsort()[::-1]]  # Sort by score from large to small

        elif anomaly_type == 3:
            dominant_edge_score = dominant_edge(featureDict)
            dominant_edge_array = []
            for key in dominant_edge_score.keys():
                dominant_edge_array.append(np.array([key, dominant_edge_score[key]]))
            dominant_edge_array = np.array(dominant_edge_array)
            dominant_edge_array = dominant_edge_array[dominant_edge_array[:, 1].argsort()[::-1]]  # Sort by score from large to small

        else:
            print('parameter error!')
    elif lof == 1:
        if anomaly_type == 1:
            star_or_clique_withLOF_score = star_or_clique_withLOF(featureDict)
            star_or_clique_withLOF_array = []
            for key in star_or_clique_withLOF_score.keys():
                star_or_clique_withLOF_array.append(np.array([key, star_or_clique_withLOF_score[key]]))
            star_or_clique_withLOF_array = np.array(star_or_clique_withLOF_array)
            star_or_clique_withLOF_array = star_or_clique_withLOF_array[star_or_clique_withLOF_array[:, 1].argsort()[::-1]]  # Sort by score from large to small

        elif anomaly_type == 2:
            heavy_vicinity_withLOF_score = heavy_vicinity_withLOF(featureDict)
            heavy_vicinity_withLOF_array = []
            for key in heavy_vicinity_withLOF_score.keys():
                heavy_vicinity_withLOF_array.append(np.array([key, heavy_vicinity_withLOF_score[key]]))
            heavy_vicinity_withLOF_array = np.array(heavy_vicinity_withLOF_array)
            heavy_vicinity_withLOF_array = heavy_vicinity_withLOF_array[heavy_vicinity_withLOF_array[:, 1].argsort()[::-1]]  # Sort by score from large to small

        elif anomaly_type == 3:
            dominant_edge_withLOF_score = dominant_edge_withLOF(featureDict)
            dominant_edge_withLOF_array = []
            for key in dominant_edge_withLOF_score.keys():
                dominant_edge_withLOF_array.append(np.array([key, dominant_edge_withLOF_score[key]]))
            dominant_edge_withLOF_array = np.array(dominant_edge_withLOF_array)
            dominant_edge_withLOF_array = dominant_edge_withLOF_array[dominant_edge_withLOF_array[:, 1].argsort()[::-1]]  # Sort by score from large to small

        else:
            print('parameter error!')
    else:
        print('parameter error!')

if __name__ == "__main__":
    main()
