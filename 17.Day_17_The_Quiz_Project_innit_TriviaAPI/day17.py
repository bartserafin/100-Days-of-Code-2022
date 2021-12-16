# DAY 17

# Construct a class
class User:
    pass


# This method is fine however, it's prone to error and forces reception for every single object.
user_1 = User()
user_1.id = "001"
user_1.username = "bart"
user_1.password = "321"


# We can use a constructor instead
# with a special function __init__ every attribute will be automatically assigned to new objects
class User2:
    def __init__(self, user_id, username, password):
        # attribute self is reserved for the object itself being created
        # create starting attributes here
        self.user_id = user_id
        self.username = username
        self.password = password


# object user_2 starts with a password "123"
user_2 = User2("002", "fatblue", '123')


# Let's add some methods to our class
class InstagramUser:

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


insta_user_1 = InstagramUser('003', 'paca')
insta_user_2 = InstagramUser('004', 'maca')

insta_user_1.follow(insta_user_2)

print(insta_user_1.followers)
print(insta_user_1.following)
print(insta_user_2.followers)
print(insta_user_2.following)
