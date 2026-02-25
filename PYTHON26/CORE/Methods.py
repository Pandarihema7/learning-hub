class profile:
    def __init__(self,username):
        self.followers=0
        self.username=("_hema_p")
    def follow(self):
        print("someone followed you")
        self.followers+=1
    def update_username(self,new_user_name):
        self.username=new_user_name
p1=profile("_hema_p")
p1.follow()
print(p1.followers)
p1.update_username("p_hema")
print(p1.username)