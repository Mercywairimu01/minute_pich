class Pitch:
    '''
    Pitch class to define pitch Objects
    '''

    def __init__(self,id,title,comment,upvote,downvote,user_id,category,time):
        self.id =id
        self.title = title
        self.comment = comment
        self.upvote = upvote
        self.downvote = downvote
        self.user_id = user_id
        self.category =category
        self.time =time
    
