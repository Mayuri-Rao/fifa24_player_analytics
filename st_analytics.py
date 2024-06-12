import pandas as pd

def cb_filterer( st_data_all: pd.DataFrame, filters_dict: dict) -> pd.DataFrame:
    filtered_df = pd.DataFrame()
    for filter_code in filters_dict.keys():
        if filter_code == 'p':
            df_p = st_data_all[ st_data_all["pos"] >= filters_dict[filter_code]]\
                        .loc[:, ["name", "pos"]]
            filtered_df = pd.concat([filtered_df, df_p], axis = 1)
            filtered_df.rename( columns = {"name": "Names"}, inplace = True)
        if filter_code == 'f':
            df_f = st_data_all[ st_data_all["finish"] >= filters_dict[filter_code]]\
                        .loc[:, ["name", "finish"]]
            filtered_df = pd.concat([filtered_df, df_f], axis = 1)
            filtered_df.rename( columns = {"name": "name_f"}, inplace = True)
        if filter_code == 's':
            df_s = st_data_all[ st_data_all["sprint"] >= filters_dict[filter_code]]\
                        .loc[:, ["name", "sprint"]]
            filtered_df = pd.concat([filtered_df, df_s], axis = 1)
            filtered_df.rename( columns = {"name": "name_s"}, inplace = True)
        if filter_code == 'h':
            df_h = st_data_all[ st_data_all["heading"] >= filters_dict[filter_code]]\
                        .loc[:, ["name", "heading"]]
            filtered_df = pd.concat([filtered_df, df_h], axis = 1)
            filtered_df.rename( columns = {"name": "name_h"}, inplace = True)
        if filter_code == 'agr':
            df_agr = st_data_all[ st_data_all["aggression"] >= filters_dict[filter_code]]\
                        .loc[:, ["name", "aggression"]]
            filtered_df = pd.concat([filtered_df, df_agr], axis = 1)
            filtered_df.rename( columns = {"name": "name_agr"}, inplace = True)
        if filter_code == 'b':
            df_b = st_data_all[ st_data_all["balance"] >= filters_dict[filter_code]]\
                        .loc[:, ["name", "balance"]]
            filtered_df = pd.concat([filtered_df, df_b], axis = 1)
            filtered_df.rename( columns = {"name": "name_b"}, inplace = True)
        if filter_code == 'acl':
            df_acl = st_data_all[ st_data_all["acceleration"] >= filters_dict[filter_code]]\
                        .loc[:, ["name", "acceleration"]]
            filtered_df = pd.concat([filtered_df, df_acl], axis = 1)
            filtered_df.rename( columns = {"name": "name_acl"}, inplace = True)
        # if filter_code == 't':
        #     df_t = st_data_all[(st_data_all["trait_1"].notnull()) & \
        #                 (st_data_all["trait_2"].notnull()) & (st_data_all["trait_3"].notnull())]\
        #                     .loc[:, ["name", "trait_1", "trait_2", "trait_3"]]
        #     filtered_df = pd.concat([filtered_df, df_t], axis = 1)
        #     filtered_df.rename( columns = {"name": "name_t"}, inplace = True)
    filtered_df.Names.fillna( filtered_df.name_h, inplace= True)
    filtered_df.Names.fillna( filtered_df.name_s, inplace= True)
    filtered_df.Names.fillna( filtered_df.name_f, inplace= True)
    filtered_df.Names.fillna( filtered_df.name_b, inplace= True)
    filtered_df.Names.fillna( filtered_df.name_agr, inplace= True)
    filtered_df.Names.fillna( filtered_df.name_acl, inplace= True)
    filtered_df.drop(["name_h", "name_agr", "name_s", "name_b", "name_f", "name_acl"], axis = 1, inplace = True)
        # if len(filters_dict.keys()) > 1:
    return filtered_df

if __name__ == "__main__":

    # Goal keepers analytics
    st_data = pd.read_csv( "st_data.csv")# Read the CSV data for 20 goalkeepers
    good_sts = cb_filterer(st_data, {'p': 85, 'acl': 75, 's': 75, 'f': 85, 'h': 80, 'agr': 70, 'b': 70})
    good_sts = good_sts.merge( st_data[["name", "price", "nation", "league", "team"]], left_on="Names", right_on="name", how="left")
    good_sts.drop(["name"], axis = 1, inplace= True)
    
    #Uncomment below line to see analysis result in the good goalkeepers file
    good_sts.to_csv("good_sts.csv")

    # Final list after analyzing the above results are
    # good_sts_list = []
    # final_gks = st_data[ st_data["name"].isin(good_sts_list)]
    # final_gks.to_csv("good_sts.csv")