import pandas as pd

def gk_filterer( gk_data_all: pd.DataFrame, filters_dict: dict) -> pd.DataFrame:
    filtered_df = pd.DataFrame()
    for filter_code in filters_dict.keys():
        if filter_code == 'h':
            df_h = gk_data_all[ gk_data_all["height"] >= filters_dict[filter_code]]\
                        .loc[:, ["name", "height"]]
            filtered_df = pd.concat([filtered_df, df_h], axis = 1)
            filtered_df.rename( columns = {"name": "Names"}, inplace = True)
        if filter_code == 'r':
            df_r = gk_data_all[ gk_data_all["reflex"] >= filters_dict[filter_code]]\
                        .loc[:, ["name", "reflex"]]
            filtered_df = pd.concat([filtered_df, df_r], axis = 1)
            filtered_df.rename( columns = {"name": "name_r"}, inplace = True)
        if filter_code == 'd':
            df_d = gk_data_all[ gk_data_all["diving"] >= filters_dict[filter_code]]\
                        .loc[:, ["name", "diving"]]
            filtered_df = pd.concat([filtered_df, df_d], axis = 1)
            filtered_df.rename( columns = {"name": "name_d"}, inplace = True)
        if filter_code == 'p':
            df_p = gk_data_all[ gk_data_all["pos"] >= filters_dict[filter_code]]\
                        .loc[:, ["name", "pos"]]
            filtered_df = pd.concat([filtered_df, df_p], axis = 1)
            filtered_df.rename( columns = {"name": "name_p"}, inplace = True)
        if filter_code == 't':
            df_t = gk_data_all[(gk_data_all["trait_1"].notnull()) & \
                        (gk_data_all["trait_2"].notnull()) & (gk_data_all["trait_3"].notnull())]\
                            .loc[:, ["name", "trait_1", "trait_2", "trait_3"]]
            filtered_df = pd.concat([filtered_df, df_t], axis = 1)
            filtered_df.rename( columns = {"name": "name_t"}, inplace = True)
    filtered_df.Names.fillna( filtered_df.name_r, inplace= True)
    filtered_df.Names.fillna( filtered_df.name_d, inplace= True)
    filtered_df.Names.fillna( filtered_df.name_p, inplace= True)
    filtered_df.Names.fillna( filtered_df.name_t, inplace= True)
    filtered_df.drop(["name_r", "name_p", "name_d", "name_t"], axis = 1, inplace = True)
        # if len(filters_dict.keys()) > 1:
    return filtered_df

if __name__ == "__main__":

    # Goal keepers analytics
    gk_data = pd.read_csv( "gk_data.csv")# Read the CSV data for 20 goalkeepers
    good_keepers = gk_filterer(gk_data, {'h': 190, 't': 0, 'r': 85, 'd': 85, 'p': 85})
    good_keepers = good_keepers.merge( gk_data[["name", "price", "nation", "league", "team"]], left_on="Names", right_on="name", how="left")
    good_keepers.drop(["name"], axis = 1, inplace= True)
    
    #Uncomment below line to see analysis result in the good goalkeepers file
    #good_keepers.to_csv("good_keepers.csv")

    # Final list after analyzing the above results are
    good_keeps_list = ["Court", "Allison", "Don", "Mike", "Kobel", "sczzcesny", "Casteels", "Alex Romiro", "Stegen"]
    final_gks = gk_data[ gk_data["name"].isin(good_keeps_list)]
    final_gks.to_csv("good_keepers.csv")
