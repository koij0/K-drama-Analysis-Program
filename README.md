# K-drama-Analysis-Program
Analyzes K-drama data for: information search, generation, and list creation

UPDATED: 12/28/25

BRIEF: Analyze K-drama data


DATA MANIPULATION:
- Change deliminator to ("=") {Third Party Site}
- Remove /n in "Synopsis" {Through Excel}
  

QUESTIONS:
- Does episode count contribute to popularity (ie. shorter shows more popular)?
    ~ Average episode count for each incrementage of rating (9+, 8.9-8, etc)
- What is the average rating for Kdramas adapted from Webtoons?
- Most popular streaming services


EXECUTABLES:
- User can ask to get the synopsis of a title
- User can retrieve information of titles
- etc...


FUNCTIONS:
- Information (asks for input to retrieve information)
    ~ title Information
    [IDK if I need these anymore...]
    ~ actor information 
    ~ genre information 
- Generate (generates a rec list) 
    ~ genre (can have multiple genres)
    ~ actor
    ~ episode length
    ~ tags
    ~ random rec
    ~ keywords in synopsis
    ~ streaming platform
- Store/list --> then generate information on list 
- Create a Watch List 
    ~ creates new file (.csv)
    ~ input each show you've watched
    ~ create new categories 
    ~ you can add entries to watch list
    ~ saves lists



ANALYSIS:
- Episode count per rating incrementage 
    * Check for Outliers!!!
- Average rating for "Webtoon Adapted"
- Most popular streaming services (top 3)


  DATA SOURCES:
  
  WordNet File: https://www.kaggle.com/datasets/dfydata/wordnet-dictionary-thesaurus-files-in-csv-format
  
  K-Drama Data: https://www.kaggle.com/datasets/redhata/korean-drama-dataset-2010-2025-2600-titles
