from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import User,UserProfile


@receiver(post_save,sender = User)    
def post_save_create_profile_reciever(sender, instance,created, **kwargs):
    if created :
        # print('created the user profile')
        UserProfile.objects.create(user = instance)
        
    else :
        try:
            # if the user profile found
            profile  = UserProfile.objects.get(user = instance)
            
            profile.save()
            # print("the profile is updated")
        except :
            #create the user profile if not exist
            UserProfile.objects.create(user = instance)
            # print("th eprofile did not exist but newly created")
            
        

# post_save.connect(post_save_create_profile_reciever, sender = User)
@receiver(pre_save,sender = User)
def pre_save_profile_reciever(sender,instance,**kwargs):
    print(instance.username, ' this user is being saved')
    pass