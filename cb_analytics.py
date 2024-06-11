import pandas as pd

def cb_filterer( cb_data_all: pd.DataFrame, filters_dict: dict) -> pd.DataFrame:
    filtered_df = pd.DataFrame()
    for filter_code in filters_dict.keys():
        if filter_code == 'p':
            df_p = cb_data_all[ cb_data_all["acceleration"] >= filters_dict[filter_code]]\
                        .loc[:, ["name", "acceleration"]]
            filtered_df = pd.concat([filtered_df, df_p], axis = 1)
            filtered_df.rename( columns = {"name": "Names"}, inplace = True)
        if filter_code == 'c':
            df_c = cb_data_all[ cb_data_all["composure"] >= filters_dict[filter_code]]\
                        .loc[:, ["name", "composure"]]
            filtered_df = pd.concat([filtered_df, df_c], axis = 1)
            filtered_df.rename( columns = {"name": "name_c"}, inplace = True)
        if filter_code == 's':
            df_s = cb_data_all[ cb_data_all["strength"] >= filters_dict[filter_code]]\
                        .loc[:, ["name", "strength"]]
            filtered_df = pd.concat([filtered_df, df_s], axis = 1)
            filtered_df.rename( columns = {"name": "name_s"}, inplace = True)
        if filter_code == 'r':
            df_r = cb_data_all[ cb_data_all["reaction"] >= filters_dict[filter_code]]\
                        .loc[:, ["name", "reaction"]]
            filtered_df = pd.concat([filtered_df, df_r], axis = 1)
            filtered_df.rename( columns = {"name": "name_r"}, inplace = True)
        if filter_code == 'agr':
            df_agr = cb_data_all[ cb_data_all["agression"] >= filters_dict[filter_code]]\
                        .loc[:, ["name", "agression"]]
            filtered_df = pd.concat([filtered_df, df_agr], axis = 1)
            filtered_df.rename( columns = {"name": "name_agr"}, inplace = True)
        if filter_code == 'b':
            df_b = cb_data_all[ cb_data_all["balance"] >= filters_dict[filter_code]]\
                        .loc[:, ["name", "balance"]]
            filtered_df = pd.concat([filtered_df, df_b], axis = 1)
            filtered_df.rename( columns = {"name": "name_b"}, inplace = True)
        if filter_code == 'agi':
            df_agi = cb_data_all[ cb_data_all["agility"] >= filters_dict[filter_code]]\
                        .loc[:, ["name", "agility"]]
            filtered_df = pd.concat([filtered_df, df_agi], axis = 1)
            filtered_df.rename( columns = {"name": "name_agi"}, inplace = True)
        # if filter_code == 't':
        #     df_t = cb_data_all[(cb_data_all["trait_1"].notnull()) & \
        #                 (cb_data_all["trait_2"].notnull()) & (cb_data_all["trait_3"].notnull())]\
        #                     .loc[:, ["name", "trait_1", "trait_2", "trait_3"]]
        #     filtered_df = pd.concat([filtered_df, df_t], axis = 1)
        #     filtered_df.rename( columns = {"name": "name_t"}, inplace = True)
    filtered_df.Names.fillna( filtered_df.name_r, inplace= True)
    filtered_df.Names.fillna( filtered_df.name_s, inplace= True)
    filtered_df.Names.fillna( filtered_df.name_c, inplace= True)
    filtered_df.Names.fillna( filtered_df.name_b, inplace= True)
    filtered_df.Names.fillna( filtered_df.name_agr, inplace= True)
    filtered_df.Names.fillna( filtered_df.name_agi, inplace= True)
    filtered_df.drop(["name_r", "name_agr", "name_s", "name_c", "name_b", "name_agi"], axis = 1, inplace = True)
        # if len(filters_dict.keys()) > 1:
    return filtered_df

if __name__ == "__main__":

    # Goal keepers analytics
    cb_data = pd.read_csv( "cb_data.csv")# Read the CSV data for 20 goalkeepers
    good_cbs = cb_filterer(cb_data, {'p': 70, 'c': 75, 's': 85, 'r': 85, 'agr': 85, 'b': 70, 'agi': 70})
    good_cbs = good_cbs.merge( cb_data[["name", "price", "nation", "league", "team"]], left_on="Names", right_on="name", how="left")
    good_cbs.drop(["name"], axis = 1, inplace= True)
    
    #Uncomment below line to see analysis result in the good goalkeepers file
    good_cbs.to_csv("good_cbs.csv")

    # Final list after analyzing the above results are
    # good_cbs_list = []
    # final_gks = cb_data[ cb_data["name"].isin(good_cbs_list)]
    # final_gks.to_csv("good_cbs.csv")