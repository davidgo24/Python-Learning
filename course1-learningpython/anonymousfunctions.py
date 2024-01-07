'First Class Functions'
def categorize_file(filename):
    get_category = lambda extension: 'Text' if '.txt' in extension else 'Document' if '.docx' in extension else 'Code' if '.py' in extension else 'Unknown'
    
    return get_category(filename[filename.rfind(".") :]) #returns the result of calling the anon fcn get_cat()
