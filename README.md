# K-drama-Analysis-Program
Analyzes K-drama data for: information search, generation, and list creation

UPDATED: 11/12/25

BRIEF: Analyze K-drama data

DATA MANIPULATION:
- Change deliminator to ("=") {Third Party Site}
- Remove /n in "Synopsis" {Through Excel}
  

QUESTIONS:
- Does episode count contribute to popularity (ie. shorter shows more popular)?
  

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
  
    ~ random recommendation
  
    ~ keywords in synopsis
  
    ~ streaming platform
  
- Store/list --> then generate information on list 
- Create a Watch List
  
    ~ creates new file (maybe generate as a spreadsheet or table/doc...?) --> extension (can connect it to .xlsx using pandas)
  
    ~ input each show you've watched
  
    ~ create new category "WATCHED" (bool)
  
    ~ you can add shows to watch list
  
    ~ which categories you want (ie. genre, synopsis, episode count...)
  
    ~ rate Shows (rating category + notes)


  DATA SOURCES:
  WordNet File: https://www.kaggle.com/datasets/dfydata/wordnet-dictionary-thesaurus-files-in-csv-format
  K-Drama Data: https://www.kaggle.com/datasets/redhata/korean-drama-dataset-2010-2025-2600-titles
