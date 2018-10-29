import filesortingfunc as fid

#open input file
fp = open('./input/h1b_input.csv')

#extract columns with a given name
data_state = fid.gencolumn(fp,'WORKSITE_STATE')
data_OCCUPATION = fid.gencolumn(fp,'SOC_NAME')

#categorize each column and count how many each category appear
state_cat = fid.categorize(data_state)
occupation_cat = fid.categorize(data_OCCUPATION)


#sort category based on its appeared frequency
state_sort = fid.merge_sort(state_cat)
occupation_sort = fid.merge_sort(occupation_cat)


#remove '"' in occupation column
for i in range(len(occupation_sort)):
    occupation_sort[i][0] = occupation_sort[i][0].strip('"')

#select the top 10 items of each column
state_top_10 = fid.picktop(state_sort,10)
occupation_top_10 = fid.picktop(occupation_sort,10)

#write the top 10 states  to file        
fp_state = open('./output/top_10_states.txt','w')
fp_state.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
for item in state_top_10:
    fp_state.write("%s;%d;%.1f%%\n" % (item[0],item[1],item[2]*100))

fp_state.close()

#write the top 10 occupations to file     
fp_occupation = open('./output/top_10_occupations.txt','w')
fp_occupation.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
for item in occupation_top_10:
    fp_occupation.write("%s;%d;%.1f%%\n" % (item[0],item[1],item[2]*100))

fp_occupation.close()