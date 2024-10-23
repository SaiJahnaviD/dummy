def report_count(token):
    # Open and read the file
    with open("corpus.txt", 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Count the occurrences of the token (case-sensitive)
    token_count = content.count(token)
    
    # Print the result in the desired format
    print(f"The term [{token}] shows up in the corpus [{token_count}] times.")