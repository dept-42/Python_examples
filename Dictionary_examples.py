#Dictionary Exampes
entry_number = 0

#1. declare an empty dictionary with 'my_dict = {}'then add values'
entry_number += 1
print(f"{entry_number}. declare an empty dictionary then add values")
print()
my_dict = {}
print("my_dict")
print(f"my_dict {my_dict}")
print()
print("add key : value pairs to my_dict")
my_dict['first name'] = 'Wayne'
my_dict['last name'] = 'Mitchell'
print(my_dict)
print()

#2. define a dictionary. NOTE no final comma!'
entry_number += 1
print(f"{entry_number}. define a dictionary. NOTE no final comma!")
print()
codon_table = {
    'ttt' : 'F', 'ttc' : 'F',

    'tta' : 'L', 'ttg' : 'L', 'ctt' : 'L', 'ctc' : 'L', 'cta' : 'L', 'ctg' : 'L',

    'att' : 'I', 'atc' : 'I', 'ata' : 'I',

    'atg' : 'M',

    'gtt' : 'V', 'gtc' : 'V', 'gta' : 'V', 'gtg' : 'V',

    'tct' : 'S', 'tcc' : 'S', 'tca' : 'S', 'tcg' : 'S',

    'cct' : 'P', 'ccc' : 'P', 'cca' : 'P', 'ccg' : 'P',
    
    'act' : 'T', 'acc' : 'T', 'aca' : 'T', 'acg' : 'T',

    'gct' : 'A', 'gcc' : 'A', 'gca' : 'A','gcg' : 'A',

    'tat' : 'Y','tac' : 'Y',

    'taa' : 'stop','tag' : 'stop',

    'cat' : 'H', 'cac' : 'H',

    'caa' : 'Q','cag' : 'Q',

    'aat' : 'N','aac' : 'N',

    'aaa' : 'K','aag' : 'K',

    'gat' : 'D','gac' : 'D',

    'gaa' : 'E', 'gag' : 'E',

    'tgt' : 'C','tgc' : 'C',

    'tga' : 'stop',

    'tgg' : 'W',

    'cgt' : 'R','cgc' : 'R','cga' : 'R','cgg' : 'R',

    'agt' : 'S','agc' : 'S',

    'aga' : 'R','agg' : 'R',

    'ggt' : 'G','ggc' : 'G','gga' : 'G','ggg' : 'G'
}
print(codon_table)
print()
print("-" * 50)
print()

#3. access and print one value of a dictionary by key 'this_dict['key']'
entry_number += 1
print(f"{entry_number}. access and print one value of a dictionary by key \
      'this_dict['key']'")
print()
print(f"the amino acid encoded by 'atg': {codon_table['atg']}")
print()
print("-" * 50)
print()

#4. loop through a dictionary with 'this_dict.items()'
entry_number += 1
print(f"{entry_number}. loop through a dictionary with 'this_dict.items()'!")
print()
for codon, amino_acid in codon_table.items():
    print(f"codon: {codon} -> aa: {amino_acid}")
print()
print("-" * 50)
print()

#5. loop through a dictionary to get keys with 'this_dict.keys()''
entry_number += 1
print(f"{entry_number}. loop through a dictionary to get keys with \
      'this_dict.keys()")
print()
for codon in codon_table.keys():
    print(f"codon: {codon}")
print()
print("-" * 50)
print()

#6. get values from a dictionatiory with 'this_dict.values(); make a list of 
    # unique amino acids and print
entry_number += 1
print(f"{entry_number}. get values from a dictionary with 'this_dict.values()'") 
amino_acids = list()
for amino_acid in codon_table.values():
    print(f"amino_ acid: {amino_acid}")
    if (not amino_acid in amino_acids and amino_acid != "stop"):
        amino_acids.append(amino_acid)
print()
print(f"There are {len(amino_acids)} amino acids")
print()
print("-" * 50)
print()

#7. create a dictionary, then add key : value pair to existing dictionary'
# with 'this_dict['key'] = value'
entry_number += 1
print(f"{entry_number}. create a dictionary, then add key : value pair to \
      existing dictionary with 'this_dict['key'] = value'")
print()
molecular_weight = {
	"A" :	"89",
	"R" :	"174",
	"N" :	"132",
	"D" :	"133",
	"C" :	"121",
	"Q" :	"146",
	"E" :	"147",
	"G" :	"75",
	"H" :	"155",
	"I" :	"131",
	"L" :	"131",
	"K" :	"146",
	"M" :	"149",
	"F" :	"165",
	"P" :	"115",
	"S" :	"105",
	"T" :	"119",
	"W" :	"204",
	"Y" :	"181",
	"V" :	"117"
	}
print(molecular_weight)
print()
print(f"Add a key value pair to 'molecular_weight'")
molecular_weight['NaCL'] = 58.44
print(molecular_weight)
print("-" * 50)
print()

#8. use a dictionary to define state (or a record), then update state
entry_number += 1
print(f"{entry_number}. use a dictionary to define state, then update state \
      then update state")
print()
Restaurant_State = {
	"Diner" : {
	    "Cook_count" :	3,
        "Waitstaff" : 5,
	    "Menu" :	["Roast Beef", "Green Beans", "Rice", "Salad"]
    },
    "Lunch" : {
	    "Cook_count" :	3,
        "Waitstaff" : 5,
	    "Menu" :	["Tuna Sandwhich", "Chips", "Dill Pickle"]
    },
    "Breakfast" : {
	    "Cook_count" :	1,
        "Waitstaff" : 2,
	    "Menu" :	["Eggs", "Toast", "Bacon", "Coffee"]
    }
}
print(Restaurant_State)
print()
print("Change the Lunch menu to '[\"Cheesburger\", \"Fries\"]'")
Restaurant_State[ "Lunch"]["Menu"] = ["Cheesburger", "Fries"]
print(Restaurant_State["Lunch"])
print()
print("-" * 50)
print()