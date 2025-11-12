# Koi Johnson
# BRIEF: Analyze K-drama data
# START: 10/22/25 
# UPDATED: 11/12/25

# IMPORTS
import random

# FUNCTIONS

# Info Functions
# title
def titleInfo(idx, info, title, synopsis, screenwriter, director, genre_list, tag_list, cast_list, episodes, air_time, duration, restriction, network_list, popularity):
    if info == 1:
        return synopsis[idx]
    elif info == 2:
        return "Screenwriter: " + screenwriter[idx] + " " + "Director: " + director[idx]
    elif info == 3:
        return genre_list[idx]
    elif info == 4:
        return tag_list[idx]
    elif info == 5:
        return cast_list[idx]
    elif info == 6:
        return episodes[idx]
    elif info == 7:
        return air_time[idx]
    elif info == 8:
        return duration[idx]
    elif info == 9:
        return restriction[idx]
    elif info == 10:
        return popularity[idx]
    elif info == 11:
        return network_list[idx]
    else:
        with open(f"{title}_INFORMATION.txt", "w") as info_file:
            info_file.write(f"{title} \nSYNOPSIS: {synopsis[idx]} \nCREDITS:\n   Screenwriter: {screenwriter[idx]}\n   Director: {director[idx]}\nGENRE(S): {genre_list[idx]}\nTAGS: {tag_list[idx]}\nCAST: {cast_list[idx]}\nEPISODES: {episodes[idx]}\nAIRED: {air_time[idx]}\nDURATION: {duration[idx]}\nRESTRICTION: {restriction[idx]}\nSTREAMING: {network_list[idx]}\nPOPULARITY: {popularity[idx]}")
            print(f"Information stored in {title}_INFORMATION.txt file")
    


# actor
def actorInfo(actor, cast_list, title):
    actor_title = []
    for i in range(len(cast_list)):
        for j in range(len(cast_list[i])):
            if cast_list[i][j] == actor:
                actor_title.append(title[i])
    if len(actor_title) == 0:
        return f"There are no Titles with {actor}."
    else:
        return f"There are {len(actor_title)} Titles with {actor}: \n{actor_title}"



# genre
def genreInfo(genre, genre_list, title):
    genre_title = []
    for i in range(len(genre_list)):
        for j in range(len(genre_list[i])):
            if genre_list[i][j] == genre:
                genre_title.append(title[i])
    if len(genre_title) == 0:
        return f"There are no Titles in {genre}."
    else: 
        return f"There are {len(genre_title)} Titles in {genre}: \n{genre_title}"


# Generate Functions
# genre
def genGenre(list, genres):
    new_list = []
    genre = input("What Genre: ")
    for i in range(len(genres)):
        check = 0
        for j in range(len(genres[i])):
            if genres[i][j] == genre:
                check = 1
        if check == 1:
            new_list.append(list[i])
    return new_list
            
# tag
def genTag(list, tags):
    new_list = []
    tag = input("What Tag: ")
    for i in range(len(tags)):
        check = 0
        for j in range(len(tags[i])):
            if tags[i][j] == tag:
                check = 1
        if check == 1:
            new_list.append(list[i])
    return new_list

# actor
def genActor(list, actors):
    new_list = []
    actor = input("What Actor: ")
    for i in range(len(actors)):
        check = 0
        for j in range(len(actors[i])):
            if actors[i][j] == actor:
                check = 1
        if check == 1:
            new_list.append(list[i])
    return new_list

# episode
def genEpisode(list, episodes):
    exact = int(input(" 1. Less Than \n 2. More Than \n 3. Exact \nRestrictions: "))
    episode = int(input("How many Episodes: "))
    new_list = []
    for i in range(len(episodes)):
        check = 0
        if exact == 1:
            if episodes[i] <= episode:
                check = 1
        elif exact == 2:
            if episodes[i] >= episode:
                check = 1
        else:
            if episodes[i] == episode:
                check = 1
        if check == 1:
            new_list.append(list[i])
    return new_list

# keywords
def genKeyword(list, word, synonyms, synopsis):
    new_list = []
    synopsis_split = []
    for i in range(len(synopsis)):
        split = synopsis[i].split(" ")
        synopsis_split.append(split)
    check1 = 0
    keyword = input("What Keyword: ")
    for i in range(len(word)):
        if word[i] == keyword:
            idx = i
            check1 = 1
            break
    if check1 == 0:
        for i in range(len(synopsis_split)):
            check2 = 0
            for j in range(len(synopsis_split[i])):
                if synopsis_split[i][j] == keyword:
                    check2 = 1
                    break
            if check2 == 1:
                if list[i] not in new_list:
                    new_list.append(list[i])
        return new_list

    else:
        for i in range(len(synonyms[idx])):
            for j in range(len(synopsis_split)):
                check3 = 0
                for k in range(len(synopsis_split[j])):
                    if synopsis_split[j][k] == synonyms[idx][i] or synopsis_split[j][k] == keyword:
                        check3 = 1
                        break
                if check3 == 1:
                    if list[j] not in new_list:
                        new_list.append(list[j])
        return new_list
                    
    

# platform
def genPlatform(list, platforms):
    new_list = []
    platform = input("What Streaming Platform: ")
    for i in range(len(platforms)):
        check = 0
        for j in range(len(platforms[i])):
            if platforms[i][j] == platform:
                check = 1
        if check == 1:
            new_list.append(list[i])
    return new_list

#random
def genRand(list):
    rand_list = []
    count = int(input("Length of Random Generated List: "))
    if count > len(list):
        print("Exceeds Number of Titles")
        return []
    elif count == 0:
        return []
    else:
        for i in range(count):
            choice = random.choice(list)
            rand_list.append(choice)
            list.remove(choice)
        return rand_list
    




# MAIN

if __name__ == "__main__": 

    # UPLOAD DATA
    with open("/Users/emmajohnson/Desktop/Personal Code/kdrama_analysis/kdrama_data.txt", "r") as kdrama_data:

        # ORGANIZE
        title = []
        synopsis = []
        screenwriter = []
        director = []
        genre_list = []
        tag_list = []
        cast_list = []
        episodes = []     # int
        air_time = []      
        duration = []   # int - figure out how to change
        restriction = []
        network_list = []
        popularity = []     # int - get rid of "#"
        next(kdrama_data) # skips first line
        for line in kdrama_data:
            line = line.strip()
            line = line.split("=")
            title.append(line[1])
            synopsis.append(line[2])
            screenwriter.append(line[3])
            director.append(line[4])
            genres = line[5].split(",")
            for i in range(len(genres)):
                new = genres[i].strip(" ")
                genres[i] = new
            genre_list.append(genres)
            tags = line[6].split(",")
            for i in range(len(tags)):
                new = tags[i].strip(" ")
                tags[i] = new 
            tag_list.append(tags)
            cast = line[7].split(",")
            for i in range(len(cast)):
                new = cast[i].strip(" ")
                cast[i] = new
            cast_list.append(cast)
            episodes.append(int(float(line[8])))
            air_time.append(line[9])
            duration.append(line[12])
            restriction.append(line[13])
            networks = line[18].split(",")
            for i in range(len(networks)):
                new = networks[i].strip(" ")
                networks[i] = new
            network_list.append(networks)
            popularity.append((line[16]).strip("#"))


    
    # WELCOME
    print("KDRAMA ANALYSIS PROGRAM")
    option = int(input(" 1. Retrieve Information \n 2. Generate List \n 3. Create Watchlist \nWhat would you like to do: "))

    if option == 1: 
        # Information 
        print("1. Title \n2. Actor \n3. Genre")
        search = input("What would you like to search: ")

        if search == "1":
            name = input("What title: ")
            true = 0
            for i in range(len(title)):
                if title[i] == name:
                    idx = i
                    true = 1
                    break
            if true == 0:
                print("TITLE NOT FOUND")
            else:
                print("1. Synopsis \n2. Credits \n3. Genre(s) \n4. Tags \n5. Cast \n6. Episodes \n7. Air Dates \n8. Duration \n9. Restrictions \n10. Popularity \n11. Where to Watch \n12. ALL")
                info = int(input("What info do you want to know: "))
                print(titleInfo(idx, info, title, synopsis, screenwriter, director, genre_list, tag_list, cast_list, episodes, air_time, duration, restriction, network_list, popularity))

        elif search == "2":
            actor = input("What actor: ")
            print(actorInfo(actor, cast_list, title))
        elif search == "3":
            genre1 = input("What genre: ")
            print(genreInfo(genre1, genre_list, title))
        else: 
            print("That was not an Option. Restart Program.")

    elif option == 2: 
        # LOAD IN THESAURUS
        with open("/Users/emmajohnson/Desktop/Personal Code/kdrama_analysis/WordnetSynonyms.csv", "r") as thesaurus:
            # ORGANIZE
            word = []
            synonym_list = []
            for line in thesaurus:
                line = line.strip()
                line = line.split(",")
                word.append(line[0])
                synonyms = (line[3]).split(";")
                synonym_list.append(synonyms)

        # Generate 
        filters = int(input("How many filters?: ")) 
        rand = 0 # for randomization
        filter_list = []
        for i in range(filters):
            print("Pick your filter")
            print("1. Genre \n2. Tag \n3. Actor \n4. Episode Length \n5. Keyword \n6. Platform \n7. Random")
            generate = int(input("Filter: "))
            if generate == 1:
                filter = genGenre(title, genre_list)
            elif generate == 2:
                filter = genTag(title, tag_list)
            elif generate == 3:
                filter = genActor(title, cast_list)
            elif generate == 4:
                filter = genEpisode(title, episodes)
            elif generate == 5:
                filter = genKeyword(title, word, synonym_list, synopsis)
            elif generate == 6:
                filter = genPlatform(title, network_list)
            elif generate == 7: 
                if filters == 1:
                    filter = genRand(title)
                else: 
                    filter_list.append(1)
                    continue
            else:
                print("That was not an Option... Generating List...")
                break
            if len(filter) == 0:
                print("There are no Titles that fit the Filters.")
                break
            else: 
                filter_list.append(filter)
        
        # Compare filters
        if len(filter_list) == 1:
            generate_list = filter_list
        else: 
            for i in range(len(filter_list)-1):
                generate_list = []
                if filter_list[i+1] == 1:
                    filter_list[0] = genRand(filter_list[0])
                    if len(filter_list) == 2:
                        generate_list = filter_list[0]
                    continue
                for j in range(len(filter_list[0])):
                    for k in range(len(filter_list[i+1])):
                        if filter_list[0][j] == filter_list[i+1][k]:
                            if filter_list[0][j] not in generate_list:
                                generate_list.append(filter_list[0][j])
                filter_list[0] = generate_list

        print("Here's your Generated List!")
        print(generate_list)

        save = int(input(" 1. Yes\n 2. No \nWould you like to SAVE this list? "))

        if save == 1:
            print("SAVING LIST...")
            save_list = input("What would you like to name the SAVED list as? ")
            with open(f"{save_list}.txt", "w") as saved_file:
                saved_file.write(f"{generate_list}")
            print(f"List SAVED as {save_list}.txt")

        else:
            print("Not SAVING...")

    elif option == 3:
        print("Let's create your Watch List!")


    else:
        print("That was not an Option. Restart Program.")



                

        

            

