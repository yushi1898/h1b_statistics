import filesortingfunc as fid

fp = open('../input/h1b_input.csv')


data_state = fid.gencolumn(fp,'WORKSITE_STATE')
data_OCCUPATION = fid.gencolumn(fp,'SOC_NAME')

state_cat = fid.categorize_2(data_state)
occupation_cat = fid.categorize_2(data_OCCUPATION)

state_sort = fid.merge_sort(state_cat)
occupation_sort = fid.merge_sort(occupation_cat)

for i in range(len(occupation_sort)):
    occupation_sort[i][0] = occupation_sort[i][0].strip('"')


state_top_10 = fid.picktop(state_sort,10)
occupation_top_10 = fid.picktop(occupation_sort,10)
   
fp_state = open('../output/top_10_states.txt','w')
fp_state.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
for item in state_top_10:
    fp_state.write("%s;%d;%.1f%%\n" % (item[0],item[1],item[2]*100))

fp_state.close()


fp_occupation = open('../output/top_10_occupations.txt','w')
fp_occupation.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
for item in occupation_top_10:
    fp_occupation.write("%s;%d;%.1f%%\n" % (item[0],item[1],item[2]*100))

fp_occupation.close()