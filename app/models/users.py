from select import select


class User:
    """
    User class to define user objects
    """
    def __init__(self,id,username,email,password,about,bio,avatar,pitches,comment,upvote,downvote):
        self.id =id
        self.username =username
        self.email =email
        self.password =password
        self.about =about
        self.bio =bio
        self.avatar =avatar
        self.pitches =pitches
        self.comment =comment
        self.upvote =upvote
        self.downvote =downvote