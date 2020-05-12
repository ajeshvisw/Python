
def 	eWordSentence(Sentence): 
  
 
    words = Sentence.split("\n ") 
      

    newWords = [word[::-1] for word in words] 
      
 
    newSentence = " ".join(newWords) 
  
    return newSentence 
 
Sentence = "geeks quiz practice code"

print(reverseWordSentence(Sentence)) 
def reverseWordSentence(Sentence): 
  
 
    words = Sentence.split("\n ") 
      

    newWords = [word[::-1] for word in words] 
      
 
    newSentence = " ".join(newWords) 
  
    return newSentence 
 
Sentence = "Split Reverse Join"

print(reverseWordSentence(Sentence)) 