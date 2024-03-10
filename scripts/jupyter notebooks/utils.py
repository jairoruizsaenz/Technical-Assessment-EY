import pandas as pd


def build_variables_dict(variables_list):
    dict={}
    highschool_variables_mapping=pd.read_excel('../../other_files/high_school_variables_mapping.xlsx')
    highschool_variables_mapping=highschool_variables_mapping.fillna('NULL')
    variables_dict=highschool_variables_mapping.set_index('VARIABLE').to_dict(orient='index')
    
    for var in variables_list:
        try:        
            variable_dict=variables_dict.get(var)
            MAIN_KEY=variable_dict['MAIN_KEY']
            MAIN_VALUE=variable_dict['MAIN_VALUE']        
            RENAME=variable_dict['RENAME']
            
            OPT1_KEY=variable_dict['OPT1_KEY']
            OPT1_VALUE=variable_dict['OPT1_VALUE']
            
            OPT2_KEY=variable_dict['OPT2_KEY']
            OPT2_VALUE=variable_dict['OPT2_VALUE']
            
            OPT3_KEY=variable_dict['OPT3_KEY']
            OPT3_VALUE=variable_dict['OPT3_VALUE']

            temp={'main':{MAIN_KEY:MAIN_VALUE}}

            if OPT1_KEY!='NULL':
                temp.update({OPT1_KEY:OPT1_VALUE})
            
            if OPT2_KEY!='NULL':
                temp.update({OPT2_KEY:OPT2_VALUE})

            if OPT3_KEY!='NULL':
                temp.update({OPT3_KEY:OPT3_VALUE})
            
            temp.update({'rename':RENAME})
            dict.update({var:temp})
        except:
            print(f'variable {var} was not found!')
    
    return dict


def get_plotly_df(data_df=None, variables_dict=None, group_by_dict={'PERIODO':'year', 'NOMBRE_INS_PLA':'institution'}):
    group_by_list=list(group_by_dict.keys())
    dfs=[]
    df_combined=None
    temp_df=None
    for key, value in variables_dict.items():
        for sub_key, sub_value in value.items():
            if sub_key=='main':
                for main_key, main_value in sub_value.items():
                    temp_df=data_df.groupby(group_by_list)[key].sum().reset_index()
                    temp_df[main_key]=main_value
            elif sub_key!='rename':
                temp_df[sub_key]=sub_value
            elif sub_key=='rename':
                temp_df.rename(columns={key: sub_value}, inplace=True)
                temp_df.rename(columns=group_by_dict, inplace=True)
            dfs.append(temp_df)
        
    df_combined=pd.concat(dfs, ignore_index=True)    
    
    try:
        df_combined=df_combined.sort_values(by=['year', 'institution'])
    except:
        pass

    df_combined.drop_duplicates(inplace=True)
    return df_combined


def update_fig_layout(fig, level=None, title=None, width=1000, height=600):
    fig.update_layout(title_x=0.5, title_font_size = 22, font_size=12, width=width,height=height)
    fig.write_image(f"../../results/graphs/{level}__{title}.png")
    return fig